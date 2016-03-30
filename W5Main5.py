import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def Convertyourgrade():
    score=raw_input("Input your score you got 0~60: ")
    s1=float(score)    
    if(s1<=10):
        print "F"
        t1.write("분발해")
    elif(10<s1<=20):           
        print "D"
        t1.write("좀더 노력하세요")
    elif(20<s1<=30):    
        print "C"
        t1.write("아까웠어요")
    elif(30<s1<=40):    
        print "B"
        t1.write("잘하시네요")
    elif(40<s1<=50):    
        print "A"
        t1.write("너 잘해")
    elif(40<s1<=60):
        print "A+"
        t1.write("너 과탑")
    else:
        print "Input Error"
        t1.write("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
Convertyourgrade()
wn.exitonclick()
