# print("Hello from lesson 16")
import turtle
window=turtle.Screen()
t=turtle.Turtle()

def drawshape (length, numsides):
    for i in range(numsides):
        t.forward(length)
        t.left(360 / numsides)
lengthvar = int(input("length? "))
drawshape(lengthvar, 4)







window.mainloop()