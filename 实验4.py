import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
data=pd.read_csv('C:/Users/文/Desktop/credit-overdue.csv')
X=data.iloc[:,0:2]
y=data['overdue']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42,stratify=y)
clf=LogisticRegression(random_state=0,solver='lbfgs',multi_class='multinomial').fit(X_train,y_train)
print('coef:\n',clf.coef_)
print('intercept:\n',clf.intercept_)
predict_y = clf.predict(X_test)
print('classfication report:n',metrics.classification_report (y_test,predict_y))