import turtle
import math
wn=turtle.Screen()
t1=turtle.Turtle()
t1.penup()
t1.setpos(0,100)
t1.pendown()
t1.circle(50)
a=float()
b=float()
t1.penup()
t1.setpos(0,-100)
def m1():
	t1.fd(30)
	x=float()
	y=float()
	a=float()
	b=float()
	(a,b)=(0,150)
	(x,y)=t1.pos()
	if(math.sqrt(math.pow(a-x,2)+math.pow(b-y,2)))<=50:
		print "turtle get into score area"
		t1.write("들어감")
		t1.goto(0,-100) 
def m2():
	t1.back(10)
def m3():
	t1.right(90)
def m4():
	t1.left(90)
wn.onkey(m1,"Up")
wn.onkey(m2,"Down")
wn.onkey(m3,"Right")
wn.onkey(m4,"Left")
def mousetogo(x,y):
	t1.setpos(x,y)
	(x,y)=t1.pos()
	a=float()
	b=float()
	(a,b)=(0,150)
	if(math.sqrt(math.pow(a-x,2)+math.pow(b-y,2)))<=50:
		print "turtle get into score area"
		t1.write("들어감")
		t1.goto(0,-100) 
	
def addMouse():
	wn.onclick(mousetogo)
addMouse()
wn.listen()
input()