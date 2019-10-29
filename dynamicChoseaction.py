#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:20:21 2019

@author: jh1111
"""
version = "dcA"

def dynamicChoseaction (state):
    expectedS0 = [-1.950e-01+state[1]*1.001,-0.002630+1.126403*state[2],0.2928203+1.0276378*state[3]]
    expectedS1 = [1.949e-01+state[1]*1.001,-0.0021675+1.1180181*state[2],-0.2890882+1.0287138*state[3]]
    if sum(expectedS0) < sum(expectedS1):
        return 0
    else :
        return 1
  
    
    
    
    
    
    
    
    
    
    
    
    
    