import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data=pd.read_csv("C:/Users/文/Desktop/KaggleCredit2.csv",index_col=0)
data.dropna(inplace=True)

x=data.iloc[:,1:]
ss=StandardScaler()
xx=ss.fit_transform(x)

x_data=pd.DataFrame(xx,columns=data.columns[1:])
y=data['SeriousDlqin2yrs']

X_train,X_test,y_train,y_test=train_test_split(x_data,y,test_size=0.3,random_state=0)

from sklearn.svm import SVC
svm=SVC()
svm.fit(X_train[['NumberOfTime60-89DaysPastDueNotWorse']],y_train)

y_pred_svm=svm.predict(X_test[['NumberOfTime60-89DaysPastDueNotWorse']])
print('预测结果:\n',y_pred_svm)

svm.score(X_test[['NumberOfTime60-89DaysPastDueNotWorse']],y_test)