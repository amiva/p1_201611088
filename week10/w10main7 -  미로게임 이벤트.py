import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgpic("maze.GIF")


def m1():
	t1.fd(10)

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
def addMouse():
	wn.onclick(mousetogo)
addMouse()
wn.listen()
input()