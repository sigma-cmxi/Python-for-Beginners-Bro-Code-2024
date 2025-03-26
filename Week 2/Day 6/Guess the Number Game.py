import random

r = random.randint(1, 50)
g = int(input("Guess a number between 1 and 50: "))

while r != g:
    print("Wrong answer, try again!")
    g = int(input("Guess a number between 1 and 50: "))

print(f"You guessed correct! The number is {g}.")
