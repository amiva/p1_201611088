import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
tracks=list()
def drawSquareAtSave(size,pos):
	t1.penup()
	t1.goto(pos)
	t1.pendown()	
	for i in range(0,4):
		tracks.append(t1.pos())
		t1.fd(50)
		t1.right(90)
		print tracks
def lab7():
	drawSquareAtSave(100,(0,0))

def main():
	lab7()
if __name__=="__main__":
	main()	
wn.exitonclick()	