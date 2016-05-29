import time
timeEdit=time.strftime('%Y-%m-%d %H:%M:%S')
editor='yjs'
edtied="[{0} edited {1}]".format(editor,timeEdit)
fin=open('output.txt','r')
fout=open('outputUpper.txt','w')
type(fin)
for line in fin:
    words=line.split()
    for word in words:
        if word=='line':
            word=word.upper()
            fout.write(word)
        elif not word=='line':
            fout.write(word)
    print "\n"        
    print line
fin.close()    
fout.close()    