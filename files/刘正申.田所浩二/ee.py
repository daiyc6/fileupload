def convert(a):
    for i in range(len(a)):
        if a[i]==':':
            break
    t=a[i-2:i]
    return t
f=open('time.txt','r',encoding='UTF-8')
li=[]
for i in f.readlines():
    t=i.strip().split(',')
    li.append(t)
for i in li[1:]:
    a=int(i[1][0:2])*60+int(i[1][3:])
    b=int(i[2][0:2])*60+int(i[2][3:])
    i.append(b-a)
    

