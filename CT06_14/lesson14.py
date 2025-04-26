# print("Hello from lesson 15")
i = 0
pisatopping = [
"mushrooms", 
"pepperoni",
"cheese"
]
userinput = []
while True:
    for item in pisatopping:
        userinput.append = int(input("Wut topping u want " + ([i + 1] + pisatopping[i] )))
        if userinput == "end":
            break
        else:
            userinput.append(pisatopping[int(userinput) - 1])
print( )