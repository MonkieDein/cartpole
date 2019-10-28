
def choseaction (state):
  return 0

## Generate samples
#import pandas as pd
import random
import gym
import tqdm
import csv
env = gym.make('CartPole-v1')

generate_samples = True

random.seed(2019)

f = open("a_CartPositionQuantile.csv","r")
cart_quantile = f.read().split(',')
f.close()
f = open("a_CartVelQuantile.csv","r")
cart_velocity = f.read().split(',')
f.close()
f = open("a_PoleAngleQuantile.csv","r")
pole_angle = f.read().split(',')
f.close()
f = open("a_PoleVelocityQuantile.csv","r")
pole_velocity= f.read().split(',')
f.close()

print(cart_quantile )
print(cart_velocity )
print(pole_angle )
print(pole_velocity )


if(generate_samples):
    print("Generating samples ...")

    with open('cartpole.csv', 'w', newline='') as csvfile:
        samplewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        samplewriter.writerow(["Step", "CartPos", "CartVelocity", "PoleAngle", \
                                "PoleVelocity", "Action", "Reward"])
        
        laststate = None
        for k in tqdm.trange(2000):
            env.reset()
            done = False
            count = 0
            for i in range(200):
                env.render()
                action = env.action_space.sample()
                if i > 0:
                    samplewriter.writerow((i-1,) + tuple(state) + (action,) + (reward,))
                
                # stop only after saving the state
                if count ==1:
                  break
                if done:
                  count = 1
                    #time.sleep(0.5)
                    # break
                [state,reward,done,info] = env.step(action) # take a random action
                
                
    env.close()
