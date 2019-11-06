#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:20:21 2019

@author: jh1111
"""
version = "dcA"

def readinput(filename):
    f = open(filename,"r")
    variable = f.read().split('\n')
    f.close()
    variable = variable[1:]
    variable =[eval(i.split(',')[1]) for i in variable]
    return variable

filename = "Linearfit1.csv"
f = open(filename,"r")
variable1 = f.readlines()
f.close()
variable1 = variable1[1:]
variable1 =[i.split(',')[1:] for i in variable1]
variable1 =[[eval(j) for j in i] for i in variable1]

# COEFICIENT FOR THE EXPECTED CHANGE
filename = "Linearfit0.csv"
f = open(filename,"r")
variable0 = f.readlines()
f.close()
variable0 = variable0[1:]
variable0 =[i.split(',')[1:] for i in variable0]
variable0 =[[eval(j) for j in i] for i in variable0]

def dynamicChoseaction (state):
    expectedS0 = [variable0[i][0]+state[i] for i in range(len(variable0))] 
    expectedS1 = [variable1[i][0]+state[i] for i in range(len(variable1))] 
    for j in range(len(variable0)):
        for i in range(len(variable0[0])-1):
            expectedS0[j] = expectedS0[j] + variable0[j][i+1]*state[i]
            expectedS1[j] = expectedS1[j] + variable1[j][i+1]*state[i]
#    expectedS1 = [1.949e-01+state[1]*1.001,-0.0021675+1.1180181*state[2],-0.2890882+1.0287138*state[3]]
             
    sum0 = abs(expectedS0[2])#sum([abs(i) for i in expectedS0 ])
    sum1 = abs(expectedS1[2])#sum([abs(i) for i in expectedS1 ])

    if sum0 < sum1:
        return 0
    else :
        return 1
  
    
    
    
    
    
    
    
    
    
    
    
    
    