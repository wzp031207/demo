from sklearn import linear_model
X=[[6,1],[9,3],[12,2],[14,3],[16,4]]
y=[[9],[12],[29],[35],[59]]
model=linear_model.LinearRegression()
model.fit(X,y)
w=model.coef_
b=model.intercept_
y_predict=model.predict([[10,3]])
print('投资一千万，推广三百万的电影预计票房收入为：',y_predict,'百万')
print('回归模型的系数是:',w)
print('回归模型的截距是:',b)


