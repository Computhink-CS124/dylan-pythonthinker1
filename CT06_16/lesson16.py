# print("Hello from lesson 16")
import turtle
# window=turtle.Screen()
t=turtle.Turtle()


def setup_screnn (screenWidth, screenHeight):
    window=turtle.Screen()
    window.setup (width = screenWidth, height = screenHeight)
    return window
screenHeight = 500
screenWidth = 300


def bigblueballs():
    ball=turtle.Turtle()
    ball.shape("circle")
    ball.color("blue")
    ball.penup
    return ball








def moveball(ball, dx, dy):
    ball.setx(ball.xcor( + dx))
    ball.sety(ball.ycor( + dy))
ball = bigblueballs()
screen = setup_screnn (screenWidth, screenHeight)
moveball(ball, dx, dy)





















screen.mainloop()