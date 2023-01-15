import pandas as pd
df1=pd.read_csv(r"zy.csv",encoding='gbk')
df1.sort_values('得分',ascending=False)
n=len(df1.index)
a=[0]*n
for i in range(n):
    t=3
    k=df1['序号'][i]
    while a[k]==0:
        m=df1.iloc[i,t]
        if a.count(m)<30:
            a[k]=m
        else:
            t+=1
xh=input("请输入")
if int(xh) in df1.学号.values:
    x=int(xh)-2210001
    print('被录取',a[x])
