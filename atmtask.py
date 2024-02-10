import datetime as d

global defamt
defamt=50000

def credit():
     global defamt
     print("Enter amount to be credited...")
     amt=int(input())
     defamt=defamt+amt
     t.sleep(2)
     print("Your amount has been Credited")
     print("Total balance is: ",defamt)
     print("==================================================")
     t.sleep(4)
     print("Please remove your card")
     t.sleep(4)
     print("==================================================")
     print("Thanks for Visiting SGS Bank..")
     print(d.datetime.now())
     t.sleep(5)
     print("")
     print("")
     main()


def withdraw():
    global defamt
    print("Cash Available Muliplies of :Rs.100,Rs.500)")
    amt=int(input("Enter the amount: "))
    if(amt<defamt):
        defamt=defamt-amt
        print("Please Wait..")
        print("Your transaction is being processed...")
        t.sleep(2)
        print("Please take the cash...")
        print("Total balance is : ",defamt)
        print("==================================================")
        t.sleep(4)
        print("Please remove your card")
        print("==================================================")
        t.sleep(4)
        print("Thanks for Visiting SGS Bank..")
        t.sleep(5)
        print("")
        print("")
        main()
    else:
         print("Enter amount less than Available Balance")
def balance():
    global defamt
    pass_word = 12345
    print("Enter the pin:")
    pin=int(input())
    if(pass_word == pin):
        print("Checking Balance......")
        t.sleep(3)
        print("Available Balance is: ",defamt)
        print("==================================================")
        print("Thanks for Visiting SGS Bank..")
        print(d.datetime.now())
        t.sleep(5)
        print("")
        print("")
        main()


    
def exit():
    global defamt
    print("Thanks for Visiting SGS Bank..")
    t.sleep(2)
    print(d.datetime.now())
    



import random as r
   
def otp():
    otp=""
    for i in range(1,5):
        otp=r.randint(1000,9999)
    print(otp)    





def current():
    global defamt
    print("Cash Available Muliplies of :Rs.500")
    print("Please Enter the Amount: ")
    amt=int(input())
    if(amt<defamt):
        defamt=defamt-amt
        print("Your transaction is being processed...")
        print("Enter the OTP: " )
        t.sleep(6)
        otp()
        t.sleep(5)
        print("Please Wait....")
        print("Your Transaction is being Processed...")
        t.sleep(5)
        print("Please Collect the Cash...")
        t.sleep(3)
        print("Available Balance is: ",defamt)      
        t.sleep(2)
        print("Please remove your card")   
        print("Thanks for Visiting SGS Bank..")
        print(d.datetime.now())
        t.sleep(5)
        print("")
        print("")
        main()     
    else:
         print("Enter amount less than Available Balance")
        

        
import time as t

def main():
    
    user_name = 'GOWTHAM'
    pass_word = 12345
    defamt= 50000
    print("Welcome to SGS Bank")
    print("======================================================")
    print("Please Insert your Card...")
    print("======================================================")
    t.sleep(3)
    print("Wait for 5 Second......")
    print("======================================================")
    t.sleep(5)
    print('Enter your Name: ')
    name=str(input())
    t.sleep(2)
    print('Enter your Pin: ')
    pin=int(input())
    print("=======================================================")
    if(user_name==name and pass_word==pin):
        t.sleep(2)
        print("Hello",name,"you are logged in")
        print("===================================================")
        typ=print("select Account Type: 1.Savings / 2.Current")
        t.sleep(1)
        types=int(input())
        if(types==1):
            print("1.Credit")
            print("2.Withdraw")
            print("3.Balance check")
            print("4.Exit")
            print("Choose any one : ")
            choice=int(input())
            if(choice==1):
                credit()
            elif(choice==2):
                withdraw()
            elif(choice==3):
                balance()
            elif(choice==4):
                exit()
        elif(types==2):
            current()
            
            
            
        
    else:
         print("Invalid user and password")
         exit()


main()































