import matplotlib.pyplot as plt

# 数据
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sales = [15, 12, 8, 20, 16, 22, 33, 18, 15, 9]

# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(months, sales, color='skyblue', edgecolor='black')

# 添加标题和坐标轴标签
plt.title('商品每月销量柱状图', fontsize=16,fontproperties='STSong')
plt.xlabel('月份', fontsize=14,fontproperties='STSong')
plt.ylabel('销量', fontsize=14,fontproperties='STSong')

# 设置x轴刻度
plt.xticks(months, fontsize=12,fontproperties='STSong')
plt.yticks(fontsize=12)

# 显示网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 调整布局并显示图表
plt.tight_layout()
plt.show()