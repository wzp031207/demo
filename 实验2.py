import pandas as pd
from scipy import stats
df=pd.read_excel('E:/edge下载/销售数据(1).xlsx')
df.fillna(method='ffill',inplace=True)
df['购买日期']=pd.to_datetime(df['购买日期'])
category=df.groupby('商品类别')['消费金额'].agg(['sum','mean'])
category.rename(columns={'sum':'总销售额','mean':'平均销售额'},inplace=True)
zfb=df[df['支付方式']=='支付宝']['消费金额']
wx=df[df['支付方式']=='微信']['消费金额']
print(zfb)
print(wx)
t_statistic,p_value=stats.ttest_ind(zfb,wx)
print(f't-statistic:{t_statistic}')
print(f'p-value:{p_value}')
alpha=0.01
if p_value<alpha:
    print('支付宝和微信支付方式的平均消费金额存在显著差异')
else:
    print('支付宝和微信支付方式的平均消费金额不存在显著差异')