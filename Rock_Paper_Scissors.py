import random
import time
print("The Rules of Rock paper scissor game will be follows: \nRock vs paper --> paper wins \nRock vs scissor --> Rock wins \nPaper vs scissor --> scissor wins")
choices=["Rock","Paper","Scissors"]
dec=1
while(dec!=0):
    pc_choice=random.choice(choices)
    print("-----------")
    print("Please enter your choice number. \n 1. Rock \n 2. paper \n 3. scissor \n")
    choice=int(input())
    if choice==1:
        ur_choice="Rock"
        print("Your Choice is:",ur_choice)
    elif choice==2:
        ur_choice="Paper"
        print("Your Choice is:",ur_choice)
    elif choice==3:
        ur_choice="Scissors"
        print("Your Choice is:",ur_choice)
    else:
        print("Your choice is invalid..")
        decision=True
        continue
    print("-----------")
    print("Now it's computer turn...")
    print("-----------")
    time.sleep(2)
    print("Computer choice is:",pc_choice)
    print("")
    time.sleep(2)
    if((pc_choice=='Rock' and ur_choice=='Scissors') or (pc_choice=='Scissors' and ur_choice=='Paper') or (pc_choice=='Paper' and ur_choice=='Rock')):
        print("Computer won!!")
        print("Better luck next time")
        print("------------")
    elif((ur_choice=='Rock' and pc_choice=='Scissors') or (ur_choice=='Scissors' and pc_choice=='Paper') or (ur_choice=='Paper' and pc_choice=='Rock')):
        print("Congratulations, You won !!")
        print("-----------")
    elif(ur_choice==pc_choice):
        print("Choices are same..So,The match is cancelled..")
        print("-----------")
    fin=1
    while(fin!=0):
        print("Do you want to play again? (yes/no)")
        info=input()
        if info=="yes":
            fin=0
            dec=1
        elif info=="no":
            fin=0
            dec=0
        else:
            print("Invalid choice..")
            print("-----------")
            fin=1
            
print("")        
print("Thanks for playing...Hope you have enjoyed!!")