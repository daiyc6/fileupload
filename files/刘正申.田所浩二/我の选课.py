import pandas as pd
a=pd.read_csv('zy.csv',encoding='gbk')
a=a.sort_values('得分'，ascending=False,ignore_index=True)
xk=[]
