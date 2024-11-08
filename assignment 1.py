import turtle

# screen setting
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("pink pig")
# pen
pen = turtle.Turtle()
pen.speed(3)  # 设置画笔速度

# head
pen.color("pink")
pen.penup()
pen.goto(-50, 0)
pen.pendown()
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# left ear
pen.penup()
pen.goto(-130, 150)
pen.pendown()
pen.color("light pink")
pen.begin_fill()
pen.circle(25)
pen.end_fill()
# right ear
pen.penup()
pen.goto(30, 150)
pen.pendown()
pen.color("light pink")
pen.begin_fill()
pen.circle(25)
pen.end_fill()

# left eye
pen.penup()
pen.goto(-80, 110)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(15)
pen.end_fill()
pen.penup()
pen.goto(-80, 110)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(7)
pen.end_fill()
# right eye
pen.penup()
pen.goto(0, 110)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(15)
pen.end_fill()
pen.penup()
pen.goto(0, 110)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(7)
pen.end_fill()

# nose
pen.penup()
pen.goto(-33, 50)
pen.pendown()
pen.color("palevioletred")
pen.begin_fill()
pen.circle(20)
pen.end_fill()
# nostril
pen.penup()
pen.goto(-40, 60)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(5)
pen.end_fill()
pen.penup()
pen.goto(-20, 60)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(5)
pen.end_fill()

# mouth
pen.penup()
pen.goto(-90, 50)
pen.pendown()
pen.pensize(3)
pen.color("black")
pen.setheading(-60)
pen.circle(50, 90)

# hide pen and show
pen.hideturtle()
turtle.done()