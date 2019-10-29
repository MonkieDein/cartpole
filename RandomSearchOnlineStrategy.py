#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:48:39 2019

@author: jh1111
"""
import random
import gym
import tqdm
import csv

env = gym.make('CartPole-v1')
import numpy as np
#CITATION
#http://kvfrans.com/simple-algoritms-for-solving-cartpole/
# Random Search
def run_episode(env, parameters):  
    observation = env.reset()
    totalreward = 0
    for _ in range(200):
        env.render()
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward

def run(env):  
    observation = env.reset()
    for _ in range(200):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            break
    return 0


bestparams = None  
bestreward = 0  

for i in range(200):
    run(env)
env.close()

for _ in range(100):  
    parameters = np.random.rand(4) * 2 - 1
    reward = run_episode(env,parameters)
    if reward > bestreward:
        bestreward = reward
        bestparams = parameters
        # considered solved if the agent lasts 200 timesteps
#        if reward == 200:
#            break
        
env.close()