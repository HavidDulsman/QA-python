#!/usr/bin/env python3.8
from random import randint

guessesTaken = 0

def randomNumber():
    secretnumber = randint(1,10)
    return secretnumber
    
session = False
play = input("Welcome to Guess the Number! Do you want to play? (y/n)")
if play == "y":
    session = True
else:
    print("nevermind :(")
    exit()
name = input("What is your name?: ")
print("Welcome " + name + "! guess the number below between 1 - 10")
while session == True:
    secretnumber = randomNumber()
    guess = int(input("Type a number: "))
    if guess == secretnumber:
        print("good job " + name + "! you won!")
        play = input("do you want to play again?:")
        if play == "n":
            session=False
    else:
        guessesTaken = guessesTaken + 1
        print("guess number:" + str(guessesTaken))
        print("no sorry! try again: ")
    
           
            
    