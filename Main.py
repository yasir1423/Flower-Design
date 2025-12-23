from turtle import *
speed(1)
bgcolor("black")
pencolor("aqua")
pendown()
def petal(color):
    pencolor(color)
    fillcolor(color)
    begin_fill()
    circle(100,60)
    left(120)
    circle(100,60)
    left(120)
    end_fill()
colors=["red","yellow","pink","orange","purple","blue"]
for i in range(12):
    petal(colors[i%len(colors)])
    left(30)
#Circle in the middle
penup()
goto(0,-20)
pendown()
color("white")
begin_fill()
circle(20)
end_fill()
hideturtle()
mainloop()
    
