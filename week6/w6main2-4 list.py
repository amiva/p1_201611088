k=list()
def sumList(k):
    	for i in range(0,1001):
		if(i%4==0 and i%5>0):
			k.append(i)
	sum=0
	for j in range(0,len(k)):
		sum=sum+k[j]
	return sum	
def main():
	print sumList(k)
main()

input("enter to end")
