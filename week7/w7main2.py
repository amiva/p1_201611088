import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
c=dict()
c=({0:(0,0),1:(100,0),2:(100,100),3:(0,100),4:(0,0)})
for i in range(1,5):
	t1.goto(c[i])
for j in range(1,5):
	print c[j]
wn.exitonclick()