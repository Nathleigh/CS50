# CS50’s Introduction to Programming with Python - problem set 4 - game
import random

while True:
    level = input("Level: ")
    if level.isdecimal():
        if int(level) > 0:
            level = int(level)
            break
answer = random.choice(range(1, level + 1)) 
while True:
    guess = input("Guess: ").strip()
    if guess.isdecimal():
        if int(guess) > 0:
            guess = int(guess)
            if guess == answer:
                print("Just right!")
                break
            elif guess > answer:
                print("Too large!")
            elif guess < answer:
                print("Too small!")


