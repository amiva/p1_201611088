import random
selectNr=raw_input("input range number ex 1~N : ")
s2=int(selectNr)
r1=random.randrange(1,s2+1)
print "Number's range is 1~%f" % s2
def subtool():
	selectN=raw_input("input number you want: ")
	s1=int(selectN)
	global s1
def maintool():
	if(s1==r1):
		print "correct!"
	else:
		if(s1>r1):
			print "down"
			subtool()
			maintool()	
		elif(s1<r1):
			print "Up"
			subtool()
			maintool()
		else:
			print "WTF"
def lab6():
	subtool()
	maintool()
def main():
	lab6()

main()
raw_input()		
"""
Diagram
@startuml

title Up and Down
:user input range number(==rn);
:computer choose number in range;


start

while (r1=s1)  is (no)
if(s1>r1)
  :print down;
elseif(s1<r1)
  :print up;
else
  :print error;
endif
endwhile
stop



@enduml
"""
if __name__=="__main__":
	main()
	