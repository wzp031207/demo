import pandas as pd
df=pd.read_excel('E:/edge下载/销售数据(1).xlsx')
df.fillna(method='ffill',inplace=True)
df['购买日期']=pd.to_datetime(df['购买日期'])
print(df)