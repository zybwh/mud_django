#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'terminal/index.html')

def login(request):
    return render(request, 'terminal/login.html')

def reg(request):
    return render(request, 'terminal/reg.html')