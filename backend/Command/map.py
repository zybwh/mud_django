#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.contrib.auth.models import User
from backend.models import *

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
