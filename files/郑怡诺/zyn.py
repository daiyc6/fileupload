f=open('time.txt',encoding='utf-8')
a=[]
for i in f.readlines()[1:]:
    t=i.strip().split(',')
    a.append([int(t[1][0:2])*60+int(t[1][3:]),int(t[2][0:2])*60+int(t[2][3:])])
def f(a1,a2):
    if a1[0]<a2[0]:
        if a1[1]>a2[1]:
            return 1
        else:
            return 0
    
        

