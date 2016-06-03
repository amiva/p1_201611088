
import turtle
import time
import math
wn=turtle.Screen()
wn.bgcolor("Pink")
t1=turtle.Turtle()
import turtle
g1=turtle.Turtle()
class mainTurtle(turtle.Turtle):
	def posss(self):
		x=float()
		y=float()
		(x,y)=self.pos()
class dodgeTurtle(turtle.Turtle):
	def dodgePlz(self,hardgrade2):
		a=float()
		b=float()
		global aaa
		aaa=0
		self.speed(2)
		k=10
		while k:
			self.fd(600)
			self.backward(600)
			aaa+=1
			print "time is elapsed",aaa
		(a,b)=self.pos()
g2=dodgeTurtle()

k1=raw_input("what mode do you want? hard or easy? plz answer only hard or easy  : ")
if(k1=='hard'):
	print "then choose hardgrade1 and 2"
	print " if you touch obstacle it will make you lose 2 score"
	print " 2 will be a range of obstacle if you touch it it will be game over"
	hardgrade2=input("hardgrade 30 or 40: ")
	print "please push the z button in your keyboard to activate hard game"
elif(k1=='easy'):
	print "have fun"
	g2.color("Pink")
else:
	print "input error"
	wn.bye()

g2.penup()
g2.goto(-300,0)
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
g1.pencolor("Blue")
g1.write("score point!")
g1.penup()
g1.goto(0,100)
g1.pendown()
g1.circle(50)
g1.pencolor("Black")
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
count=float()
count=0
def m1():
	global score
	global count
	(x,y)=t1.pos()
	t1.forward(20)
	if(-275<x<-225 and 125<y<175):
		score+=2
		print "your score is now %d !" % score
		t1.setpos(0,-200)
	q=float()
	w=float()
	e=float()
	r=float()
	(e,r)=(0,150)
	(q,w)=t1.pos()
	if(math.sqrt(math.pow(e-q,2)+math.pow(r-w,2)))<=50:
		score+=1
		print "your score is now {0} !".format(score)
		t1.setpos(0,-200)
	if(215<x<235 and 165<y<185):
		score+=3
		print "your score is now %d !" % score
		t1.setpos(0,-200)
	if(score>=10):
		print "Nice Playeeeeeeeeeeeeeeeeeeeee!!!"
		t1.setpos(0,0)
		t1.write("Good job")
		k2=500+score-aaa-(count/2)+hardgrade2
		print "your final score is {0} it is good when your score is high".format(k2)
		print "Game will be ended after 10 sec"
		time.sleep(10)
		wn.bye()
	a1=float()
	b1=float()
	(a1,b1)=g2.pos()
	if(math.sqrt(math.pow(a1-x,2)+math.pow(b1-y,2)))<=hardgrade2:
		score-=2
		t1.setpos(0,-200)
		print "your score is now {0} !".format(score)
	count+=1
def m11():
	global score
	global count
	(x,y)=t1.pos()
	t1.forward(20)
	if(-275<x<-225 and 125<y<175):
		score+=2
		print "your score is now %d !" % score
		t1.setpos(0,-200)
	count+=2
	q=float()
	w=float()
	e=float()
	r=float()
	(e,r)=(0,150)
	(q,w)=t1.pos()
	if(math.sqrt(math.pow(e-q,2)+math.pow(r-w,2)))<=50:
		score+=1
		print "your score is now {0} !".format(score)
		t1.setpos(0,-200)
	if(215<x<235 and 165<y<185):
		score+=3
		print "your score is now %d !" % score
		t1.setpos(0,-200)
	if(score>=10):
		print "TY for playing!!!"
		k3=400-(count/2)+score
		print "your final score is {0}".format(k3)
		t1.setpos(0,0)
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
def m6():
	t1.back(20)
def m5():
	g2.dodgePlz(hardgrade2)
	
	
if(k1=='easy'):
	wn.onkey(m11, "Up")
elif(k1=='hard'):
	wn.onkey(m1, "Up")
wn.onkey(m2, "Left")
wn.onkey(m3, "Right")
wn.onkey(m4, "q")
wn.onkey(m6, "Down")
wn.onkey(m5, "z")

wn.listen()





wn.exitonclick()