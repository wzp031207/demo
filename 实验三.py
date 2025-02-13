import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df=pd.read_csv('C:/Users/文/Desktop/机器学习实验素材/实验素材/实验素材/Customer_Info.csv')
# 提取特征
features=df[['age','deposit']]
# 实例化KMeans模型
kmeans=KMeans(n_clusters=4,random_state=0)
# 模型训练
kmeans.fit(features)
# 预测聚类结果
labels=kmeans.labels_
# 添加聚类结果到数据集
df['cluster']=labels
# 打印各类客户的特点画像
for i in range(4): # 假设有3个类别
    cluster_data=df[df['cluster']==i]
    # 统计每个类别的年龄和存款数量均值
    avg_age=cluster_data['age'].mean()
    avg_deposit=cluster_data['deposit'].mean()
    print(f'Cluster{i+1}:Average age={avg_age},Average deposit={avg_deposit}')
# 可视化分析
plt.scatter(df['deposit'],df['age'],c=df['cluster'])
plt.xlabel('Deposit')
plt.ylabel('Age')
plt.title('Customer Segmentation')
plt.show()
