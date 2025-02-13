import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel表格
file1 = 'E:/edge下载/hfda_ch07_new_probs(1).xls'
data1 = pd.read_excel(file1, engine='xlrd')

# 使用列名进行计算
# 计算 P(E) 和修正后的 P(S1|E)
data1['P(E)'] = (data1['P(E|S1)'] * data1['P(S1)']) + (data1['P(E|~S1)'] * data1['P(~S1)'])
data1['P(S1|E)'] = (data1['P(E|S1)'] * data1['P(S1)']) / data1['P(E)']

# 绘制修正后的散点图
plt.figure(figsize=(10, 6))
plt.scatter(data1['Analyst'], data1['P(S1|E)'], color='red')
plt.title('P(S1|E) vs Analyst')
plt.xlabel('Analyst')
plt.ylabel('P(S1|E)')
plt.show()