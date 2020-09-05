# You're a teacher and you've just had a final exam. You need to give out rewards to students. Everyone gets a minimum reward of 1. There are a couple rules to follow however;
#1. All students must receive a minimum reward of 1
#2. and the student must receive more rewards than an adjacent student with a lower exam score, and receive a lower reward than an adjacent student with higher score

def minReward(scores):
    rewards = []
    for x in range(len(scores)):
        rewards.append(1)

    for i in range(1, len(scores)):
        j = i-1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j]+1
        else:
            while j >= 0 and scores[j] > scores[j+1]:
                rewards[j] = max(rewards[j], rewards[j+1]+1)
                j -= 1
    rewardSum = sum(rewards)
    return f"The rewards array is: {rewards}, and the sum of the rewards are is: {rewardSum}"
    
print(minReward([8,4,2,1,3,6,7,9,5]))


#interview questions? are we given just integers? psoitive integers only? can we have duplicates grades? does the order matter? 

