from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
iris=load_iris( )
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2,random_state=22)
transfer=StandardScaler()
x_train=transfer.fit_transform(x_train)
x_test=transfer.fit_transform(x_test)
knn=KNeighborsClassifier(n_neighbors=1)
param_dict={'n_neighbors':[1,3,5]}
knn=GridSearchCV(knn,param_grid=param_dict,cv=10)
knn.fit(x_train,y_train)
y_pre=knn.predict(x_test)
accuracy=knn.score(x_test,y_test)
print(y_pre==y_test)
print(y_pre)
print(accuracy)
print(knn.best_estimator_)
print(knn.best_score_)
print(knn.cv_results_)
