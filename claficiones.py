# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:44:41 2021

@author: hp
"va hacer calificiones de un estudiante"""

class archivo(object):
    def __init__(self,nombre,grado):
        self.nombre=nombre
        self.notas=[]
        self.grado=grado
    def agregardor(self,nota):
        self.notas.append(nota)
    def __repr__(self):  
        return self.nombre
    
class imprimir(object): 
    
    def __init__(self,name):
        self.promediod=0
        self.name=name
        self.promedio()
        
    def promedio(self):
        suma=0
        for i in range(0,len(self.name.notas)):
            suma=suma+self.name.notas[i]
        self.promediod=suma/len(self.name.notas)
            
    def __repr__(self):  
        return '{} {}{}'.format( self.name.nombre,self.promediod,self.name.grado)
       
          
           
    
n=int(input("Ingrese el numero de estudiantes que desea ingresar"))
i=0
while i<n:
    name=input("Ingrese el nombre del estudiante")
    grade=input("Ingrese el grado al que pertenece")
    objt=archivo(name,grade)
    yes=bool(input("Quiere ingresar notas?"))
    if yes==1:
        num=int(input("Ingrese el nuemro de notas"))
        j=0
        while j<num:
             nota=int(input("Ingrese las nota "+str(j+1)))
             objt.agregardor(nota)
             j=j+1
    estudiante=imprimir(objt)
    print(estudiante)
            
            
            
        
     
     
        
        
    

