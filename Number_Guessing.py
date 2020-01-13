import random
Secret_Number=int(20*(random.random())+1)
Guess=int(input("Enter a number in range 1 to 20"))
for i in range(2):
    if Guess>0:
        if Guess==Secret_Number:
            print("YOU WON")
            break
        elif Guess<Secret_Number:
            print("Your guess is less than secret number")
            Guess = int(input("New Number:"))
        else:
            print("Your guess is greater than secret number")
            Guess = int(input("New Number:"))

    else:
        print("Negative numbers are not allowed")
        Guess = int(input("New Number:"))
print("GAMEOVER!")