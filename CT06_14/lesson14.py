# ##############################################################################################################################################################################################################print("Hello from lesson 15")
# i = 0
# pisatopping = [
# "mushrooms", 
# "pepperoni",
# "cheese"
# ]
# userinput = []

# for item in pisatopping:
#     print(str(i + 1) + str(pisatopping[i]))
#     i = i + 1

# while True:
    
#     usertop = (input("Wut topping u want?????"))
#     # userinput.append = pisatopping[usertop - 1]
#     if userinput == "end":
#         break
#     else:
#         userinput.append(pisatopping[int(i) - 1])

# for item in userinput:
#     print(item)
# print(userinput)






import turtle
window = turtle.Screen()
window.setup(width = 600, height = 400)

t= turtle.Turtle()

t.shape("turtle")
t.fillcolor("orange")
t.seth(90)
t.down
for i in range(360):
    t.forward(1)
    t.right(1)

for i in range(4):
    t.forward(180)
    t.right(90)

for i in range(3):
    t.forward(180)
    t.right(120)

for i in range(5):
    t.forward(30)
    t.right(72)

t.forward(180)
for i in range(6):
    t.forward(180)
    t.right(60)









window.mainloop()