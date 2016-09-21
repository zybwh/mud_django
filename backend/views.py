#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

from initial import Initial

# Create your views here.

def start(request):
    data = {'msg':'欢迎来到江湖群侠传！\n\t 输入help获得更多信息'}
    return JsonResponse(data)


def helpFun(request):
    return JsonResponse({'msg': '还没做'})


def mapFun(request, direction=0):
    if direction == 0:
        #return 地图
        return JsonResponse({'msg': '还没做'})
    elif direction == 1:
        return JsonResponse({'msg': '向北走'})
    elif direction == 2:
        return JsonResponse({'msg': '向南走'})
    elif direction == 3:
        return JsonResponse({'msg': '向西走'})
    elif direction == 4:
        return JsonResponse({'msg': '向东走'})

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
    if command in commandList:
        return commandList[command](request)
    else:
        return JsonResponse({'msg':'指令错误！输入help获得更多信息'})

def loginUser(request):
    username = request.POST.get('user')
    pwd = request.POST.get('password')
    user = authenticate(username=username, password=pwd)
    if user is not None:
        login(request, user)
        return JsonResponse({'msg':'登录成功！', 'code': 1})
    else:
        return JsonResponse({'msg':'用户名密码不正确！', 'code': 0})




