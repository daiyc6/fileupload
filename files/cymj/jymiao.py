n=int(input('请输入加油站数量：'))
a=[]
for i in range(n):
        a.append(list(map(int,input().split())))
b=[]

oil=int(input('初始油量：'))
home=int(input('家离起始点距离：'))

n+=1
a.append([home,0])
f=[False]*n

ans=0
x=0

while x+oil<home:
        c=0
        maxx=0

        for i in range(n-1):
                if x<a[i][0]<=x+oil and a[i][1]>=maxx:
                        maxx=a[i][1]
                        c=i

        oil-=(a[c][0]-x)
        oil+=a[c][1]
        x=a[c][0]
        b.append([c,a[c][1]])
        f[c]=True
        ans+=1
        
print('最少的加油次数：',ans)
s=""
for i in range(n):
        if f[i]:
                s=s+str(i)+','
print('以此加油站的编号：',s)
        
        
