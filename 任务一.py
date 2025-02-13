import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel表格
file1 = 'E:/edge下载/hfda_ch07_new_probs(1).xls'
file2 = 'E:/edge下载/hfda_ch07_data_transposed(1).xls'
data1 = pd.read_excel(file2, engine='xlrd')

# 创建第二个文件的数据框
data2_columns = ["Analyst"] + [str(i) for i in range(1, 21)]
data2_values = [
    ["Statement1", 0.87, 0.88, 0.89, 0.91, 0.91, 0.92, 0.87, 0.92, 0.88, 0.92, 0.88, 0.89, 0.92, 0.88, 0.89, 0.90, 0.92, 0.91, 0.89, 0.91],
    ["Statement2", 0.68, 0.40, 0.47, 0.88, 0.37, 0.60, 0.47, 0.46, 0.59, 0.23, 0.34, 0.78, 0.70, 0.80, 0.54, 0.67, 0.74, 0.21, 0.21, 0.36],
    ["Statement3", 0.37, 0.11, 0.67, 0.07, 0.08, 0.30, 0.66, 0.41, 0.83, 0.09, 0.00, 0.46, 0.45, 0.35, 0.15, 0.63, 0.14, 0.22, 0.42, 0.87],
    ["Statement4", 0.39, 0.56, 0.33, 0.38, 0.19, 0.19, 0.27, 0.33, 0.14, 0.30, 0.58, 0.28, 0.33, 0.35, 0.16, 0.19, 0.33, 0.40, 0.28, 0.27],
    ["Statement5", 0.05, 0.28, 0.00, 0.24, 0.00, 0.18, 0.05, 0.03, 0.12, 0.09, 0.02, 0.05, 0.01, 0.13, 0.05, 0.03, 0.00, 0.07, 0.06, 0.05],
    ["Statement6", 0.77, 0.81, 0.85, 0.78, 0.72, 0.84, 0.88, 0.69, 0.74, 0.91, 0.92, 0.70, 0.03, 0.81, 0.87, 0.70, 0.79, 0.89, 0.81, 0.84],
]

data2 = pd.DataFrame(data2_values, columns=data2_columns)

# 计算标准差
std_dev_data1 = data1.std(numeric_only=True)
std_dev_data2 = data2.drop(columns=["Analyst"]).astype(float).std(axis=1)

print("Standard Deviation of Data1:\n", std_dev_data1)
print("Standard Deviation of Data2:\n", std_dev_data2)

# 绘制第一个数据表的散点图
fig, ax = plt.subplots(1, 2, figsize=(15, 6))

# "P(S1)" 与 "Analyst"
# 使用数字列名进行绘图
ax[0].scatter(data1['Analyst'], data1[1], color='blue')
ax[0].set_title('P(S1) vs Analyst')
ax[0].set_xlabel('Analyst')
ax[0].set_ylabel('P(S1)')

# "P(E|S1)" 与 "Analyst"
ax[1].scatter(data1['Analyst'], data1[2], color='green')
ax[1].set_title('P(E|S1) vs Analyst')
ax[1].set_xlabel('Analyst')
ax[1].set_ylabel('P(E|S1)')

plt.show()

# 绘制第二个数据表的散点图
fig, ax = plt.subplots(2, 3, figsize=(18, 12))

# 逐行绘制
for i in range(6):
    row = data2.iloc[i, 1:].astype(float)
    ax[i//3, i%3].scatter(row.index, row.values)
    ax[i//3, i%3].set_title(f'{data2.iloc[i, 0]} Data Distribution')
    ax[i//3, i%3].set_xlabel('Index')
    ax[i//3, i%3].set_ylabel('Value')

plt.tight_layout()
plt.show()