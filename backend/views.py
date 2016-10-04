#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from backend.models import *
from backend.map.map import MapObject
from django.forms.models import model_to_dict
import json


# Create your views here.

mapObject = MapObject()

def start(request, command):
    data = {'msg':u'欢迎来到江湖群侠传！\n\t 输入 [[;green;]help] 获得更多信息'}
    return data


def helpFun(request, command):
    return {'msg': '还没做'}

def mapFun(request, args):
    direction = args[0]
    current_location = Users.objects.get(userid=request.user.id).location
    if direction == 'map':
        surround = mapObject.getSurround(current_location)

        msg = u'你现在位于 [[;yellow;]' + mapObject.translate(current_location) + u'] \n'
        msg += u'当前地图有 [[;green;]' + str(mapObject.getPeople(current_location)) + u'] 个人，输入 [[;green;]who] 查看详细信息。\n'
        msg += u'你可以像以下方向行走：\n'

        for direction in surround.keys():
            if surround[direction]:
                msg += u'[[;green;]' + direction + ']: [[;yellow;] '+ mapObject.translate(surround[direction]) + ']   '

        return {'msg': msg}
    else:
        dest = mapObject.moveDirection(current_location, direction)
        if dest:
            Users.objects.filter(userid=request.user.id).update(location=dest, pplList=None)
            res = {'msg': u'向'+mapObject.DIRs[direction]+u'走，前往 [[;yellow;]' + mapObject.translate(dest) + u']'}
            info = mapFun(request, ['map'])
            ppl = who(request, [''])
            res['msg'] += u'\n' + info['msg'] + '\n' + ppl['msg']
            return res

        else:
            return {'msg': u'大侠，[[;yellow;]'+mapObject.DIRs[direction]+u'边] 真的没路了！换个方向吧！'}


def stats(request, command):
    stats = Users.objects.get(userid=request.user).stats
    msg = "气血：[[;red;]" + str(stats.currentHp) + "]/[[;red;]" + str(stats.maxHp) + "]\n"
    msg += "内力：[[;blue;]" + str(stats.currentMana) + "]/[[;blue;]" + str(stats.maxMana) + "]\n"
    msg += "修为：[[;green;]" + str(stats.currentExp) + "]/[[;green;]" + str(stats.nextExp) + "]\n"
    msg += "力量：[[;yellow;]" + str(stats.power) + "]  "
    msg += "灵巧：[[;yellow;]" + str(stats.agility) + "]  "
    msg += "悟性：[[;yellow;]" + str(stats.intelligent) + "]"

    return {'msg': msg}

def who(request, command):
    current_user = Users.objects.filter(userid=request.user.id)
    location = current_user[0].location
    npcs = Npc.objects.filter(location=location).order_by('id')
    users = Users.objects.filter(location=location).order_by('id')
    msg = u'除了你以外，还有 [[;green;]' + str(npcs.count() + users.count() - 1) +  u'] 个人在 [[;yellow;]' + mapObject.translate(location) + u'] 闲逛。\n'
    i = 1

    pplList = {'n':[], 'p':[]}

    for npc in npcs:
        msg += str(i) + '. [[;yellow;]' + npc.username + ']  '
        i += 1
        pplList['n'].append(npc.id)

    for user in users:
        if user.username == current_user[0].username:
            continue
        msg += str(i) + '. [[;blue;]' + user.username + ']  '
        i += 1
        pplList['p'].append(user.id)

    current_user.update(pplList=json.dumps(pplList))

    return {'msg': msg}


def checkNpcExist(request, command):
    index = int(command) - 1 #command starts from 1, index starts from 0
    current_user = Users.objects.get(userid=request.user.id)
    location = current_user.location
    if current_user.pplList is None:
        return 'invalid'

    pplList = json.loads(current_user.pplList)
    if index < len(pplList['n']):
        target = Npc.objects.filter(id=pplList['n'][index], location=location)
    elif index < len(pplList['n']) + len(pplList['p']):
        target = Users.objects.filter(id=pplList['p'][index], location=location)
    else:
        return  None
    return target


def selection(request, args):
    command = args[0]
    target = checkNpcExist(request, command)

    if target == 'invalid':
        return {'msg':'[[;red;]指令错误！输入] [[;green;]help] [[;red;]获得更多信息]'}
    elif target.exists():
        msg = u'[[;yellow;]' + target[0].username + u']\n'
        msg += u'[[;yellow;]' + target[0].guild.name + u']\n'
        msg += target[0].description
        return {'msg': msg}
    else:
        return {'msg': u'这个人已经离开了此地图，请输入[[;green;]who]重新查看当前地图人物。'}

def talk(request, args):
    if len(args) == 1 :
        return {'msg': u'你好像想跟谁说点什么，但是周围并没有人理你。'}
    elif len(args) == 2:
        target = checkNpcExist(request, args[1])
        if target == 'invalid':
            return  {'msg': u'并没有人明白你想说什么。'}      
        elif target.exists():
            msg = u'你走上去想跟 [[;yellow;]' + target[0].username + u'] 说点什么 \n然而他看起来并不想跟你说话。'
            return {'msg': msg}
        else:
            return {'msg': u'这个人已经离开了此地图，请输入[[;green;]who]重新查看当前地图人物。'}
    else:
        return {'msg': '[[;red;]指令错误！输入] [[;green;]help] [[;red;]获得更多信息]'}



commandList = {'start': start, 'help': helpFun, 'stats': stats, 'who': who, 'map': mapFun,
                'w': mapFun, 's': mapFun, 'a': mapFun, 'd': mapFun,
                'talk': talk, 'selection': selection}

@csrf_exempt
def main(request):
    command = request.POST['command'].lower().strip(' ')

    result = {}
    if not request.user.is_authenticated():    
        if command == 'login':
            result = {'msg': '转向登录页面', 'redir': 'login'}
        if command == 'register':
            result = {'msg': '转向注册页面', 'redir': 'reg'}
        result = {'msg': '[[;red;]您还没有登录！]\n\t请输入 [[;green;]login]     进行登录\n\t或者   [[;green;]register]  进行注册！'}
    else:
        if command == 'logout':
            logout(request)
            result = {'msg': '登出成功！'}

        # if not Users.objects.filter(userid=request.user.id).exists():
        #     Users.objects.create(userid=request.user.id, )

        args = command.split(' ')


        if args[0] >= '1' and args[0] <= '9':
            result = commandList['selection'](request, args)
        elif args[0] in commandList:
            result = commandList[args[0]](request, args)
        else:
            result = {'msg': '[[;red;]指令错误！输入] [[;green;]help] [[;red;]获得更多信息]'}

    return JsonResponse(result)


@csrf_exempt
def loginUser(request):
    username = request.POST.get('user')
    pwd = request.POST.get('password')
    user = authenticate(username=username, password=pwd)
    if user is not None:
        login(request, user)
        return JsonResponse({'msg':'登陆成功！', 'code': 1})
    else:
        return JsonResponse({'msg':'用户名密码不正确！', 'code': 0})

@csrf_exempt
def regUser(request):
    username = request.POST.get('user')
    pwd = request.POST.get('password')
    if User.objects.filter(username=username).exists():
        return  JsonResponse({'msg':'用户名已存在！', 'code': 0})
    user = User.objects.create_user(username,'',pwd)
    return JsonResponse({'msg':'注册成功！', 'code': 1})




