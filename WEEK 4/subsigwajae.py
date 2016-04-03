import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
temp = input("user input temperature: ")
sel = raw_input("F or C: ")
t3=int(temp)
if(sel=='F'):
    print ((t3-32) / 1.8), "C"
elif(sel=='C'):
    print (t3*1.8+32), "F"
else:
    print "Input Error"
t1.pencolor("Pink")
t1.write("완성")
wn.exitonclick()