import turtle

t=turtle.Screen()
t.bgcolor("Black")

p=turtle.Turtle()
p.speed(200)

p.width(5)

p.color("Orange")
t=turtle.Screen()

for i in range(22):
    p.forward(1)
    p.right(1)
p.left(22)
p.forward(22.5)
for i in range(360):
    if (i<=180):
        p.forward(1)
        p.left(1)
    else:
        p.right(1)
        p.forward(1)
p.right(0)
p.forward(22.5)
for i in range(22):
    p.forward(1)
    p.right(1)

p.penup()
p.left(22)
p.forward(157.5)
p.right(22)
p.pendown()

for i in range(22):
    p.backward(1)
    p.left(1)
p.backward(22.5)
for i in range(180):
    if(i<90):
        p.backward(1)
        p.left(1)
    elif(i==90):
        p.backward(112.5)
    else:
        p.backward(1)
        p.left(1)
p.backward(22.5)
for i in range(22):
    p.left(1)
    p.backward(1)
p.left(68)
p.backward(67)
p.left(90)
p.backward(45)

turtle.done



