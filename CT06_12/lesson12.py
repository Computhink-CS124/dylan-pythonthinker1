# print("Hello from lesson 12")
# visitors = 0
# while visitors < 50:
#     visitors = visitors + 1 # visitors += 1
# print("there are " + str(visitors) + " visitors.")



# visitors = 0
# max = 30
# while visitors < max:
#     add = (input("do u wanna add a visiititiros????? "))
#     if add == "yes":
#         visitors = visitors + 1
#         print("ok  i will add visitor")
#         print("there are " + str(visitors) + " visiititiros now")


order = " "
skipcomma = True
while True:
    userinput = input("What would you like to order???? ")
    if userinput == "end":
        break
    else:
        userinput = input("What would you like to order???? ")
    
    order += "," + userinput
print(order)
