class Currency(object):## representa la modena
    
    def __init__(self,simbolo,nombre,factor):## cuando se inicia la clase
        self.nombre=nombre
        self.simbolo=simbolo
        self.factor=factor
    def _convert_to_base_currency(self ,anumber):## devuelvela modena base
        return self.factor*anumber
    def _convert_from_base_currency(self,anumber):##devuelva la moneda actual
        return anumber/self.factor
    def __repr__(self):## devuelve el objeto en pantalla
        return self.nombre
class money(object):##la cantidade dinero
    def __init__(self,monto,moneda):## tiene dos instancias
        self.monto=monto
        self.moneda=moneda
    def base_currency(self):
        return self.moneda._convert_to_base_currency(self.monto)
    def __add__(self,objeto2):##son metodos magicos para la operaciones
        monto=self.base_currency()+objeto2.base_currency()
        monto=self.moneda._convert_from_base_currency(monto)
        return  money(monto,self.moneda)
    def __mul__(self,numero):## metodo magico para multiplicacion
        return money(self.monto*numero,self.moneda)
        

    def __repr__(self):
        return '{} {}'.format( self.monto,self.moneda.simbolo)
    
    
dolar=Currency('dolar','U$S',1)
Pesos=Currency('Pesos','$',1/40)

one_dolar=money(1,dolar)
two_pesos=money(2,Pesos)
one_dolar+two_pesos
print(one_dolar+two_pesos)
print(one_dolar*10)

