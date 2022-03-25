#game of random numbers in python
#its imposible to beat in hard mode
import os
from time import sleep as sleep#importing sleep from time module
from random import randint as randint#importing randint from random module
pname = str(input('playername: '))#playername
t = int(input('how many games you wanna play!: '))#asks you how many games you wanna play
mode = str(input('easy or medium or hard mode?: '))#mode
n = 1
#setting up the scoreboard
pscore = 0
bscore = 0
pscoretotal = []
bscoretotal = []
#the game starts now
if mode == 'easy':
    while n <= t:
        pscore = 0
        bscore = 0
        rand = randint(1, 1000)#random number is generated randomly between 1 - 1000
        print('the random number has been generated between 1-1000, you have 18 tries good luck')
        #each round has 18 tries, get it wrong in anyone try the bot gets a point, if not you get a point
        for x in range(0,18):
            ted = int(input("can you guess it!: "))
            if ted == rand:
                print('you got that right')
                pscore = pscore + 1
                break
            elif ted <= rand: 
                print('your guess was lower than the random number')
                bscore = bscore + 1
            elif ted >= rand:
                print('your guess was more than the random number')
                bscore =+ 1
        n = n + 1
        sleep(1)#sets delay to 1 seconds
        os.system('clear')#clearing the gameboard
        #and printing you scores
        print('your score:', pscore)
        print('bot score:', bscore)



        #using list to collect scores across the games
        bscoretotal.append(bscore)
        pscoretotal.append(pscore)
elif mode == 'medium':
    while n <= t:
        pscore = 0
        bscore = 0
        rand = randint(1, 1000)#random number is generated randomly between 1 - 1000
        print('the random number has been generated between 1-1000, you have 14 tries good luck')
        #each round has 14 tries, get it wrong in anyone try the bot gets a point, if not you get a point
        for x in range(0,14):
            ted = int(input("can you guess it!: "))
            if ted == rand:
                print('you got that right')
                pscore = pscore + 3
                break
            elif ted <= rand: 
                print('your guess was lower than the random number')
                bscore = bscore + 3
            elif ted >= rand:
                print('your guess was more than the random number')
                bscore =+ 1
        n = n + 1
        sleep(1)#sets delay to 1 seconds
        os.system('clear')#clearing the gameboard
        #and printing you scores
        print('your score:', pscore)
        print('bot score:', bscore)



        #using list to collect scores across the games
        bscoretotal.append(bscore)
        pscoretotal.append(pscore)
elif mode == 'hard':
    while n <= t:
        pscore = 0
        bscore = 0
        rand = randint(1, 1000)#random number is generated randomly between 1 - 1000
        print('the random number has been generated between 1-1000, you have 7 tries good luck')
        #each round has 7 tries, get it wrong in anyone try the bot gets a point, if not you get a point
        for x in range(0,7):
            ted = int(input("can you guess it!: "))
            if ted == rand:
                print('you got that right')
                pscore = pscore + 7
                break
            elif ted <= rand: 
                print('your guess was lower than the random number')
                bscore = bscore + 7
            elif ted >= rand:
                print('your guess was more than the random number')
                bscore =+ 1
        n = n + 1
        sleep(1)#sets delay to 1 seconds
        os.system('clear')#clearing the gameboard
        #and printing you scores
        print('your score:', pscore)
        print('bot score:', bscore)



        #using list to collect scores across the games
        bscoretotal.append(bscore)
        pscoretotal.append(pscore)


#adds all the values in alist
def addvalues(list):
    total = 0
    for i in list:
        total = total + i
    return total

#printing the scoreboard
os.system('clear')
print('the scoreboard is:')
print('player:', pname, 'score:', addvalues(pscoretotal))
print('bot:', 'score:', addvalues(bscoretotal))
