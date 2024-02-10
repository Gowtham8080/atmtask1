import random as r
import time as t
userchoice =""
compchoice=""


def choose():
    global userchoice
    global compchoice
    print("ENTER => STONE / PAPER / SCISSOR :")
    print("")
    t.sleep(1)
    userchoice =input("User Choice : ").lower()
    print("====================================================")
    item =["stone","paper","scissor"]
    compchoice = r.choice(item)
    t.sleep(3)
    print("Computer Choice : ",compchoice)
    
def game():
    global userchoice
    global compchoice
    choose()
    t.sleep(2)
    print("====================================================")
    if(userchoice==compchoice):
        print("Ohh , Match is Draw")
    elif(userchoice=='stone' and compchoice=='paper'):
        print("Hooray ,I won the Game")
    elif(userchoice=='paper' and compchoice=='scissor'):
        print("Hooray ,I won the Game")
    elif(userchoice=='scissor' and compchoice=='stone'):
        print("Hooray ,I won the Game")    
    elif(userchoice=='paper' and compchoice=='stone'):
        print("User won the Game")
    elif(userchoice=='scissor' and compchoice=='paper'):
        print("User won the Game")
    elif(userchoice=='stone' and compchoice=='scissor'):
        print("User won the Game") 
    else:
        print("****Invalid Input****")
game()    
    



