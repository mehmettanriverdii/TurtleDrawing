import turtle

drawingBoard = turtle.Screen()
drawingBoard.bgcolor("light blue")
drawingBoard.title("Python Turtle")

'''
turtleInstance = turtle.Turtle() # kaplumbağa oluşturduk.
turtleInstance.forward(100) # 100 piksel ileri gitmesini sağladık.

turtleInstance2 = turtle.Turtle() # 2. kaplumbağa'ı oluşturduk.
turtleInstance2.left(45) # sola 45 derece dönsün dedik.
turtleInstance2.forward(100) # 45 derecelik açı ile 100 piksel ileri git dedik.
'''

#square
square = turtle.Turtle()
"""
square.forward(100)
square.right(90)
square.forward(100)
square.right(90)
square.forward(100)
square.right(90)
square.forward(100)
"""
# kod tekrarını kaldırmak için while dıngusu kullandım.
'''
i = 0
while i < 4:
    i +=1
    square.forward(100)
    square.right(90)
'''


#star
'''
star = turtle.Turtle()
for i in range(5):
    star.right(144)
    star.forward(100)
'''

#polygon(star)
turtleInstance = turtle.Turtle()
numSides = 5
angle = 360 / numSides * 2
sideLenght = 100
for i in range(numSides):
    turtleInstance.right(angle)
    turtleInstance.forward(sideLenght)

turtle.done() # ekranın açık kalmasını sağladık.
