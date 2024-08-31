import turtle

turtleScreen = turtle.Screen()
turtleScreen.bgcolor("light green")
turtleScreen.title("Turtle Python")

turtleInstance = turtle.Turtle()
turtleInstance.color("blue") # çizim rengini belirledik.

def shrinkingsquare(size):
    for i in range(4):
        turtleInstance.forward(size)
        turtleInstance.left(90)
        size = size - 5

shrinkingsquare(150)
shrinkingsquare(130)
shrinkingsquare(110)
shrinkingsquare(90)
shrinkingsquare(70)
shrinkingsquare(50)
shrinkingsquare(30)
shrinkingsquare(10)

turtle.done()