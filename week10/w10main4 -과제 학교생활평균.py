print "this is data made in 2014"
datavs=[["studyingcontent",13.1],["studyingmethod",10.6],["freindship",27.1],["relationshipwithteacher",16.2],["schoolfacility",11.4],
       ["enviroment",12.2],["major",13.5],["schoollife",13.7]]
datas=[["studyingcontent",37.1],["studyingmethod",34.6],["freindship",40.0],["relationshipwithteacher",37.8],["schoolfacility",29.8],
       ["enviroment",26.5],["major",29.7],["schoollife",37.6]]
datads=[["studyingcontent",8.7],["studyingmethod",13.4],["freindship",2.9],["relationshipwithteacher",6.8],["schoolfacility",14.8],
       ["enviroment",14.9],["major",11.1],["schoollife",4.1]]
datavds=[["studyingcontent",1.5],["studyingmethod",1.9],["freindship",1.5],["relationshipwithteacher",0.8],["schoolfacility",4.9],
       ["enviroment",4.4],["major",2.4],["schoollife",1.2]]
sum1=0
sum2=0
sum3=0
sum4=0
for t in datavs:
    sum1=sum1+t[1]
 
print "the very satisfaction data's sum is %s"% sum1
for t in datas:
    sum2=sum2+t[1]
print "the satisfaction data's sum is %s"% sum2
for t in datads:
    sum3=sum3+t[1]
print "the disatisfaction data's sum is %s"% sum3
for t in datavds:
    sum4=sum4+t[1]
print "the very disatisfaction data's sum is %s"% sum4
k1=sum1+sum2
a1=len(datavs)+len(datas)
t1=float(k1)/float(a1)
print "the very and normal satisfaction's average is %s"% t1
k2=sum3+sum4
a2=len(datads)+len(datavds)
t2=float(k2)/float(a2)
print "the very and noraml dissatisfaction's average is %s"% t2