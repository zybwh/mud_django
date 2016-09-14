#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import os
import json

class Initial :
    def new(self):
        # with open('txtFile' + os.sep + 'welcome.txt', 'r') as data_file:
        #     data = json.load(data_file)
        # return data
        return 0

    def resume(self):
        return 0

