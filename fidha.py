from turtle import*

speed(0)

# Blue Background
penup()
goto(0,-250)
pendown()
color("lightskyblue")
begin_fill()
circle(250)
end_fill()

# Tree Trunk
penup()
goto(-15,-50)
pendown()
color("brown")
begin_fill()
for i in range(2):
    forward(30)
    right(90)
    forward(40)
    right(90)
end_fill()

#set the start position and the initial tree width
y=-50
width = 240
height = 25

#Green section of tree
while width > 20:
    width=width-30# Make the tree get smaller as it goes up in height
    x=0-width/2# Set the starting x-value of each level of the tree
    color("green")
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

    y=y+ height# keep drawing the levels of the tree higher than the previous

#star
penup()
goto(-15,150)
pendown()
color("yellow")
begin_fill()
for i in range(5):
    forward(30)
    right(144)
end_fill()

#Message
penup()
goto(-210,-150)
color("red")
write("MERRY CHRISTMAS AND HAPPY NEW YEAR",font=("Arial",15,"bold"))

penup()
goto(-90,-170)
color("red")
write("-FIDHA ZAINAB FAIZAL",font=("Arial",15,"bold"))

#ORNAMENTS
penup()
goto(-95,0)
pendown()
color("BLUE")
begin_fill()
circle(10)
end_fill()

penup()
goto(95,0)
pendown()
color("RED")
begin_fill()
circle(10)
end_fill()

penup()
goto(68,48)
pendown()
color("GREEN")
begin_fill()
circle(10)
end_fill()

penup()
goto(-68,48)
pendown()
color("YELLOW")
begin_fill()
circle(10)
end_fill()

penup()
goto(40,95)
pendown()
color("PINK")
begin_fill()
circle(10)
end_fill()

penup()
goto(-40,95)
pendown()
color("WHITE")
begin_fill()
circle(10)
end_fill()

hideturtle()

