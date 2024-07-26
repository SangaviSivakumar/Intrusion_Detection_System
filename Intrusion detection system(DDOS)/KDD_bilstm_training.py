import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import *
from tensorflow.keras.layers import *
import tensorflow.keras as tf
import bilstm
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score

import seaborn as sns
import pandas as pd

import pandas as pd

df = pd.read_csv(
    'KDD.txt', sep=",",header=None)
print("")
print(df)
print("")

df=df.dropna(how="any")
print(df)
print("")
print(df.info())
print("")

#Data Visualization

#histogram of output

plt.figure(figsize=(10,8))
plt.title("Histogram of Output")
plt.hist(df[41],rwidth=0.9)
plt.show()

df[41] = df[41].map({"teardrop.":5,"satan.":4,"portsweep.":3,"smurf.":2,"neptune.":1,"normal.":0})
print(df)

print(df[41].value_counts())
X = df.iloc[:,4:41].values
y = df.iloc[:, 41].values
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 121)#101

print("Xtrain value")
print(X_train)
print("ytrain value")

print(y_train)

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
ytest = to_categorical(y_test)
y_train


#improved BiLSTM Layers)
model = Sequential()
net = model.add(Dense(64,input_dim=37,activation='relu'))
net = model.add(bilstm.bilstm_layer(net, 128))
net = model.add(bilstm.bilstm_layer(net, 256))
model.add(Dense(6,activation='softmax'))

model.compile(loss="categorical_crossentropy",optimizer='adam',metrics=['accuracy'])

history = model.fit(X_train,y_train,epochs=10)
model.save("bilstm_training.h5")
print(history.history.keys())

plt.figure(figsize=(20,10))
plt.title('Optimizer : Adam', fontsize=10)
plt.ylabel('Loss', fontsize=16)
plt.plot(history.history['loss'], label='Training Loss')
plt.legend(loc='upper right')
plt.show()

plt.figure(figsize=(20,10))
plt.title('Optimizer : Adam', fontsize=10)
plt.ylabel('Accuracy', fontsize=16)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.legend(loc='upper right')
plt.show()
