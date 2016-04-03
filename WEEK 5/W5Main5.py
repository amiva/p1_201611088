import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
score=raw_input("Input your score you got 0~60: ")
s1=float(score)
def Convertyourgrade(score):
    if(s1<=10):
        grade= "F"
        t1.write("분발해")
    elif(10<s1<=20):           
        grade= "D"
        t1.write("좀더 노력하세요")
    elif(20<s1<=30):    
        grade= "C"
        t1.write("아까웠어요")
    elif(30<s1<=40):    
        grade= "B"
        t1.write("잘하시네요")
    elif(40<s1<=50):    
        grade= "A"
        t1.write("너 잘해")
    elif(40<s1<=60):
        grade= "A+"
        t1.write("너 과탑")
    else:
        grade= "Input Error"
        t1.write("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
    return grade
result=Convertyourgrade(score)
print "your grade is %s " % result
t1.fd(200)
t1.pencolor("PINK")
t1.write("완성")
wn.exitonclick()
