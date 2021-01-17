import numpy as np
import random

def is_Rainbow(card):
    cnt = np.bincount(card)
    flag = True
    for item in cnt:
        if item >=2:
            flag = False
    return flag

rainbow = 0
for num in range(1000000):
    per = num//10000
    if num%10000 == 0:
        print(f"-진행율{per}%"+" ["+"■"*((per//10)+1)+"]", end = '\r')
    card = []
    for i in range(10):
        for j in range(i+1):
            card.append(i+1)

    dealer = random.sample(card, 4)
    for i in range(4):
        card.remove(dealer[i])
    youNeunim = random.sample(card, 3)
    for i in range(3):
        card.remove(youNeunim[i])
    jongMun = random.sample(card, 3)
    for i in range(3):
        card.remove(jongMun[i])
    npcA = random.sample(card, 3)
    for i in range(3):
        card.remove(npcA[i])
    npcB = random.sample(card, 3)
    for i in range(3):
        card.remove(npcB[i])
    if is_Rainbow(dealer+youNeunim) == True:
        rainbow += 1

probability = rainbow/1000000
percentage = probability*100
print("100번 게임 시행 중 "+ str(percentage)+"번 레인보우")