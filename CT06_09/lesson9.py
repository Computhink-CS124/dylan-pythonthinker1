import random
num = int(input("How many questions do you want? "))
for i in range(num):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    ans = int(input("What is " + (num1) + "x"))