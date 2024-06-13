# Task 1

import random

weapons = ["sword", "gun", "knife", "axe"]
random_choice = random.choice(weapons)

while True:
    user = input("Guess the weapon! sword, gun, knife, axe?  ")
    if user == random_choice:
        print("congrats! you guessed correctly, it was {random_choice}")
        # break
    else:
        print("oopsie wrong guess, guess again! ")
        print("thanks for playing")
        
   






