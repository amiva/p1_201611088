import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
tracks=list()
def lab7():
	for i in range(0,4):
		tracks.append(t1.pos())
		t1.fd(50)
		t1.right(90)
		print tracks
def main():
	lab7()
if __name__=="__main__":
	main()	
wn.exitonclick()	