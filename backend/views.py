#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

from initial import Initial

# Create your views here.

def start(request):
    if request.POST['token']:
        data = initial.resume(request.POST['token'])
    else:
        initial.new()
        data = {'msg':'欢迎来到mud！\n 输入help获得更多信息'}
    return JsonResponse(data)


def helpFun(request):
    return JsonResponse({'msg': '还没做'})


def mapFun(request):
    return JsonResponse({'msg': '还没做'})

commandList = {'start': start, 'help': helpFun, 'map': mapFun}

def main(request):
    command = request.POST['command']
    if command in commandList:
        return commandList[command](request)
    else:
        return JsonResponse({'msg':'指令错误！输入help获得更多信息'})
