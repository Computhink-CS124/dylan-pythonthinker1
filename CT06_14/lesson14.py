# print("Hello from lesson 15")
i = 0
pisatopping = [
"mushrooms", 
"pepperoni",
"cheese"
]
userinput = []
while True:
    print(str(i + 1) + str(pisatopping[i]))
    for item in pisatopping:
        userinput.append = int(input("Wut topping u want?????"))
        if userinput == "end":
            break
        else:
            userinput.append(pisatopping[int(userinput) - 1])
print( )