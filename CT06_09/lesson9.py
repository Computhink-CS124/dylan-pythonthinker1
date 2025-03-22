import random
guess = int(input("Guess a number from 1 to 10 "))
num1 = random.randint(1, 10)
print("Guess: "+ str(guess))
print("num1: " + str(num1))
print(num1 == guess
      )