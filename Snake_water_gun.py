import random
list =["s","w","g"]
n=10
up=0
cp=0
print("WELCOME TO THE GAME : There are 10 Rounds\nEnter \"s\" for snake, \"w\" for water, \"g\" for gun")
while(n):
    print(f"\nRound {11-n}")
    user = input("Your Chance: ")
    if user!="s" and user!="w" and user!="g":
        print("\nCaution!!!!! Enter A valid input")
        break
    comp = random.choice(list)
    print(f"Computer: {comp}")
    if(comp == "s"):
        if(user=="w"):
            cp+=1
        elif(user=="g"):
            up+=1
    elif(comp == "w"):
        if(user=="g"):
            cp+=1
        elif(user=="s"):
            up+=1
    elif(comp == "g"):
        if(user=="s"):
            cp+=1
        elif(user=="w"):
            up+=1
    print(f"COMPUTER: {cp}\nYOU: {up}")
    n-=1
if(cp>up):
    print("\nYou Lose!")
elif(up>cp):
    print("\nCongrats You Won!")
elif(up==cp):
    print("\nDraw! Well Played")
print(f"Final Score: Computer-> {cp} You-> {up}")