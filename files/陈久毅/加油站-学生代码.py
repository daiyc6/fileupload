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
a = [[10, 4], [15, 7], [18, 6], [31, 12], [35, 16], [36, 10], [42, 9]]
b = []
oil = 23    # 起始油量
home = 50    # 终点距离
'''
f = [False]*n
ans=0
while oil<home:
    i=0
    m=0
    while (not f[i]) and a[i][0]<=oil:
        if a[i][1]>=a[m][1]:
            m=i
        i+=1
    ans+=1
    f[m]=True
    oil+=a[m][1]
# 输出加油站的信息：
print(f'最少的加油次数为：{ans}')
s = '此次加油站的编号为：'
for i in range(n):
    if f[i]:
        s += str(i)+','
print(s)
