#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from backend.models import *

def createGuild(glist):
    for g in glist:
        if not Guilds.objects.filter(name=g).exists():
            Guilds.objects.create(name=g)

def createNpc(npclist):
    for npc in npclist:
        if not Npc.objects.filter(username=npc['name']).exists():
            stats = UserStats.objects.create()
            Npc.objects.create(username=npc['name'], location=npc['location'], stats=stats, description=npc['description'], guild=Guilds.objects.get(name=npc['guild']))



def guild():
    glist = [u'少林', u'武当', u'峨眉', u'明教', u'华山派', u'日月明教', u'丐帮', u'逍遥派', u'六扇门', u'五毒教']
    createGuild(glist)

def npc():
    npclist = [
    {'name': u'张三丰', 'location': 'zijincheng', 'description': u'年约百岁，发如白霜，道骨仙风，看起来气质非凡，手中真武剑削铁如泥，武功震古烁今', 'guild': u'武当'},
    {'name': u'宋远桥', 'location': 'zixiaodian', 'description': u'年约五六十岁，三络长须，温文尔雅，看起来稳重踏实，手中武当长剑锋锐无比，武功登峰造极', 'guild': u'武当'},
    {'name': u'俞莲舟', 'location': 'longhudian', 'description': u'年约五六十岁，生性严峻，沉默寡言，看起来豪气万丈，手中虎爪手损阴绝嗣，武功登峰造极', 'guild': u'武当'},
    {'name': u'俞岱岩', 'location': 'longhudian', 'description': u'年约五六十岁，鼻梁高耸，气宇轩昂，看起来精干英挺，手中武当长剑锋锐无比，武功超群绝伦', 'guild': u'武当'},
    {'name': u'张松溪', 'location': 'yuxugong', 'description': u'年约四五十岁，身材矮小，遇人恭谨，看起来足智多谋，手中太极拳出神入化，武功超群绝伦', 'guild': u'武当'},
    {'name': u'张翠山', 'location': 'yuxugong', 'description': u'年约三四十岁，面目俊秀，神朗气爽，看起来天赋卓然，手中判官笔独步天下，武功超群绝伦', 'guild': u'武当'},
    {'name': u'殷梨亭', 'location': 'taijiguangchang', 'description': u'年约三四十岁，长身玉立，遇人恭谨，看起来温文尔雅，手中武当长剑锋锐无比，武功超群绝伦', 'guild': u'武当'},
    {'name': u'莫声谷', 'location': 'taijiguangchang', 'description': u'年约三四十岁，魁梧奇伟，满脸浓髯，看起来豪气万丈，手中武当长剑锋锐无比，武功超群绝伦', 'guild': u'武当'},
    {'name': u'宋青书', 'location': 'taijiguangchang', 'description': u'年约二十岁，眉目清秀，长身玉立，看起来天赋卓然，手中武当长剑锋锐无比，武功炉火纯青', 'guild': u'武当'},
    ]
    createNpc(npclist)








