import turtle
pen=turtle.Pen()
def walk_pen(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

#设置画布属性
turtle.screensize(400,300,'blue')

#设置画笔属性
pen.color('black','black')
pen.pensize(5)

#黑色部分
radius=200
pen.begin_fill()
pen.circle(radius / 2,180)#右上角的黑色半圆
pen.circle(radius,180)#左边黑色半圆
pen.left(180)
pen.circle(-radius / 2,180)#左下角与白色衔接的半圆轮廓
pen.end_fill()

#白色部分
pen.color('black','white')
walk_pen(0,0)
pen.begin_fill()
pen.circle(-radius / 2,-180)
pen.circle(-radius,-180)
pen.left(180)
pen.circle(radius / 2,-180)
pen.end_fill()

#小白圆
walk_pen(0,radius/3)

pen.begin_fill()
pen.circle(radius/6)
pen.end_fill()

pen.color('black','black')
#小黑圆
walk_pen(0,-2*radius/3)

pen.begin_fill()
pen.circle(radius/6)
pen.end_fill()
