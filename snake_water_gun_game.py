'''
rules of the game are : 

1 for snake 
-1 for water
0 for gun

'''

import random 

computer = random.choice([1,-1,0])
yourInput = input("enter your choice as 's' , 'g' , 'w' : ")

youDict = {"s" : 1 , "g" : 0 , "w" : -1}
reverseDict = {1 : "snake" , -1 : "water" , 0 : "gun"}

you = youDict[yourInput]
print(f"computer chooses : {reverseDict[computer]} and you choose : {reverseDict[you]} ")

if computer == you :
    print("Ooops , it's a draw .Try again !!! ")
    
else:
    if computer == 1 and you == -1 :
        print("you lose! ")
        
    elif computer == 1 and you == 0 :
        print("you win! ")
        
    elif computer == -1 and you == 1 :
        print("you win! ")
        
    elif computer == -1 and you == 0 :
        print("you lose! ")
        
    elif computer == 0 and you == -1 :
        print("you win! ")
        
    elif computer == 0 and you == 1 :
        print("you lose! ")
        
    else:
        print("something went wrong . Check again !!!")
        
        
        
        
        
'''
short trick :
first calculate (computer - you )

if (computer - you )== 1 and (computer - you)== -2:
    print("you win")
elif (computer - you )== -1 and (computer - you)== 2:
    print("you lose")

'''