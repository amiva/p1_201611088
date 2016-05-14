allData=[["Coffee","Water","Milk","Icecream"],
         ["Espresso","No","No","No"],
         ["Long Black","Yes","No","No"],
         ["Flat White","No","Yes","No"],
         ["Cappuccino","No","Yes - Frothy","No"],
         ["Affogato","No","No","Yes"]]
print allData
data=allData[1:]
datat=list()
for t in data:
	if t[2].upper()=='YES' or t[2].upper()=='YES - FROTHY':
		print t[0]
		datat.append(t[0])
print len(datat)
print len(data)
print float(len(datat))/float(len(data))*100,"%"
input()