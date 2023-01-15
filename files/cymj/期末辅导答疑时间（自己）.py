
f=open('time.txt','r',encoding='UTF-8')
tm=[]
for i in f.readlines()[1:]:
    t=i.strip().split(',')
    tm.append(t)
for i in range(len(tm)-1):
    if int(tm[i][1][0:2])>int(tm[i+1][1][0:2]):
        tm[i],tm[i+1]=tm[i+1],tm[i]
    elif int(tm[i][1][0:2])==int(tm[i+1][1][0:2]):
        if int(tm[i][1][3:5])>int(tm[i+1][1][3:5]):
            
            tm[i],tm[i+1]=tm[i+1],tm[i]
        
print(tm)
