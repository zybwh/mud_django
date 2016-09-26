#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from backend.models import *

class MapObject():


    dirs = ['w','s','a','d']
    DIRs = {'w':u'北','s':u'南','a':u'西','d':u'东'}




    worldMap = {
        #洛阳
        'luoyang' : {'w': 'taiyuan', 's': 'luoyangnan', 'a': 'jingzhaofu', 'd': 'xuzhou'},
        'luoyangnan': {'w': 'luoyang', 's': 'songshanjiao', 'a': '', 'd': ''},
        #少林
        'songshanjiao': {'w': 'luoyangnan', 's': 'wudangshanjiao', 'a': '', 'd': ''},
        #武当
        'wudangshanjiao': {'w': 'songshanjiao', 's': 'xiangyangbei', 'a': '', 'd':'wudangshan'},
        'wudangshan' : {'w': 'taijiguangchang', 's': '', 'a': 'wudangshanjiao', 'd':''},
        'taijiguangchang': {'w': 'zixiaodian', 's': 'wudangshan', 'a': '', 'd': 'longhudian'},
        'zixiaodian': {'w': 'zijincheng', 's': 'taijiguangchang', 'a:': 'yuxugong', 'd': ''},
        'zijincheng': {'w': '', 's':'zixiaodian', 'a': '', 'd': ''},
        'yuxugong' : {'w': '', 's': '', 'a': '', 'd': 'zixiaodian'},
        'longhudian': {'w': '', 's': '', 'a': 'taijiguangchang', 'd': ''},
        #襄阳
        'xiangyangbei': {'w': 'wudangshanjiao', 's': 'xiangyang', 'a': '', 'd': ''},
        'xiangyang' : {'w': 'xiangyangbei', 's': '', 'a': 'jingzhaofu', 'd': 'yingtianfu'},
        #京兆府
        'jingzhaofu' : {'w': 'taiyuan', 's': 'hanzhong', 'a': 'lanzhou', 'd': 'luoyang'},
        #兰州
        'lanzhou' : {'w': '', 's': 'hanzhong', 'a': '', 'd': 'jingzhaofu'},
        #太原
        'taiyuan' : {'w': '', 's': 'luoyang', 'a': 'jingzhaofu', 'd': ''},    
        #汉中
        'hanzhong' : {'w': 'jingzhaofu', 's': '', 'a': 'lanzhou', 'd': 'xiangyang'},
        #应天府
        'yingtianfu' : {'w': 'xuzhou', 's': '', 'a': 'xiangyang', 'd': ''},
        #徐州
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
        u'luoyangnan': u'洛阳南',
        u'songshanjiao': u'嵩山脚',
        u'wudangshanjiao': u'武当山脚',
        u'wudangshan': u'武当山',
        u'xiangyangbei': u'襄阳北',
        u'taijiguangchang': u'太极广场',
        u'zixiaodian': u'紫霄殿',
        u'zijincheng': u'紫金城',
        u'yuxugong': u'玉虚宫',   
        u'longhudian': u'龙虎殿'
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

    def getPeople(self, place):
        return Npc.objects.filter(location=place).count() + Users.objects.filter(location=place).count()



