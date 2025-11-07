import random
i1 = input("Enter rock-paper-scissor: ")
i1.lower()
li = ["rock", "paper", "scissor"]
i2 = random.choice(li)
cfori1 = 0
cfori2 = 0
print("Computer choose:",i2)
while True:
    if (i1 == "rock" and i2 == "rock") or (i1 == "paper" and i2 == "paper") or (i1 == "scissor" and i2 == "scissor"):  #for Draw
        print("Draw")
        print(f"Your score is {cfori1} and Computer Score is {cfori2}")
        a = input("Do you want to play again? (y/n): ")
        if a == ("y" or "yes"):
            i1 = input("Enter rock-paper-scissor: ")
            i2 = random.choice(li)
            print("Computer choose:",i2)
        else:
            break
    elif (i1 == "rock" and i2 == "scissor") or (i1 == "paper" and i2 == "rock") or (i1 == "scissor" and i2 == "paper"): #for user win
        print("Congratulations!!! You win")
        cfori1 += 1
        print(f"Your score is {cfori1} and Computer Score is {cfori2}")
        a = input("Do you want to play again? (y/n): ")
        if a == ("y" or "yes"):
            i1 = input("Enter rock-paper-scissor: ")
            i2 = random.choice(li)
            print("Computer choose:",i2)
        else:
           break
    elif (i1 == "rock" and i2 == "paper") or (i1 == "paper" and i2 == "scissor") or (i1 == "scissor" and i2 == "rock"): # for User loose
        print("Oops! You Loose !")
        cfori2 += 1
        print(f"Your score is {cfori1} and Computer Score is {cfori2}")
        a = input("Do you want to play again? (y/n): ")
        if a == ("y" or "yes"):
            i1 = input("Enter rock-paper-scissor: ")
            i2 = random.choice(li)
            print("Computer choose:",i2)
        else:
            break
    