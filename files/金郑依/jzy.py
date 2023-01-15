import pandas as pd
df1=pandas.read_csv('zy.csv',encoding='gbk')
df2=df1.sort_values('得分',ascending=False)
n=len(df1.index)
a=[0]*n
for i in  range(n):
    t=3
    k=df2['序号'][i]
    while a[k]==0:
        m=df2.iloc[i,t]
        if a.count(m)<30:
            a[k]=m
        else:
            t+=1
