from random import randint
a = [[chr(randint(65, 90))*3, randint(1, 100)]for i in range(10)]
b = [i for i in range(len(a))]

print('原始数据：')
for i in range(len(b)):
    print(a[b[i]])
print('\n')
print('索引数组数据：')


for i in range(len(b)):
    print(i,b[i])

    
for i in range(len(a)-1):
    k = i
    for j in range(i, len(a)):
        if a[b[k]][1] < a[b[j]][1]:
            k = j
    if k != i:
        b[k], b[i] = b[i], b[k]


print('排序后数据:')
for i in range(len(b)):
    print(a[b[i]])
print('\n')
print('before:')
for i in range(len(b)):
    print(a[i])
print('索引数组数据：')
for i in range(len(b)):
    print(i,b[i])
