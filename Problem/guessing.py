from random import randint


for x in range(1,8):
    guessNumber = int(input("Enter your Guess between 1 to 8 : "))
    randomNumber = randint(1,7)
    
    if guessNumber == randomNumber:
        print("You Have won")
    else:
        print("You Have Lost")
        print("Random Number Was : ",randomNumber)