# You're a teacher and you've just had a final exam. You need to give out rewards to students. Everyone gets a minimum reward of 1. There are a couple rules to follow however;
#1. All students must receive a minimum reward of 1
#2. and the student must receive more rewards than an adjacent student with a lower exam score, and receive a lower reward than an adjacent student with higher score

def minReward(scores):
    reward = []
    for i in range(len(scores)):
        if scores[i]>scores[i+1]:
            reward.append(1)
    return reward

print(minReward([8,4,2,1,3,6,7,9,5]))


#interview questions? are we given just integers? psoitive integers only? can we have duplicates grades? does the order matter? 

