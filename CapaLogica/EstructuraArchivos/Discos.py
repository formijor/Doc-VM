'''
Created on 21 jun. 2021

@author: monto
'''

class Carpeta():
    def __init__(self):
        self.nombre = ''
        self.tipo = ''
        self.tamanio = 0
        self.parent = ''
        
    def set_parent(self, parent):
        self.parent = parent
        
    def get_parent(self):
        return self.parent
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
    
class Tipo():
    def __init__(self):
        self.nombre = ''
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
    

    