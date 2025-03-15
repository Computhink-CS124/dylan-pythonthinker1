# print("Hello from lesson 8")
# import time
# sec = int(input("How many seconds do you want to countdown from? "))
# for i in range(sec, 0, -1):
#     print(i)
#     time.sleep(1)
# print ("the bomb exploded!")
# import random 

# num = random.randint(0, 6)
# print (num)

# for i in range(10):
#     num = random.randint(0,9999)
#     print(num)

# num1 = 3 == 5
# print(num1)

# num2 = 3 == 3
# num3 = 4 == 4
# print(num2 == num3)

# num4 = 8 == 8
# num5 = 8 == 42
# print(num4 == num5)

import random
num1 = random.randint(1, 50)
num2 = random.randint(1, 50)
ans = input("what is " + str(num1) + " +" + str(num2) + " ?")
print (num1+num2 == ans)