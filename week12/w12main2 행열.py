data=[1,2,3,4,5,6,7,8,9,10]
fout=open('outputNumber1.txt','w')
for i in data:
    if i%2==0:
        toPrint="{0}\t\n".format(i)
    else:
        toPrint="{0}\t".format(i)    
    print toPrint,
    fout.write(toPrint)
fout.close()
input("")
