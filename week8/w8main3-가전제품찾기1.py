myhome=list()
friendhome=list()
myhome=['tv','phone','camera','fridger','mixer','audio','cdplayer','light','computer','notebook','recorder']
friendhome=['coffeemachine','radio','camera','runningmachine','ramp','computer','notebook','recorder']
print myhome
print friendhome
k=friendhome
k1=set(myhome)&set(friendhome)
k2=myhome
x1=list()
x2=list()
print k1
for c in friendhome:
    if c in k and c not in k1:
        x1.append(c)
print "the thing that is not in your home and that is in your friendhome is" , x1 
for t in myhome:
    if t in k2 and t not in k1:
	x2.append(t)
print "the thing that is not in your friendhome and that is in your home is" , x2
input()