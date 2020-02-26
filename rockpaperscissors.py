#!/usr/bin/env python3.8
import random #4. import modules


session = True #0. create session


decisions = ["rock", "paper", "scissors"] #5. create variables + options


rock_counter = 0
paper_counter = 0 #10. EXTRA BIT: machine learning!
scissors_counter = 0


def better_decision ():
    max_counter = max(rock_counter, paper_counter, scissors_counter) #12. variable that can only be used in this function!!!!
    if rock_counter == max_counter:
        return 1 #13. variables need a returned value to be completed!!!!
    elif paper_counter == max_counter:
        return 2
    elif scissors_counter == max_counter:
        return 0
    else:
        return randint(0,2)#14. if there hasnt been any decisions, 


while session:
    computer_decision =  better_decision() #7. create computer inputs (old function = random.randint(0,2))
    player_decision = int(input("select 0 for rock, 1 for paper or 2 for scissors:")) #6. create user inputs

    if player_decision == computer_decision:
        if player_decision == 0:
            rock_counter +=1
        if player_decision ==1: #11. machine learning: machine increments values based of what the USER has chosen
            paper_counter +=1
        if player_decision ==2:
            scissors_counter +=1
        print("tie!" + " you selected " + decisions[player_decision] + ", computer selected " + decisions[computer_decision])
    elif player_decision == 0 and computer_decision == 1:
        rock_counter += 1 
        print("you lose" + " you selected " + decisions[player_decision] + ", computer selected " + decisions[computer_decision])#8. create game rules
    elif player_decision == 1 and computer_decision == 2:
        paper_counter +=1
        print("you lose" + " you selected " + decisions[player_decision] + ", computer selected " + decisions[computer_decision])#9. display the decisions of both players!
    elif player_decision == 2 and computer_decision == 0:
        print("you lose" + " you selected " + decisions[player_decision] + ", computer selected " + decisions[computer_decision])
        scissors_counter +=1
    else:
        if player_decision == 0:
            rock_counter +=1
        if player_decision ==1: #12. machine learning: machine increments values based of what the USER has chosen
            paper_counter +=1
        if player_decision ==2:
            scissors_counter +=1
            print("you win!" + " you selected " + decisions[player_decision] + ", computer selected " + decisions[computer_decision])   
    
    play = input("do you want to play again?: (y/n)") #1. create loop
    if play.lower() =="n":
        session = False
    elif play.lower() =="y":
        pass
    else:
        print("not valid. try again") #2. option to close loop