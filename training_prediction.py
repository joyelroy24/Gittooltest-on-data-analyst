import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data=pd.read_csv('Copy of sonar data.csv',header=None)
# header =None will indicate that the csv file not contain a header row and panda should create numbred coulmn starting from o 
print(data.head())
print(data.shape)
# will display no.of.row*no.of.column
print(data.describe())
print(data[3].value_counts())


x=data.drop(columns=4,axis=1)
y=data[4]
print(x)
print(y)


xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.1,random_state=1)
print(xtrain.shape,xtest.shape,ytrain.shape,ytest.shape)

model=LogisticRegression()
model.fit(xtrain,ytrain)
# The fit method is called on the model object, where xtrain is the input features from the training set, and ytrain is the corresponding target variable (labels).
# After this step, the model object contains the learned parameters that describe the relationship between the input features and the target variable based on the training data.

predictions_train = model.predict(xtrain)
# make predictions on xtrain the output will be the labels
print(predictions_train)
accuracy_train=accuracy_score(predictions_train,ytrain)
# accuracy_score is used to calculate the accuracy by comparing the predicted values (predictions_train) with the actual values (ytrain).
print(accuracy_train)


predictions_test=model.predict(xtest)
print(predictions_test)
accuracy_test=accuracy_score(predictions_test,ytest)
print(accuracy_test)

input_data=(0.009,0.0062,0.0253,0.0489)
input_np=np.asarray(input_data)
reshape_data=input_np.reshape(1,-1)
# only 1 data point prediction (1,-1)

pred=model.predict(reshape_data)
print(pred)