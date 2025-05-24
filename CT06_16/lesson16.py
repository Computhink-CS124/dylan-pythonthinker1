# print("Hello from lesson 16")
import turtle
window=turtle.Screen()
t=turtle.Turtle()

def drawshape (length, numsides):
    for i in range(numsides):
        t.forward(length)
        t.left(360 / numsides)

drawshape(1, 360)







window.mainloop()