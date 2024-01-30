#!/usr/bin/env python
# coding: utf-8


import seaborn as sns
import pandas as pd
import numpy as np


raw_data = sns.load_dataset('titanic')
raw_data


raw_data.info()


raw_data.isnull().sum() #isnull인지 확인


clean_data=raw_data.dropna(axis=1,thresh=500) #deck삭제할 작업 thresh - 500개 기준 , axis컴럼 1개삭제


clean_data.columns


mean_age=clean_data['age'].mean() #나이 빈값에 평균을 넣을 작업
print(mean_age)


#clean_data = clean_data['age'].fillna(mean_age) 이건 삭제된 컬럼을 clean_data에 저장
clean_data['age'].fillna(mean_age,inplace=True)


clean_data.head(10)


clean_data.drop(['embark_town','alive'], axis=1, inplace=True) #컴럼 삭제하기


clean_data.info()


clean_data['embarked'].fillna(method='ffill',inplace=True) #정착지 바꾸기 작업
clean_data['embarked'][825:830]


clean_data.isnull().sum()


clean_data.info()


clean_data['sex'].replace({'male':0 ,'female':1} , inplace=True)
clean_data.info()


print(clean_data['sex'].unique()) #unique는 가진것만 보여줌


print(clean_data['embarked'].unique())


from sklearn import preprocessing


label_encoder= preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder()


print(clean_data['embarked'].value_counts())


clean_data['embarked'] = label_encoder.fit_transform(clean_data['embarked'])
print(clean_data['embarked'].unique())


print(clean_data['embarked'].value_counts())


clean_data.info()


clean_data['adult_male']=clean_data['adult_male'].astype('int64')
clean_data.info()


clean_data.head()


target = clean_data[['survived']] #산 사람만 빼어놓음
target


training_data = clean_data.drop('survived' ,axis=1 ,inplace=False) #나머지 데이터
training_data.head()


value_data = training_data[['age','fare']] #수를 가진 데이터를 정규화
value_data


from sklearn.preprocessing import StandardScaler #정규화작업
scaler = StandardScaler()
scaled_data = scaler.fit_transform(value_data)
value_data = pd.DataFrame(scaled_data,columns=value_data.columns)
value_data.head()


training_data.drop(['age','fare'] ,axis=1,inplace=True) #value로 뺏으니 삭제함
training_data.head()


onehot_data=pd.get_dummies(training_data['pclass']) #onehot엔코딩   가변수화
onehot_data.head()


onehot_data = pd.get_dummies(training_data ,columns=training_data.columns) #onehotencoding
onehot_data.head()


onehot_data.info()


training_data = pd.concat([value_data,onehot_data] ,axis=1)
training_data.info()


training_data=training_data.astype('float64')


from sklearn.model_selection import train_test_split #학습시켜보자
x_train,x_test,y_train,y_test=train_test_split(training_data,target,test_size=0.20)


print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape)


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout


model = Sequential()
model.add(Dense(128,input_dim=34,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(256,input_dim=34,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(512,input_dim=34,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(256,input_dim=34,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128,input_dim=34,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(64,input_dim=34,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32,input_dim=34,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1,input_dim=34,activation='sigmoid'))
model.summary()


model.compile(loss='mse',optimizer='adam',metrics=['binary_accuracy'])


fit_hist=model.fit(x_train,y_train,batch_size=50,epochs=5,validation_split=0.2,verbose=1)


import matplotlib.pyplot as plt
plt.plot(fit_hist.history['binary_accuracy'])
plt.plot(fit_hist.history['val_binary_accuracy'])
plt.show()


score = model.evaluate(x_test,y_test,verbose=0)
print('loss',score[0])
print('accuracy',score[1])