import turtle
import time
wn=turtle.Screen()
wn.bgcolor("Pink")
t1=turtle.Turtle()
import turtle
g1=turtle.Turtle()
t1.penup()
g1.penup()
t1.goto(0,-200)
t1.pendown()
t1.write("시작점")
t1.penup()
t1.left(90)
g1.goto(-300,200)
g1.speed(50)
print "Press Q when you want to exit"
print "score >10 game end"
g1.pendown()
for i in range(0,4):
	g1.fd(100)
	g1.right(90)
g1.penup()
g1.goto(0,150)
g1.pendown()
for i in range(0,2):
	g1.fd(50)
	g1.right(90)
	g1.fd(100)
	g1.right(90)
g1.penup()
g1.goto(200,200)
g1.pendown()
for i in range(0,4):
	g1.fd(50)
	g1.right(90)
g1.pencolor("Blue")
g1.penup()
g1.goto(-250,150)
g1.pendown()
g1.write("2 score point")
g1.penup()
g1.goto(-275,175)
g1.pendown()
for i in range(0,4):
	g1.fd(50)
	g1.right(90)
g1.penup()
g1.goto(25,75)
g1.pendown()
g1.write("1 score point")
g1.penup()
g1.goto(15,130)
g1.pendown()
for i in range(0,2):
	g1.fd(20)
	g1.right(90)
	g1.fd(60)
	g1.right(90)
g1.penup()
g1.goto(225,175)
g1.pendown()
g1.write("3 score point")
g1.penup()
g1.goto(215,185)
g1.pendown()
for i in range(0,4):
	g1.fd(20)
	g1.right(90)
g1.color("Pink")
x=float()
y=float()
print "your starting score is 0"
score=0
def m1():
	global score
	(x,y)=t1.pos()
	t1.forward(20)
	if(-275<x<-225 and 125<y<175):
		score+=2
		print "your score is now %d !" % score
		t1.goto(0,-200)
	if(15<x<35 and 70<y<130):
		score+=1
		print "your score is now %d !" % score
		t1.goto(0,-200)
	
	if(215<x<235 and 165<y<185):
		score+=3
		print "your score is now %d !" % score
		t1.goto(0,-200)
	if(score>=10):
		print "Nice Playeeeeeeeeeeeeeeeeeeeee!!!"
		t1.goto(0,0)
		t1.write("Good job")
		print "Game will be ended after 10 sec"
		time.sleep(10)
		wn.bye()	
	
def m2():
	t1.left(45)
def m3():
	t1.right(45)
def m4():
	wn.bye()
def m5():
	t1.back(10)
wn.onkey(m1, "Up")
wn.onkey(m2, "Left")
wn.onkey(m3, "Right")
wn.onkey(m4, "q")
wn.onkey(m5, "Down")
wn.listen()
timeout=0
for i in range(timeout,0,-1):
	print timeout
	time.sleep(5)
	timeout-=5





wn.exitonclick()