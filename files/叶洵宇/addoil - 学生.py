n = int(input('请输入加油站数量：'))
a = []  # a[i][0]存储第i个加油站里离起点距离，a[i][0]存储第i个加油站可加油量
for i in range(n):
    a.append(list(map(int,input().split())))
b = []  # b[i][0]存储加加油站的编号，b[i][1]存储该加油站的可加油量

oil = int(input("初始油量："))
home = int(input('家离起点距离：'))

n += 1
a.append([home, 0])
f = [False]*n
head = tail = 0
ans = 0

for i in range(n):    # 计算开到下一站的距离，并扣除油量
    if i == 0:
        dis = a[i][0]
    else:
        dis = a[i][0]-a[i-1][0]
    oil =oil-dis
# 开不到下一个站点，在前面还没有加油的站点加油
    while oil < 0 and head < tail:
        oil = oil+b[head][1]
        f[b[head][0]] = True
        head += 1
        ans += 1
    if oil < 0:
        print('回不了家了')
        break
	# 添加编号为i的加油站，并在还没有加油的站点中按加油量降序排序
    b.append([i, a[i][1]])
    tail += 1
    for j in range(tail-2,head-1,-1):
        if b[j][1] < b[j+1][1]:
            b[j], b[j+1] = b[j+1], b[j]
        else:
            break
else:
    print('最少的加油次数：', ans)
    s = ""
    for i in range(n):
        if f[i]:
            s = s+str(i)+','
    print('以此加油站的编号：',s)
