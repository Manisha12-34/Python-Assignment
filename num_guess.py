import math
import random
def guess_the_number():
    print("Let's start the game:")
    print("Think of a number!!!")
    number_to_guess=random.randint(1,100)
    low=1
    high=100
    num_guess=0
    while True:
        mid_point=(low+high)//2
        guess=input(f"if your guess is:{mid_point}(Enter 'h' if number is higher than you think, 'l' if number is lower than you think, or 'c'if it matches with your guess):")
        num_guess=num_guess+1
        if guess=="c" or guess=="C":
            print(f"Your guess is matched in{num_guess}guesses.")
            break
        elif guess=="h" or guess=="H":
            high=mid_point-1
        elif guess=="l" or guess=="L":
            low=mid_point+1
        else:
            print("Invalid Input")

guess_the_number()