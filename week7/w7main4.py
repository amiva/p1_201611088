import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def saveTracks():
	tracks=list()
	t1.penup()
	t1.goto(-400,300)
	t1.pendown()
	t1.pencolor("Red")
	t1.right(90)
	t1.fd(400)
	tracks.append(t1.pos())
	t1.backward(150)
	tracks.append(t1.pos())	
	t1.left(90)
	t1.fd(300)
	tracks.append(t1.pos())
	t1.left(90)
	t1.fd(300)
	tracks.append(t1.pos())
	t1.back(150)
	tracks.append(t1.pos())
	t1.right(90)
	t1.fd(300)
	tracks.append(t1.pos())
	t1.left(90)
	t1.right(90)
	t1.right(90)
	t1.fd(200)
	tracks.append(t1.pos())
	t1.fd(300)
	tracks.append(t1.pos())
	t1.back(100)
	tracks.append(t1.pos())
	t1.left(90)
	t1.fd(200)
	tracks.append(t1.pos())
	return tracks
Tracks=saveTracks()
def reset():
	t1.penup()
	t1.goto(-400,300)
	t1.pendown()
	t1.clear()
def replayTracks(Tracks):
	for t in Tracks:
		print t
	for i in range(0,len(Tracks)):	
		t1.goto(Tracks[i])

def lab7():
	reset()
	replayTracks(Tracks)	
def main():
	lab7()
if __name__=="__main__":
	main()
wn.exitonclick()