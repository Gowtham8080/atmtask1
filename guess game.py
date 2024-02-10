import random as r

num=r.randint(1,15)
guess=int(input("Guess a number b/w 1 to 15: "))
count=0
print("=================================================")
while count<4:
    count=count+1
    if(guess > num):
        print("Guessed number is larger ,try again ")
        guess=int(input("enter a number b/w 1 to 15: "))
        print("=================================================")
    elif(guess < num):
        print("Guessed number is Smaller")
        guess=int(input("enter a number b/w 1 to 15: "))
        print("=================================================")
    elif guess==num:
        break
    
        
if(guess==num):
    print("=================================================")
    print("Good job, you took ",count,"chances" )
    print("The number you guessed is : ",num)

elif(guess!=num):
    print("You Guessed Wrong ,you took ",count,"chances" )
    print("The number is :",num)
