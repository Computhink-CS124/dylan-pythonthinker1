import random
num = int(input("How many questions do you want? "))
for i in range(num):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    ans = int(input("What is " + str(num1) + " x " + str(num2) + "? "))
    print(num1 * num2 == ans)