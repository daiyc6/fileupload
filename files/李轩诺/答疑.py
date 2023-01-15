f=open('time.txt','r',encoding='UTF-8')
tm=[]
for i in f.readlines()[1:]:
    t=i.strip().split(',')
    tm.append(t)

    
