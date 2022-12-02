import turtle

def drawTree(card):
    
    card.pencolor("#001A00")
    card.pensize(5)
    card.fillcolor("#001A00")
    card.begin_fill()

    card.forward(100)
    card.left(150)
    card.forward(90)
    card.right(150)
    card.forward(60)
    card.left(150)
    card.forward(60)
    card.right(150)
    card.forward(40)
    card.left(150)
    card.forward(100)

    card.left(60)
    card.forward(100)
    card.left(150)
    card.forward(40)
    card.right(150)
    card.forward(60)
    card.left(150)
    card.forward(60)
    card.right(150)
    card.forward(90)
    card.left(150)
    card.forward(133)
    card.end_fill()

    card.color("#3D251E")
    card.pensize(1)
    card.begin_fill()
    card.right(90)
    card.forward(80)
    card.right(90)
    card.forward(40)
    card.right(90)
    card.forward(80)
    card.end_fill()

    x = 110
    y = -10
    for i in range(3):
        card.penup()
        card.color("red")
        card.goto(x,y)
        card.pendown()
        card.begin_fill()
        card.circle(10)
        card.end_fill()
        x -= 100
        y += 40
    
    x = 0
    y = 100
    for j in range(2):
        card.penup()
        card.color("#F4BC1C")
        card.goto(x,y)
        card.pendown()
        card.begin_fill()
        card.circle(10)
        card.end_fill()
        x -= 30
        y -= 50
    card.penup()

    
def mainCard():
    turtle.TurtleScreen._RUNNING=True
    card = turtle.Turtle()
    card.hideturtle()
    turtle.bgcolor("#E8FFFF")
    drawTree(card)
    message="Under the christmas tree"
    card.goto(-10,-180)
    card.color("Orange")
    card.pendown()
    card.write(message,move=False,align="center",font=("Arial",15,"bold"))
    turtle.exitonclick()
    
    




    
