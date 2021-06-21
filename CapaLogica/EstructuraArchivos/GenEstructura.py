'''
Created on 21 jun. 2021

@author: monto
'''

import Discos

class Estructura():
    def __init__(self):
        self.nombre = ''
        self.raiz = ''
    
    def crear_carpeta(self, nombre, tipo, parent):
        carpeta = Discos.Carpeta(nombre, tipo, parent)
        return carpeta
    
    def crear_tipo(self, nombre, tipo, tamanio):
        tipo = Discos.Tipo(nombre, tipo, tamanio)
        return tipo
    
    def get_path(self):
        return self.raiz.get_path()
    