#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

class MapObject():


    dirs = ['w','s','a','d']
    DIRs = {'w':u'北','s':u'南','a':u'西','d':u'东'}


    worldMap = {
        'luoyang' : {'w': 'taiyuan', 's': 'xiangyang', 'a': 'jingzhaofu', 'd': 'xuzhou'},
        'xiangyang' : {'w': 'luoyang', 's': '', 'a': 'jingzhaofu', 'd': 'yingtianfu'},
        'jingzhaofu' : {'w': 'taiyuan', 's': 'hanzhong', 'a': 'lanzhou', 'd': 'luoyang'},
        'lanzhou' : {'w': '', 's': 'hanzhong', 'a': '', 'd': 'jingzhaofu'},
        'taiyuan' : {'w': '', 's': 'luoyang', 'a': 'jingzhaofu', 'd': ''},    
        'hanzhong' : {'w': 'jingzhaofu', 's': '', 'a': 'lanzhou', 'd': 'xiangyang'},
        'yingtianfu' : {'w': 'xuzhou', 's': '', 'a': 'xiangyang', 'd': ''},
        'xuzhou' : {'w': '', 's': 'yingtianfu', 'a': 'luoyang', 'd': ''},
    }

    dictionary = {
        u'luoyang': u'洛阳',
        u'xiangyang': u'襄阳',
        u'jingzhaofu': u'京兆府',
        u'lanzhou': u'兰州',
        u'taiyuan': u'太原',
        u'hanzhong': u'汉中',
        u'yingtianfu': u'应天府',
        u'xuzhou': u'徐州',
    }


    def getSurround(self, place):
        return self.worldMap[place]

    # def isAtWest(self, src, dest):
    #     return worldMap[src][a] == dest

    # def isAtEast(self, src, dest):
    #     return worldMap[src][d] == dest

    # def isAtNorth(self, src, dest):
    #     return worldMap[src][w] == dest

    # def isAtSouth(self, src, dest):
    #     return worldMap[src][s] == dest

    def moveDirection(self, loc, direction):
        return self.worldMap[loc][direction]

    def translate(self, place):
        return self.dictionary[place]



