import random
# num1 = int(input("What is the first number? "))
# num2 = int(input("What is the second number? "))
# num3 = int(input("What is the third number? ")) 

# print("First num: " + str(num1))
# print("Second num: " + str(num2) )
# print("Third num: " + str(num3))

# num1iseven = num1 % 2 == 0 
# # num2iseven = num2 % 2 == 0
# # num3iseven = num3 % 2 == 0
# # all_even_odd = num1iseven == num2iseven == num3iseven
# # print(all_even_odd)
# # days = int(input("How many days have you borrowed yiour book for? "))
# # if days > 25:
# #     print("return your book!")
# magicnum = random.randint(1, 10)
# guess = int(input("Guess a number from 1 to 10 "))
# if guess == magicnum:
#     print("Thats the magic number!")


px_apple = 0.60
px_orange = 0.90
costapple = 0
costorange = 0
total = 0

num_apples = int(input("How many apples would you like to buy? "))
num_oranges = int(inout("How many oranges would you like to buy? "))

if num_apples > 5:
    costapple = num_apples *px_apple