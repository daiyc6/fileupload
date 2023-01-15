n = 7
a = [[10, 4], [15, 7], [18, 6], [31, 12], [35, 16], [36, 10], [42, 9]]
b = []
oil = 23
home = 50

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
    oil=oil-dis
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
    for j in range(tail-2,head-1, -1):
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
