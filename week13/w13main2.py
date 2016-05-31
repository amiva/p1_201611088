import time
def homework():
    filetwo=open('output.txt', 'w')
    line1='first line\n'
    filetwo.write(line1)
    line2='second line\n'
    filetwo.write(line2)
    line3='third line'
    filetwo.write(line3)
    filetwo.close()
    msg='[Yjs edited {0}]'.format(time.strftime('%Y.%m.%d , %H:%M:%S'))
    fin=open('output.txt', 'r')
    fout=open('outputUpper.txt','w')
    for line in fin:
        words=line.split()
        fout.write(msg)
        fout.write('\t')
        for word in words:
            if word == 'line':
                fout.write('\t')    
                word=word.upper()
            fout.write(word)
        fout.write('\n')
    fin.close()
    fout.close()