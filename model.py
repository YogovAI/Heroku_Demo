import pandas as pd
import numpy as np
import pickle


df=pd.read_csv("E:\Projects\VSCODE_WORKSPACE\ML\Play_Tennis\play_tennis.csv")

df1=df.drop(['day', 'temp'], axis =1)

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()


df1['outlook']= label_encoder.fit_transform(df1['outlook'])
df1['humidity']= label_encoder.fit_transform(df1['humidity']) 
df1['wind']= label_encoder.fit_transform(df1['wind']) 
df1['play']= label_encoder.fit_transform(df1['play'])

x=df1[['outlook', 'humidity', 'wind']]

y=df1[['play']]


from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=101)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
# predictions = model.predict(x_test)
# predictions

pickle.dump(model, open('model.pkl','wb'))





