#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:42:06 2019

@author: edo
"""

from collections import namedtuple
import numpy as np
import random


higpair  = namedtuple('higpair', 'rank x')
pair = namedtuple('pair','rank x')
doublepair =  namedtuple('doublepair','rank x y')
tris = namedtuple('tris','rank x')
draw = namedtuple('draw','rank x')
color = namedtuple('color', 'rank seed x')
full = namedtuple('full', 'rank x y')
poker = namedtuple('poker', 'rank x')
drawcolor = namedtuple('drawroyal','rank x y' )

listdrawcol = []
lrif=[]
lp= [14,2,3,4,5]
seed = [1,2,3,4]
card = namedtuple('card', 'value seed')

for i in range(len(seed)):
    for k in range(len(lp)):
        lrif.append(card(lp[k],seed[i]))
    listdrawcol.append(lrif)
    lrif=[]


for k in range(len(seed)):
        
    for i in range(2,11):
        
        j=0
        j=i
        while j < i+5:
            
            lrif.append(card(j,seed[k]))
            j+= 1
        listdrawcol.append(lrif)
        lrif=[]













listdraw = []
lp= [14,2,3,4,5]
listdraw.append(lp)
lp=[]
for i in range(2,11):
    j=0
    j=i
    
    while j < i+5:
        lp.append(j)
        j+=1
    listdraw.append(lp)
    lp=[]

def deckgen():
    card = namedtuple('card', 'value seed')
    value = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    seed = [1,2,3,4]
    
    deck=[]
    for i in value:
        for j in seed:
            deck.append(card(i,j))
    
    random.shuffle(deck)
    random.shuffle(deck)
    return deck



dizval={2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J', 12:'Q' ,13:'K', 14:'A'}
dizsem = {1:'spades',2:'flower',3:'diamonds',4:'heart'}




class player():
    
    def __init__(self,card1,card2):
        self.card1 = card1
        self.card2 = card2
        self.action=['call','check','raise','bet','fold']
        self.card = [self.card1,self.card2]
        self.stack = 10000
        self.position=0

    
    def point(self):
        
        #draw color
        if len(self.card)>=5:            
            lp =[]
            for j in range(len(self.card)):
                lp.append(self.card[j])
            for i in range(len(listdrawcol)):
                if set(listdrawcol[i]).issubset(lp):
                    return drawcolor(9,listdrawcol[i][-1].value,listdrawcol[i][0].seed)
                
                
            
        
        
        
        
  
        #poker
        if len(self.card) >=4:
            for i in range(len(self.card)-3):
                for j in range(i+1,len(self.card)-2):
                    for h in range(j+1,len(self.card)-1):
                        for k in range(h+1,len(self.card)):
                            if self.card[i].value==self.card[j].value==self.card[h].value == self.card[k].value:
                                return poker(8,self.card[i].value)
        
        
        
        
        
        
        
        #full
        if len(self.card) >=5:
            listtris = []
            listcopp =[]
            for i in range(len(self.card)-2):
                for j in range(i+1,len(self.card)-1):
                    for h in range(j+1,len(self.card)):
                        if self.card[i].value==self.card[j].value==self.card[h].value:
                            listtris.append(self.card[i].value)
            if len(listtris) >=1:
                for k in range(len(self.card)-1):
                    for p in range(k+1,len(self.card)):                        
                        if self.card[k].value == self.card[p].value != max(listtris):
                            listcopp.append(self.card[k].value)
                if len(listcopp)>=1:
                    return full(7,max(listtris),max(listcopp))
        
        
        
        #color
        if len(self.card) >=5:
            countcolor=[]
            for i in range(len(self.card)-4):
                for j in range(i+1,len(self.card)-3):
                    for k in range(j+1,len(self.card)-2):
                        for h in range(k+1,len(self.card)-1):
                            for p in range(h+1,len(self.card)):
                                
                                if self.card[i].seed ==self.card[j].seed ==self.card[k].seed ==self.card[h].seed ==self.card[p].seed:
                                    
                                    countcolor.append(self.card[i])
                                    countcolor.append(self.card[j])
                                    countcolor.append(self.card[k])
                                    countcolor.append(self.card[h])
                                    countcolor.append(self.card[p])
                            
                                    
        
            if len(countcolor) >=5:
                return color(6,max(countcolor).seed,max(countcolor).value)
                
                                    
                                    
        
        

           
        
        #draw normale
        if len(self.card) >= 5:
            
            lp =[]
            for j in range(len(self.card)):
                lp.append(self.card[j].value)
            for i in range(len(listdraw)):
                if set(listdraw[i]).issubset(lp):
                    return draw(5,listdraw[i][-1])
        
        
        #tris
        if len(self.card) >=3:
            for i in range(len(self.card)-2):
                for j in range(i+1,len(self.card)-1):
                    for h in range(j+1,len(self.card)):
                        if self.card[i].value==self.card[j].value==self.card[h].value:
                            return tris(4,self.card[i].value)
        
        
        
        #doppia pair
        if len(self.card) >=4:
            countpair =[]
            for i in range(len(self.card)-1):
                for j in range(i+1,len(self.card)):
                    #if i==j:
                    #    pass
                    if self.card[i].value == self.card[j].value:
                        countpair.append(self.card[i].value)
            if len(countpair) >= 2:
                cp1= max(countpair)
                countpair.remove(max(countpair))
                cp2 = max(countpair)
                return doublepair(3,cp1,cp2)
                
                            
                            
                        
        
        #pair
        if len(self.card) >=2:
            
            for i in range(len(self.card)-1):
                for j in range(i+1,len(self.card)):
                    if self.card[i].value == self.card[j].value:
                        return pair(2,self.card[i].value)
        
        #pair iniziale
        if len(self.card) ==2:
            
            if self.card1.value == self.card2.value:        
                return pair(2,self.card1.value)
            
        #card alta    
        else:
            c = max(self.card)
            return higpair(1,c)
            
    def getaction(event):
        if event == 'preflop':
            #x = input()
            pass

     
#higpair = namedtuple('')


class table():
    def __init__(self,nplayer):
        self.nplayers=nplayer
        self.nplayer=[]
        self.deck = deckgen()
        self.tablecard=[]        
        for i in range(nplayer):
            self.nplayer.append(player(self.deck.pop(),self.deck.pop()))
            self.nplayer[i].position= i
        self.pot=0
        self.bigb=50
        self.smallb=25
        for p in range(nplayer):
            self.nplayer[p].position=p
            
    
    
    
    def flop(self):
        self.deck.pop()
        self.Flop=[self.deck.pop(),self.deck.pop(),self.deck.pop()]
        self.tablecard= self.tablecard + self.Flop
        for i in range(self.nplayers):
            self.nplayer[i].card += self.Flop
            
        
    
    
    def turn(self):
        self.deck.pop()
        self.Turn=[self.deck.pop()]
        self.tablecard= self.tablecard + self.Turn
        for i in range(self.nplayers):
            self.nplayer[i].card += self.Turn
        
    def river(self):
        self.deck.pop()
        self.River=[self.deck.pop()]
        self.tablecard= self.tablecard + self.River
        for i in range(self.nplayers):
            self.nplayer[i].card += self.River
        
        
    def winner(self):
        totalpoint=[]
        
        for i in range(self.nplayers):
            totalpoint.append(self.nplayer[i].point())
        
        if totalpoint[0]==totalpoint[1]:
            print(totalpoint[0])
            print(totalpoint[1])
            return 'nobody', 11
            print(totalpoint[0])
            print(totalpoint[1])        
        return max(totalpoint),(totalpoint.index(max(totalpoint))) 
        
    
    
    def reset(self):
        self.deck= deckgen()
        self.tablecard=[]
        #self.bigb=50
        #self.smallb=25 
        self.pot=self.bigb + self.smallb
        #self.bigb=50
        #self.smallb=25
        pos=[]
        for i in range(len(self.nplayer)):
            pos.append(self.nplayer[i].position)
        for i in range(len(self.nplayer)):
            self.nplayer[i].card =[]
            self.nplayer[i].card1= self.deck.pop()
            self.nplayer[i].card2= self.deck.pop()
            self.nplayer[i].card =[self.nplayer[i].card1,self.nplayer[i].card2]
            self.nplayer[i].position= pos[i-1]


def getactionpos(movehi,event):
    if event == 'preflop':
        if movehi==0:
            actpos=['2 call','3 raise','4 fold']
            print(actpos)
            actpos1=[2,3,4]
            return actpos1
        if movehi==3:
            actpos=['2 call','3 raise','4 fold']
            print(actpos)
            actpos1=[2,3,4]
            return actpos1
        if movehi==2:
            actpos=['1 check','3 raise']
            print(actpos)
            actpos1=[1,3]
            return actpos1
            
# 1 check , 2 call, 3 raise, 4 fold        
             




