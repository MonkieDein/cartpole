# setwd("~/POMDP")
setwd("~/Desktop/GITHUB/cartpole/cartpole/POMDP")
library(pomdp)
ExpectedRew = read.csv("ExpectedRew")[,-1]
Transition0 =as.matrix.data.frame(read.csv("Transition0")[,-1])
Transition1 =as.matrix.data.frame(read.csv("Transition1")[,-1])
init_freq = read.csv("initfreq")[,-1]
# Splitstate=10
# n_var =3
# state2obs = matrix(0,Splitstate^(n_var),Splitstate^(n_var-1))
# for (i in 1:(Splitstate^(n_var))){
#   if (i%%10 == 0 ){
#     state2obs[i,((((i-1)%/%100)+1)*10)] = 1
#   } else {
#     state2obs[i,((i%/%100)*10+i%%10)] = 1
#   }
# }
# generate_s2o = TRUE
# if (generate_s2o){
#   write.csv(state2obs,"ObsTransitionState")
# }
ObsTransitionState = as.matrix.data.frame(read.csv("ObsTransitionState")[,-1])

anything = rep("*",(10^3))

mystates = as.character(1:(10^3))
for (i in 1:length(mystates)){mystates[i] = paste0("state",mystates[i])}
myobs = as.character(1:100)
for (i in 1:length(myobs)){myobs[i] = paste0("obs",myobs[i])}
myaction = as.character(0:1)
for (i in 1:length(myaction)){myaction[i] = paste0("action",myaction[i])}


rewarddf =data.frame(
  "action" = anything,"start-state"=anything,"end-state"=mystates,
  "observation" = anything,"reward" = ExpectedRew)
# can let start to be "uniform" and solve the first error but what if I have a distribution for start
  cartpole <- POMDP(
    name = "cartpole",
    discount = 0.95,
    states = mystates,
    actions = c("action0","action1"), # myaction
    observations = myobs,
    start = "uniform" , #init_freq
    transition_prob = list("action0" = Transition0  , "action1" = Transition1),#Transition0 Transition1
    observation_prob = list("action0" = ObsTransitionState,"action1" = ObsTransitionState), #t(ObsTransitionState)
    reward = rewarddf
  )
  cartpole
  cartpole_solved <- solve_POMDP(cartpole)
  plot(cartpole_solved)
