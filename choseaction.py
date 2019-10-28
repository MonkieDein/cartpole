#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:38:22 2019

@author: jh1111
"""
def readinput(filename):
    f = open(filename,"r")
    variable = f.read().split('\n')
    f.close()
    variable = variable[1:-1]
    variable =[eval(i.split(',')[1]) for i in variable]
    return variable




version = "a3"
if version!="a3":
    cart_quantile = readinput( version +"_CartPositionQuantile.csv")
else :
    cart_quantile = [1]
cart_velocity  = readinput( version +"_CartVelQuantile.csv")
#readinput("a_policy.csv")
pole_angle = readinput( version +"_PoleAngleQuantile.csv")
pole_velocity=readinput( version +"_PoleVelocityQuantile.csv")
statemap = readinput( version +"_StateMap.csv")
statearr = readinput( version +"_StateArr.csv")
reward1 = readinput( version +"_Reward1.csv")
reward2= readinput( version +"_Reward2.csv")
policy= readinput( version +"_policy.csv")

#print(cart_quantile )
#print(cart_velocity )
#print(pole_angle )
#print(pole_velocity )

statemap = [i-1 for i in statemap]
statearr = [i-1 for i in statearr]

def choseaction (state):
    
    if (version!="a3"):
        i=sum([(state[0]>=x) for x in cart_quantile])-1
    else :
        i=0
    j=sum([(state[1]>=x) for x in cart_velocity])-1
    k=sum([(state[2]>=x) for x in pole_angle])-1
    l=sum([(state[3]>=x) for x in pole_velocity])-1
    
    if i<0 or j<0 or k<0 or l<0 :
        return -1
    
    
    value = i + j*len(cart_quantile) +  k*len(cart_quantile)*len(cart_velocity)+  l*len(cart_quantile)*len(cart_velocity)*len(pole_angle)
#    print(statemap[value], policy[statemap[value]])
#    print(i,j,k,l,value)
    return (policy[statemap[value]])


