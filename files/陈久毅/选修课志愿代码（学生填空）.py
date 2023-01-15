import pandas as pd
# 读取zy.csv文件内的数据，并保存
data = []
f = open('zy.csv', encoding='gbk')
n = 0
for s in f.readlines()[1:]:
    a = list(map(int,s.strip().split(',')))# 使用map对整行的数据进行整数转换，map（int，列表对象），其含义就是使用int函数处理列表对象。
    a[1] =str(a[1])# 将学号转换为字符串
    data.append(a)
    n += 1

# 对数据进行降序排序，借用idx数组记录排序前后的顺序情况。
idx = [i for i in range(n)] # 记录排序后的的新序号
for i in range(n-1):
    k = i
    for j in range(i+1, n):
        if data[idx[k]][2] < data[idx[j]][2]:
            k = j
    if  k!=i:
        idx[k], idx[i] =idx[i],idx[k]# 改错

# 确定每位学生的志愿
b = [0]*10  # b用来记录选修课的已选课人数
for i in range(n):
    for j in data[i][3:13]:
        if b[j-1] < 30:
            b[j-1] += 1
            data[i].append(j)
            break
# 查找指定学号的选修课志愿录取情况

key = input('请输入学号查询录取情况：')
left, right = 0, n-1
flag =False
while left<=right:# 循环查找的条件
    m =(left+right)//2#中间值
    if key==data[m][1]:
        print(f'{key}已被{data[m][-1]}号选修课录取')
        flag = True
        break
    elif data[m][1]<key:
        left = m+1
    else:
        right = m-1
if not flag:
    print(f'找不到学号{key}，请确认学号是否有误！')
