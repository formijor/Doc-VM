'''
Created on 21 jun. 2021

@author: monto
'''

class Carpeta():
    def __init__(self, nombre, tipo, parent):
        self.nombre = nombre
        self.tipo = tipo
        self.parent = parent
        self.childs = []
        
    def set_parent(self, parent):
        self.parent = parent
        
    def get_parent(self):
        return self.parent
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
    
    def add_child(self, child):
        self.childs.append(child)
        
    def get_path(self):
        '''Devuele la estructura desde raiz hasta esta carpeta'''
        return self.nombre + '/' + self.parent.get_path() 
    
class Tipo():
    def __init__(self, nombre, tipo, tamanio):
        self.nombre = nombre
        self.tipo = tipo
        self.tamanio = tamanio
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
    
    def set_tamanio(self, tamanio):
        self.tamanio = tamanio
        
    def get_tamanio(self):
        return self.tamanio
    

    