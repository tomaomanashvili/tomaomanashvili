from turtle import *


#we want to paint a house

#step 1: draw a square
speed(10)
width(7)
color("green")
forward(200)
left(90)


forward(200)
left(90)
forward(200)
left(90)


forward(200)
left(90)
#end of square

#draving a door
forward(70)
color("blue")
begin_fill()
left(90)
forward(100) #hight of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill
penup()
goto(200, 200)
pendown()

color("gray")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#we want to paint windows
color("purple")
left(50)
penup()
forward(40)
left(70)
pendown()
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
penup()
right(90)
forward(120)
pendown()
right(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()



exitonclick()
