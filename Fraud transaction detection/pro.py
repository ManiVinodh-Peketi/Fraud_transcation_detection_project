import pandas as pd


df=pd.read_csv(r'fraudTrain.csv',encoding='utf-8-sig')

df.columns
df.index.name = 'index'

df['dob']=pd.to_datetime(df['dob'].astype(str), errors='coerce')
df['dob'] = pd.to_datetime(df['dob'], format = '%d/%m/%Y %H:%M:%S')

df['trans_date_trans_time']=pd.to_datetime(df['dob'].astype(str), errors='coerce')
df['trans_date_trans_time'] = pd.to_datetime(df['dob'], format = '%d/%m/%Y %H:%M:%S')

#df['New']=pd.to_datetime(df['New'],format='%d/%m/%Y %H:%M:%S')
#df['dob']=pd.to_datetime(df['dob'])

#df['unix_time']=pd.to_datetime(df['unix_time'])[11:]

column_new=df['dob']
column_ne=df['trans_date_trans_time']
#column_new=pd.to_datetime(column_new,format='%d/%m/%Y %H:%M:%S')
db=pd.DataFrame({'Year':column_new.dt.year,
                 'month':column_new.dt.month,
                 'day':column_new.dt.day,
                 'hour':column_new.dt.hour})
db1=pd.DataFrame({'Year1':column_ne.dt.year,
                 'month1':column_ne.dt.month,
                 'day1':column_ne.dt.day,
                 'hour1':column_ne.dt.hour})

df=df.drop(['trans_date_trans_time'],axis=1)
df=pd.concat([db,df,db1],axis=1)
df=df.drop_duplicates()
ds=df
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df.columns
df=df.drop(['first', 'last','street','city','state','dob','Unnamed: 0','hour'],axis=1)
l=['merchant', 'gender','category', 'job','trans_num']


for i in l:
    df[i]=le.fit_transform(df[i])
    
le.fit(l)
df.dropna()
x=df.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19]]
y=df.iloc[:,16]
#print(x)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

from sklearn.neighbors import _KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=515)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
#from sklearn import metrics
#print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

'''from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(criterion='entropy')
dt.fit(x_train,y_train)
y_pred_dt = dt.predict(x_test)'''
#from sklearn import metrics
#print("Accuracy:",metrics.accuracy_score(y_test, y_pred_dt))



'''df1=pd.read_csv('c:/users/Vinodh_wow/Downloads/fraudTest.csv',encoding='utf-8-sig')
df1['New']=pd.to_datetime(df1['trans_date_trans_time'],errors='coerce')
df1['New']=pd.to_datetime(df1['New'],format='%d/%m/%Y %H:%M:%S')
df1['dob']=pd.to_datetime(df1['dob'])
column_new1=df1.iloc[:,-1]
db1=pd.DataFrame({'Year':column_new1.dt.year,
                 'month':column_new1.dt.month,
                 'day':column_new1.dt.day,
                 'hour':column_new1.dt.hour,})
df1=df1.drop(['trans_date_trans_time'],axis=1)
df1=pd.concat([db1,df1],axis=1)

df1=df1.drop_duplicates()
df1=df1.drop(['first', 'last','New','street','city','state', 'Unnamed: 0',],axis=1)
lis=['merchant', 'category','dob', 'gender','zip', 'lat', 'long', 'city_pop', 'job','trans_num', 'unix_time', 'merch_lat', 'merch_long', 'is_fraud',]
le=LabelEncoder()
for i in lis:
    df1[i]=le.fit_transform(df1[i])
y1_pred_dt = dt.predict(df1)
print(y1_pred_dt)
'''
import pickle
pickle.dump(knn,open(r"ohno.plk",'wb'))
