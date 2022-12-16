#Himawan Prayogo (HP)
#71220852 (852)
#H852P

import turtle

t = turtle.Turtle()
z = turtle.Turtle()
t.penup()
z.penup()
t.goto(-300,0)
z.goto(-300,0)
t.pendown()
z.pendown()

#huruf H

t.forward(50)
t.left(90)
t.forward(80)
t.right(90)
t.forward(50)
t.right(90)
t.forward(80)
t.left(90)
t.forward(50)

z.left(90)
z.forward(200)
z.right(90)
z.forward(50)
z.right(90)
z.forward(80)
z.left(90)
z.forward(50)
z.left(90)
z.forward(80)
z.right(90)
z.forward(50)
z.right(90)
z.forward(200)
z.left(90)

#jarak
t.penup()
z.penup()

t.forward(90)
z.forward(90)

t.pendown()
z.pendown()

#angka 8
t.circle(50)
t.left(90)
t.penup()
t.forward(12.5)
t.circle(15)
t.forward(12.5)
t.right(90)
t.pendown()
t.circle(25)
t.penup()
t.right(90)
t.forward(25)
t.pendown()
t.left(90)

z.penup()
z.left(90)
z.forward(100)
z.right(90)
z.pendown()

z.circle(50)
z.left(90)
z.penup()
z.forward(12.5)
z.circle(15)

z.forward(12.5)
z.right(90)
z.pendown()
z.circle(25)

z.penup()
z.right(90)
z.forward(125)
z.left(90)
z.pendown()

#jarak
t.penup()
z.penup()

t.forward(90)
z.forward(90)

t.pendown()
z.pendown()

#angka 5
t.pensize(7)
z.pensize(7)

t.circle(80,180)
t.setheading(90)
t.forward(100)
t.setheading(180)
t.forward(-100)

#angka2

t.pensize(1)
t.color("black")
t.penup()
t.goto(200,-40)
t.pendown()
t.setheading(-180)
t.forward(100)
t.right(120)
t.forward(100)
t.circle(30,180)

#angka2

t.pensize(7)
t.color("black")
t.penup()
t.goto(200,-40)
t.pendown()
t.setheading(-180)
t.forward(100)
t.right(120)
t.forward(100)
t.circle(30,180)

#jarak
t.penup()
t.setheading(180)
t.right(180)
t.forward(150)
t.pendown()


#hurufp
t.pensize(7)
t.right(90)
t.forward(150)
t.setheading(90)
t.forward(150)
t.right(90)
t.circle(-30,180)



t.hideturtle()
z.hideturtle()
