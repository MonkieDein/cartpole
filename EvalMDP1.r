library(gdata)
library(ggplot2)
# before MDP
rm(list = ls())
# setwd("~/Desktop/AML/cartpole")
setwd("~/Desktop/GITHUB/cartpole/cartpole")
df = read.csv("cartpole.csv")
# df2 = read.csv("cartpole2.csv")
# df3 = read.csv("cartpolea2.csv")
df4 = read.csv("cartpolea3.csv")
# df5 = read.csv("cartpolea4.csv")

last = c((which(df$Step == 0)[-1] -1),nobs(df))
b4mdp = data.frame(Step=df$Step[last])

# last2=c((which(df2$Step == 0)[-1] -1),nobs(df2))
# aftermdp = data.frame(Step=df2$Step[last2])
# 
# last3=c((which(df3$Step == 0)[-1] -1),nobs(df3))
# aftermdp3 = data.frame(Step=df3$Step[last3])

last4=c((which(df4$Step == 0)[-1] -1),nobs(df4))
aftermdp4 = data.frame(Step=df4$Step[last4])

# last5=c((which(df5$Step == 0)[-1] -1),nobs(df5))
# aftermdp5 = data.frame(Step=df5$Step[last5])


b4mdp$name <- 'default'
# aftermdp$name <- 'MDP'
# aftermdp3$name <- 'MDP3.0'
aftermdp4$name <- 'MDP'
# aftermdp5$name <- 'MDP5.0'

histplot <- rbind(b4mdp, aftermdp4)#,aftermdp3,aftermdp4,aftermdp5)

# hist(b4mdp$Step)
# hist(aftermdp$Step)
# hist(aftermdp3$Step)
# hist(aftermdp4$Step)
# hist(aftermdp5$Step)

ggplot(histplot, aes(Step, fill = name)) + geom_density(alpha = 0.4)

# summary(b4mdp)
# summary(aftermdp)
# summary(aftermdp3)
# summary(aftermdp4)
# summary(aftermdp5)

