def main():
	sum=0
	for i in range(1,1001):
		if(i%3==0 or i%5==0):
			sum=sum+i
	print sum
main()
import turtle
wn=turtle.Screen()
wn.exitonclick()



"""
diagram
@startuml

title 3과5의배수 더하기 


start

repeat
if(i is divided by 3 or 5)then(plus)
:sum=0;
:sum=sum+i;
else
:throw away;
endif

repeat while(1<i<=1000)
"""