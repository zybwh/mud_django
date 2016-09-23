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

# Create your views here.

mapObject = MapObject()

def start(request):
    data = {'msg':u'欢迎来到江湖群侠传！\n\t 输入 [[;green;]help] 获得更多信息'}
    return JsonResponse(data)


def helpFun(request):
    return JsonResponse({'msg': '还没做'})

def mapFun(request, direction=0):
    current_location = Users.objects.get(userid=request.user.id).location
    if direction == 0:
        surround = mapObject.getSurround(current_location)

        msg = ""

        for direction in surround.keys():
            if surround[direction]:
                msg += u'[[;green;]' + direction + ']: [[;yellow;] '+ mapObject.translate(surround[direction]) + ']   '

        return JsonResponse({'msg': u'你现在位于 [[;yellow;]' + mapObject.translate(current_location) + 
            u'] \n 你可以像以下方向行走：\n ' + msg})
    else:
        dest = mapObject.moveDirection(current_location, direction)
        if dest:
            Users.objects.filter(userid=request.user.id).update(location=dest)
            return JsonResponse({'msg': u'向'+mapObject.DIRs[direction]+u'走，前往 [[;yellow;]' + mapObject.translate(dest) + u']'})
        else:
            return JsonResponse({'msg': u'大侠，[[;yellow;]'+mapObject.DIRs[direction]+u'边] 真的没路了！换个方向吧！'})

def makeStatsMsg(stats):
    msg = "气血：[[;red;]" + str(stats.currentHp) + "]/[[;red;]" + str(stats.maxHp) + "]\n"
    msg += "内力：[[;blue;]" + str(stats.currentMana) + "]/[[;blue;]" + str(stats.maxMana) + "]\n"
    msg += "修为：[[;green;]" + str(stats.currentExp) + "]/[[;green;]" + str(stats.nextExp) + "]\n"
    msg += "力量：[[;yellow;]" + str(stats.power) + "]  "
    msg += "灵巧：[[;yellow;]" + str(stats.agility) + "]  "
    msg += "悟性：[[;yellow;]" + str(stats.intelligent) + "]"

    return msg


def stats(request):
    stats = Users.objects.get(userid=request.user).stats
    msg = makeStatsMsg(stats)
    return JsonResponse({'msg': msg})



commandList = {'start': start, 'help': helpFun, 'map': mapFun,
                'stats': stats}

@csrf_exempt
def main(request):
    command = request.POST['command'].lower()



    if not request.user.is_authenticated():    
        if command == 'login':
            return JsonResponse({'msg': '转向登录页面', 'redir': 'login'})
        if command == 'register':
            return JsonResponse({'msg': '转向注册页面', 'redir': 'reg'})
        return JsonResponse({'msg': '[[;red;]您还没有登录！]\n\t请输入 [[;green;]login]     进行登录\n\t或者   [[;green;]register]  进行注册！'})
    else:
        if command == 'logout':
            logout(request)
            return JsonResponse({'msg': '登出成功！'})

        # if not Users.objects.filter(userid=request.user.id).exists():
        #     Users.objects.create(userid=request.user.id, )
        if command in mapObject.dirs:
            return mapFun(request, command)
        if command in commandList:
            return commandList[command](request)
        else:
            return JsonResponse({'msg':'指令错误！输入help获得更多信息'})

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




