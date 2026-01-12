# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:38:09 2020

@author: hp
"""

from sklearn import datasets
###preparar la data
dataset=datasets.load_breast_cancer()
print(dataset)
########conocer los datos
print("la informacion de los datos")
print(dataset.keys())
print()
####ver la descripcion de los datos###
print("la descripcion de los datos")
print(dataset.DESCR)
####SELCIONASMOS LAS VARIABLES
x=dataset.data
####selcionamos y
y=dataset.target
###separo los datos de entrenamiento y de prueba
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
######escarlar los datos
from sklearn.preprocessing import StandardScaler
escalar=StandardScaler()
X_train=escalar.fit_transform(X_train)
X_test=escalar.transform(X_test)
###hacemos el modelo
from sklearn.linear_model import LogisticRegression
algoritmo=LogisticRegression()
###entrenamiento
algoritmo.fit(X_train,y_train)
###prediccion
Y_pred = algoritmo.predict(X_test)
print(Y_pred)
##revisar las metricas
from sklearn.metrics import confusion_matrix

matrix=confusion_matrix(y_test,Y_pred)
print("matrizde confusion")
print(matrix)
###LA PRESICION
from sklearn.metrics import precision_score

presicion=precision_score(y_test,Y_pred)
print("prescion:")
print(presicion)
####La exactitud
from sklearn.metrics import accuracy_score
exactitud=accuracy_score(y_test,Y_pred)
print("la exactitud")
print(exactitud)
####La sensibilidad
from sklearn.metrics import recall_score
sensibilidad=recall_score(y_test,Y_pred)
print("sensibilidad:")
print(sensibilidad)
###el puntaje
from sklearn.metrics import f1_score
f1=f1_score(y_test,Y_pred)
print("El puntaje F1 del modelo:")
print(f1)
###por ultimo la curva  ROC
from sklearn.metrics import roc_auc_score
curva=roc_auc_score(y_test,Y_pred)
print("curva ROC")
print(curva)

