#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from backend.models import Users
from backend.map.map import MapObject

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
        #return 地图

        surround = mapObject.getSurround(current_location)

        msg = ""

        for direction in surround.keys():
            if surround[direction]:
                msg += u'[[;green;]' + direction + ']: [[;yellow;] '+ mapObject.translate(surround[direction]) + ']   '

        return JsonResponse({'msg': u'你现在位于 [[;yellow;]' + mapObject.translate(current_location) + 
            u'] \n 你可以像以下方向行走：\n ' + msg})
    elif direction == 1:
        dest = mapObject.moveDirection(current_location, 'w')
        if dest:
            Users.objects.filter(userid=request.user.id).update(location=dest)
            return JsonResponse({'msg': u'向北走，前往 [[;yellow;]' + mapObject.translate(dest) + u']'})
        else:
            return JsonResponse({'msg': u'大侠，[[;yellow;]北边] 真的没路了！换个方向吧！'})
    elif direction == 2:
        dest = mapObject.moveDirection(current_location, 's')
        if dest:
            Users.objects.filter(userid=request.user.id).update(location=dest)
            return JsonResponse({'msg': u'向南走，前往 [[;yellow;]' + mapObject.translate(dest) + u']'})
        else:
            return JsonResponse({'msg': u'大侠，[[;yellow;]南边] 真的没路了！换个方向吧！'})
    elif direction == 3:
        dest = mapObject.moveDirection(current_location, 'a')
        if dest:
            Users.objects.filter(userid=request.user.id).update(location=dest)
            return JsonResponse({'msg': u'向西走，前往 [[;yellow;]' + mapObject.translate(dest) + u']'})
        else:
            return JsonResponse({'msg': u'大侠，[[;yellow;]西边] 真的没路了！换个方向吧！'})
    elif direction == 4:
        dest = mapObject.moveDirection(current_location, 'd')
        if dest:
            Users.objects.filter(userid=request.user.id).update(location=dest)
            return JsonResponse({'msg': u'向东走，前往 [[;yellow;]' + mapObject.translate(dest) + u']'})
        else:
            return JsonResponse({'msg': u'大侠，[[;yellow;]东边] 真的没路了！换个方向吧！'})

def goNorth(request):
    return mapFun(request, 1)

def goSouth(request):
    return mapFun(request, 2)

def goWest(request):
    return mapFun(request, 3)

def goEast(request):
    return mapFun(request, 4)

commandList = {'start': start, 'help': helpFun, 'map': mapFun,
                'w': goNorth, 's': goSouth, 'a': goWest, 'd': goEast}

def main(request):
    command = request.POST['command']

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




