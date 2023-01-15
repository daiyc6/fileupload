'''
n = int(input('请输入加油站数量：'))
a = []  # a[i][0]存储第i个加油站里离起点距离，a[i][0]存储第i个加油站可加油量
for i in range(n):
    a.append(list(map(int, input().split())))
b = []  # b[i][0]存储加加油站的编号，b[i][1]存储该加油站的可加油量

oil = int(input("初始油量："))
home = int(input('家离起点距离：'))
#初始化加油信息
'''
n = 7
a = [[10, 4,0], [15, 7,1], [18, 6,2], [31, 12,3], [35, 16,4], [36, 10,5], [42, 9,6]]
f = [False]*(n+1)
b = []
oil = 23    # 起始油量
home = 50    # 终点距离
a.append([home,0,7])
n+=1
loc=0
while a[loc][1]!=0:
    flag=True
    o=oil
    tail=0
    sl=0
    while flag:
        o-=a[tail][0]
        if o<0:
            break
        tail+=1
    need=a[tail+1][0]-a[tail][0]
    ra=a[loc:tail+1]
    for j in range(len(ra)-1):
        max=j
        for g in range (j,len(ra)):
            if ra[j][1]<ra[g][1]:
                max=g
        ra[j],ra[max]=a[max],a[j]
    oilget=0
    print(ra)
    for j in range(len(ra)):
        oilget+=ra[j][1]
        sl+=1
        f[ra[j][2]]=True
        if need-oilget<=0:
            break
    oil+=oilget
    loc+=tail
# 输出加油站的信息：
print(f'最少的加油次数为：{sl}')
s = '此次加油站的编号为：'
for i in range(n-1):
    if f[i]:
        s += str(i)+f'{a[i]}'+'、'
print(s)
