# print("Hello from lesson 16")
import turtle
# window=turtle.Screen()
# t=turtle.Turtle()


def setup_screnn (screenWidth, screenHeight):
    window=turtle.Screen()
    window.setup (width = screenWidth, height = screenHeight)
    return window
screenHeight = 500
screenWidth = 300
screen = setup_screnn (screenWidth, screenHeight)





window.mainloop()