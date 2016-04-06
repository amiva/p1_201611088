import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def lab6():
	year=raw_input("input year{2000~}: ")
	y1=int(year)
	if(y1%4==0):
		print "This year is leap year"
	else:
		print "This year is not leap year"
def main():
	lab6()
main()
t1.write("윤주석 과제끝!")
wn.exitonclick()

"""
Diagram

@startuml

title 윤년맞추기


start
:user input year;

if(year%4==0)and year(%100 !=0 or year%400==0) then (yes)

:print 윤년입니다;

else (no)

:print 윤년이 아닙니다;

endif


"""