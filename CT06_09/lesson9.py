import random
num1 = random.randint(1, 10)
guess = int(input("guess a number from 1 to 10"))
print("Guess: " + str(guess))
print("num1: " + str(num1))
print(num1 == guess)