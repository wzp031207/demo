import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
# 读取数据集
file_path = 'C:/Users/文/Desktop/testSet.txt'
data = np.loadtxt(file_path)
# 使用肘部方法来确定最优的簇数
wcss = []
silhouette_scores = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)
    if i > 1:
        silhouette_scores.append(metrics.silhouette_score(data, kmeans.labels_))
# 绘制肘部折线图
plt.figure(figsize=(12, 6))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('肘部方法', fontproperties='STSong')
plt.xlabel('簇数', fontproperties='STSong')
plt.ylabel('簇内误差平方和（WCSS）', fontproperties='STSong')
plt.show()
# 根据轮廓分数确定最佳簇数
optimal_clusters = np.argmax(silhouette_scores)+2
# 使用最优簇数进行K-Means聚类
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(data)
# 绘制聚类结果图
plt.figure(figsize=(12, 6))
plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='black', label='中心点', alpha=0.5)
plt.title('聚类结果图', fontproperties='STSong')
plt.xlabel('特征1', fontproperties='STSong')
plt.ylabel('特征2', fontproperties='STSong')
plt.legend(prop={'family': 'STSong', 'size': 12})
plt.show()
