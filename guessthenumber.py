#game of random numbers in python
import os
from time import sleep as sleep#importing sleep from time module
from random import randint as randint#importing randint from random module
pname = str(input('playername: '))#playername
t = int(input('how many games you wanna play!: '))#asks you how many games you wanna play
n = 1
#setting up the scoreboard
pscore = 0
bscore = 0

#the game starts now
while n <= t:
    rand = randint(1, 1000)#radnom number is generated randomly
    print('the random number has been generated between 1-1000, you have 10 tries good luck')
    x = 0
    #each round has 10 tries, get it wrong in anyone try the bot get a point, if not you get a point
    while x <= 10:
        ted = int(input("can you guess it!: "))
        if ted == rand:
            print('you got that right')
            score = score + 1
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
print('your score:', score)
print('bot score:', bscore)
#and the winner is
if score == bscore:
    print('tie')
elif score > bscore: 
    print("the", pname,'won congratulations on beating the bot')
elif score < bscore: 
    print("the bot wins, better luck next time", pname)
