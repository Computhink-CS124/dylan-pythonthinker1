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
        print(str(i + 1) + str(pisatopping[i]))
        i = i + 1
    usertop = int(input("Wut topping u want?????"))
    userinput.append = pisatopping[usertop - 1]
    if userinput == "end":
            break
    else:
            userinput.append(pisatopping[int(userinput) - 1])
print( )