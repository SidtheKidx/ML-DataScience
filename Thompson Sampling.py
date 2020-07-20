#Thompson Sampling 
#Upper Confidence Bound 

#Importing the libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

#Importing the dataset 
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')



#Implementing UCB 
import random 
N= 10000
d = 10
ads_selected = []
number_of_rewards_1 = [0] * d
number_of_rewards_0 = [0] * d
total_reward = 0
for n in range(0, N):
    ad = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(number_of_rewards_1[i] +1, number_of_rewards_0[i] +1)
        
        if ( random_beta > max_random):
            max_random = random_beta
            ad = i
   
    ads_selected.append(ad)
    reward = dataset.values[n, ad]  
    if (reward == 1):
        number_of_rewards_1[ad] += 1
    else:
        number_of_rewards_0[ad] += 1
    
    total_reward = total_reward + reward 


#Visualising
import seaborn as sns
sns.set()

plt.hist(ads_selected)
plt.title('Histogram of ads selection')
plt.xlabel('Ads')
plt.ylabel('No. of each ad was selected')
plt.show()

    
    

"""
#Implementing Thompson Sampling 
import math
(N,d)=(dataset.shape[0],dataset.shape[1]) #get row and col values
(num_of_selections,sum_of_rewards) = ([0] * d,[0] * d) #initialize
(avg_reward,ucb) = ([0] * d,[0] * d) #initialize
ad_selected=[] #initialize
ad=0 #initialize

for n in range(0,N): #read thru every row
    
    if n < d: #have we tried all ads atlest once
        ad = n #try that ad
    else:
        ad = ucb.index(max(ucb)) #else get ad with max upper confidence bound
    
    ad_selected.append(ad)   #add the ad selected 
    sum_of_rewards[ad] += dataset.values[n,ad] #update the reward for selected ad
    num_of_selections[ad] += 1 #update number of selection for selected ad
    avg_reward[ad] = sum_of_rewards[ad]/num_of_selections[ad] #update avg reward for selected ad
    delta = math.sqrt(3/2*math.log(n+1)/num_of_selections[ad]) #delta for selected ad
    ucb[ad]= avg_reward[ad]+delta #update upper confidence bound for selected ad
total_rewards = sum(sum_of_rewards) #calcualte total rewards earned

"""