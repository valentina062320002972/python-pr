
import unittest
from  tkinter import *
from tkinter import ttk
from unittest import TestCase
from tkinter import messagebox 
 ## ventana
ventana = Tk()
ventana.config(width=800, height=500)
## cajas de texto
tbx_codigo = ttk.Entry(ventana)# Crear caja de texto.
tbx_codigo.place(x=90, y=50)   

tbx_pago= ttk.Entry(ventana)# Crear caja de texto.
tbx_pago.place(x=90, y=250)  


texto_detalle = Text(ventana,height=9,width=32)
texto_detalle.place(x=90,y=90)

## etiquetas
lbl_codigo = ttk.Label(ventana)
lbl_codigo.place(x=20,y=50)
lbl_codigo.configure(text="Codigo")

lbl_subtotal = ttk.Label(ventana)
lbl_subtotal.place(x=20,y=90)
lbl_subtotal.configure(text="Detalle")
lbl_lista = ttk.Label(ventana)
lbl_lista.place(x=350,y=50)
lbl_lista.configure(text="PRODUCTOS: \ncodigo-  producto: \n123   -  chocolate \n124   -    matequilla  \n125   -    Pera")
lbl_pago = ttk.Label(ventana)
lbl_pago.place(x=20,y=250)
lbl_pago.configure(text="Pago \ncliente")

class NegativeValueError(Exception):
    pass
objeto2=NegativeValueError()
class caja(object): 
   
    def __init__(self):
         self.factura=factura() 
    def _total_(self):
        
        texto="Producto\t\tprecio Rebajado\n"
        for i in range(0,len(self.factura.lista)):  
            
            texto=texto+str(self.factura.lista["item"+str(i+1)][1])+"\t\t"+str(float(self.factura.lista["item"+str(i+1)][0]-1*self.factura.lista["item"+str(i+1)][2]))+"\n"
        texto2=texto+"subtotal"+"\t\t"+str(self.factura.suma)+"\n"+"TOTAL"+"\t\t"+str(self.factura.total)
        texto_detalle.insert(1.0,texto2)
    def pago(self,dinero):
        
        if float(dinero)<self.factura.total:
            
            messagebox.showwarning('Message error', 'No le alcanza')
            
        else:    
            devueltas=float(dinero)-self.factura.total
        return devueltas
        
    def subtotal(self):
        
        texto1 ="Precio-producto\t\tdescuento\n"
        for key in self.factura.lista:
            texto1=texto1+str(self.factura.lista[key])+"\n"
        texto3=texto1+"subtotal :"+str(self.factura.suma)+"\n"
        texto_detalle.insert(1.0,texto3)
        return  self.factura.suma
    
class factura(object):
    
    def __init__(self):
        self.lista={}
        self.num=0
        self.texto=""
        self.producto=producto()
        
    def _listado_(self,codigo):
        if self.producto._verificacion_(codigo)==True: 
        
            self.lista["item"+str(self.num+1)]=self.producto._to_item__(codigo) 
            self.num=self.num+1
            self._subtotal_() 
        else:
            messagebox.showwarning('Message error', 'codigo invalido')
            tbx_codigo.configure(text=" ")
    def _subtotal_(self):
        self.suma=0
        self.total=0
        for i in range(0,len(self.lista)):  
            self.suma =self.suma+int(self.lista["item"+str(i+1)][0])
            self.total=self.total+(float(self.lista["item"+str(i+1)][0])-float((self.lista["item"+str(i+1)][2]))*float(self.lista["item"+str(i+1)][0]))
        return self.suma,self.total
    def __repr__(self):  
        return self.lista,self.suma,self.total
           
class producto(object):
    
    def __init__(self):
        self.productos = {'123': (20000,"chocolate",0.2), '124': (1900,"mantequilla",0.1),'125':(2200,"pera",0.5)}
        ##self.productos_nombres = {"123": "chocolate", "124": "leche","125":"carbon"}

    def _to_item__(self,codigo):
        valor =self.productos.get(str(codigo))
        return valor
   
    def _verificacion_(self,codigo): 
        
        if codigo in self.productos:
            respuesta =True
           
        else:
            respuesta =False
        return respuesta
        
    

objeto=caja()
##funcion del boton
def funcion_agregador():
    objeto.factura._listado_(tbx_codigo.get())
    tbx_codigo.delete(0,END)
def funcion_sumar():
    texto_detalle.delete(0.0,END)
    objeto.subtotal()
def funcion_finalizar():
     texto_detalle.delete(0.0,END)
     objeto._total_()

     if not tbx_pago.get():
         tbx_pago.insert(0,"0")   
     texto3="DEVOLVER :"+ str(objeto.pago(tbx_pago.get()))
     messagebox.showinfo("PAGO",texto3) 
     return objeto.pago(tbx_pago.get())
     
     
     
       
    
    

###botones

btn_agregar=ttk.Button(ventana)
btn_agregar.configure(command=funcion_agregador,text="agregar")
btn_agregar.place(x=355,y=160)
btn_sumsubtotal=ttk.Button(ventana)
btn_sumsubtotal.configure(command=funcion_sumar,text="sumar subtotal")
btn_sumsubtotal.place(x=355,y=190)
btn_finalizar=ttk.Button(ventana)
btn_finalizar.configure(command=funcion_finalizar,text="Finalizar compra")
btn_finalizar.place(x=355,y=220)



ventana.mainloop()

##testeos
class cajaTest(unittest.TestCase):
    def setUp(self):

        self.cajita=caja()   
        
    def test_verificaion123_(self):
        CODIGO1=self.cajita.factura.producto._verificacion_('123')
        self.assertEqual(True, CODIGO1)
    def test_verificaion124_(self):
        CODIGO1=self.cajita.factura.producto._verificacion_('124')
        self.assertEqual(True, CODIGO1)
    def test_verificaion125_(self):
        CODIGO1=self.cajita.factura.producto._verificacion_('125')
        self.assertEqual(True, CODIGO1)
    def test_verificaionsubtotal1_(self):
        self.cajita.factura._listado_('123')
        self.cajita.factura._listado_('124')
        self.assertEqual(21900,self.cajita.factura.suma)
    def test_verificaionsubtotal2_(self):
        self.cajita.factura._listado_('123')
        self.cajita.factura._listado_('125')
        self.assertEqual(22200,self.cajita.factura.suma) 
    def test_verificaionsubtotal3_(self):
        self.cajita.factura._listado_('124')
        self.cajita.factura._listado_('125')
        self.assertEqual(4100,self.cajita.factura.suma)
    def test_verificaiontotal1_(self):
        self.cajita.factura._listado_('123')
        self.cajita.factura._listado_('124')
        self.assertEqual(17710,self.cajita.factura.total)
    def test_verificaiontotal2_(self):
        self.cajita.factura._listado_('123')
        self.cajita.factura._listado_('125')
        self.assertEqual(17100,self.cajita.factura.total)
    def test_verificaiontotal3_(self):
        self.cajita.factura._listado_('124')
        self.cajita.factura._listado_('125')
        self.assertEqual(2810,self.cajita.factura.total)
    def test_verificaiontotal4_(self):
        self.cajita.factura._listado_('123')
        self.cajita.factura._listado_('124')
        self.cajita.factura._listado_('125')
        self.assertEqual(18810,self.cajita.factura.total)
    def test_verificacionpago1_(self):
        self.cajita.factura._listado_('123')
        self.cajita.factura._listado_('124')
        self.cajita.factura._listado_('125')
        pago1= self.cajita.pago(20000)
        self.assertEqual(1190.0,pago1)
   
    
if __name__=='__main__':
    unittest.main()
    

    