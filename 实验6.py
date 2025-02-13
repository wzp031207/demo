import pandas as pd
from numpy import linalg as la
from sklearn.preprocessing import MinMaxScaler
def ecludSim(inA,inB):
    return 1.0/(1.0+la.norm(inA-inB))
data=pd.read_csv('C:/Users/文/Desktop/UserInfo.csv',sep=',',encoding='gbk')
data=data.fillna(method='ffill',axis=1).values
scaler =MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(data)
similarity=[]
for i in range(dataset.shape[0]):
    vec1=dataset[i-1]
    corr=[]
    for j in range(dataset.shape[0]):
        vec2=dataset[j-1]
        corr.append(ecludSim(vec1,vec2))
    similarity.append(corr)
similarity=pd.DataFrame(similarity)
similarity
label = pd.read_csv('C:/Users/文/Desktop/userFavorit.csv', header=None).values.tolist()
recmdStr=''
for m in range(similarity.shape[0]):
    a='为用户'+str(m+1)+'推荐:'
    simMax=0
    for n in range(similarity.shape[1]):
        if similarity[m][n]>simMax and similarity[m][n]<1:
            simMax=similarity[m][n]
            recmd=label[n]
        else:
            continue
    a=a+str(recmd)+"\n"
    recmdStr+=a
print(recmdStr)
