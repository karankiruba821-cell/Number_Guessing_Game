import random
secret=random.randint(1,100)
guess=None
attempts=0
print("Welcome to the Game")
print("Your limit is 1 to 100")
while secret!=guess:
    guess=int(input("Enter your guess : "))
    attempts+=1
    if guess>secret:
        print("Too high")
    elif guess<secret:
        print("Too low")
    elif guess==secret:
        print("hurreyyyy !! Your guessing is correct")
        print("Your Attempts :",attempts)