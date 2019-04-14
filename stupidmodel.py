#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 23:26:42 2019

@author: edo
"""
from collections import namedtuple
import numpy as np
import random
import pokerrule as pk
import untitled0 as pg
import keras
from keras import Sequential
from keras.layers import Dense, Activation
import tensorflow
import time
'''
THE MODEL IS FIT TO ONLY TO FOLD IN BAD CONDITION
AND RAISE ON MAX VALUE POINT
'''
potodds=0.5
BB=50
pos=1
rankhand=9
stacktobb= 30
outs=0.6

test=np.array([pos,potodds,stacktobb,rankhand,outs]) # rankhand max , raise evere
test3=np.array([0,0.5,30,0,0.10])#rankhand min and outs 10% , fold ever 
test3=test3.reshape((1,5))# shape correct
test = test.reshape((1,5))

g=[1,2,3,4] #possible move check , call , raise , fold
#create test example
tg =np.random.randint(2, size=4)
for i in range(4):
    if i==2:
        tg[i]=1
    else:
        tg[i]=0
print(tg)
th =np.random.randint(2, size=4)
for i in range(4):
    if i==3:
        th[i]=1
    else:
        th[i]=0

print(th)

#create multiexample
X1_test=np.tile(th,(100,1))
Y1_test=np.tile(test3,(100,1))


X_test=np.tile(tg,(100,1))
Y_test=np.tile(test,(100,1))
p_test=np.tile(test3,(100,1))
Xf_test=np.append(X_test,X1_test,axis=0)
Yf_test=np.append(Y_test,Y1_test,axis=0)
Xf_test=np.append(Xf_test,Xf_test,axis=0)
Yf_test=np.append(Yf_test,Yf_test,axis=0)

t1=time.time()
#model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=5))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=4))
model.add(Activation('linear'))

model.compile(loss='mse',
              optimizer='adam',
              metrics=['mae'])
#model fit
model.fit(Yf_test,Xf_test,epochs=180,validation_split=0.2,verbose=0)

t2=time.time()
model.save('stupid_model.h5')

print(t2-t1,'seconds')
#score of model
score = model.predict(test)
print(score)
score3 =model.predict(test3)
print(score3)


'''
print(score2)
print(np.argmax(score2))
if np.argmax(score2)==0:
    mf=(g[np.argmax(score2)])
if np.argmax(score2)==2:
    mf=(g[np.argmax(score2)-1])
if np.argmax(score2)==1:
    mf=(g[np.argmax(score2)-1])
if np.argmax(score2)==3:    
    mf=(g[0])


if len(g)==2:
    np.delete(score2,1)
    np.delete(score2,3)
'''


