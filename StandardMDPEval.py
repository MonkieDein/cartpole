#from choseaction import *
from dynamicChoseaction import *
## Generate samples
#import pandas as pd
import random
import gym
import tqdm
import csv



env = gym.make('CartPole-v1')

generate_samples = True

random.seed(2019)

if(generate_samples):
    print("Generating samples ...")

    with open(('cartpole'+version+'.csv'), 'w', newline='') as csvfile:
        samplewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        samplewriter.writerow(["Step", "CartPos", "CartVelocity", "PoleAngle", \
                                "PoleVelocity", "Action", "Reward"])
        
        laststate = None
        for k in tqdm.trange(20):
            env.reset()
            done = False
            count = 0
            env.render()
            action = env.action_space.sample()
            j=0
            for i in range(200):                    
                if i > 0:
                    samplewriter.writerow((i-1,) + tuple(state) + (action,) + (reward,))
                j=i
                # stop only after saving the state
                if count ==1:
                  break
                if done:
                  count = 1
                    #time.sleep(0.5)
                    # break
                [state,reward,done,info] = env.step(action) # take a random action
                
                
                env.render()
#                action = choseaction(tuple(state))
                action = dynamicChoseaction(tuple(state))
                
                if action == -1:
                    action = env.action_space.sample()
                
            print("\n",j)
    env.close()
