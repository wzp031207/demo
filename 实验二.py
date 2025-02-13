import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
df=pd.read_csv('C:/Users/文/Desktop/机器学习实验素材/实验素材/实验素材/fruit_data.txt',sep=r'[,\t]')
# 提取特征和标签
df.columns=['fruit_label','mass','width','height','color_score']
X=df[['mass','width','height','color_score']]
y=df['fruit_label']
# 将数据集分成训练集和测试集
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
# 实例化KNN模型
knn=KNeighborsClassifier(n_neighbors=5)
# 模型训练
knn.fit(X_train,y_train)
# 预测新样本的类别
new_fruit1=pd.DataFrame({'mass':[192],'width':[8.4],'height':[7.3],'color_score':[0.55]})
new_fruit2=pd.DataFrame({'mass':[200],'width':[7.3],'height':[10.5],'color_score':[0.72]})
predicted_label1=knn.predict(new_fruit1)
predicted_label2=knn.predict(new_fruit2)
print('Predicted label:',predicted_label1)
print('Predicted label:',predicted_label2)