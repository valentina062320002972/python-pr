# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:14:59 2020

@author: valentina Bustos
"""

from sklearn import datasets, linear_model

###importar los datos
boston=datasets.load_boston()
print(boston)
print()
##VERIFICA LA CARACTERISTICA
print("imformacion del dataset:")
print(boston.keys())
print()
#VERIFICA LA DESCRIPCION
print("caracteristicas de dataset")
print(boston.DESCR)
##VERIFICAR LA CANTIDAD DE LOS DATOS
print("cantidad de datos")
print(boston.data.shape)
print()
######PREPARAR LA DATA PARA LA REGRESION##########################################
X_multiple=boston.data[:, 5:8]
print(X_multiple)
##DEFINO Y
y_multiple=boston.target
######IMPLEMENTACION DEL MODELO#################################
from sklearn.model_selection import train_test_split

###separo los datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split( X_multiple, y_multiple, test_size = 0.2)
####establecer el modelo
lr_multiple=linear_model.LinearRegression
####entrenar
lr_multiple.fit(X_train, y_train)
###prediccion
Y_pred_multiple = lr_multiple.predict(X_test)
