import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
df=pd.read_csv('C:/Users/文/Desktop/机器学习实验素材/实验素材/实验素材/Customer_Info.csv')
X=df.iloc[:,[4,3]].values
sumDS=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(X)
    sumDS.append(kmeans.inertia_)
plt.plot(range(1,11),sumDS)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters K')
plt.ylabel('SSE')
plt.show()