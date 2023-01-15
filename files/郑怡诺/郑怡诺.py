import pandas as pd
df1=pd.read_csv('zy.csv',encoding='gbk')
df2=df1.sort_values('得分',ascending=False)
n=len(df1.index)
a=[0]*n
for i in range(n):
    t=3
    k=df2['序号'][i]
    while a[k]==0:
        m=df2.iloc[i,t]
        if a.count(m)<30:
            a[k]=m
        else:
            t+=1
xh=input('请输入学号查询录取情况')
if int(xh) in df2.学号.values:
    x=int(xh)-2210001
    print(xh,'已被第',a[x],'号选修课录取')
else:
    print('找不到学号',xh,'请确认学号是否有误！')
