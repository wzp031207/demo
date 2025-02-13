import pandas as pd
from matplotlib import pyplot as plt
file_path="E:/edge下载/BeijingPM20100101_20151231.csv"
df=pd.read_csv(file_path)
#数据预览
print(df.head(3))
print(df.info())
#将时间连接起来
period=pd.PeriodIndex(year=df["year"],month=df["month"],day=df["day"],hour=df["hour"],freq="H")
print(period)
df["datetime"] = period
print(df.head(10))
#把datetime设置为索引
df.set_index("datetime",inplace=True)
#进行降采样
df=df.resample("7D").mean()
#处理缺失数据,删除缺失数据
data=df["PM_US Post"].dropna()
#画图
_x=data.index
_y=data.values
plt.figure(figsize=(20,8),dpi = 80)
plt.plot(range(len(_x)),_y)
plt.xticks(range(0,len(_x),10),list(_x)[::10],rotation=45)
plt.show()
