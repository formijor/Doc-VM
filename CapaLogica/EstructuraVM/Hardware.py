'''
Created on 21 jun. 2021

@author: monto
'''

class Procesador():
    def __init__(self):
        self.cant_procesadores = 0
    
    def set_cant_procesadores(self, cantidad):
        self.cant_procesadores = cantidad
        
    def get_cant_procesadores(self):
        return self.cant_procesadores
    
    def set_multiplicador_nucleos(self, multiplicador):
        self.multiplicador_nucleos = multiplicador
        
    def get_multiplicador_nucleos(self):
        return self.multiplicador_nucleos
    
    def get_cantidad_nucleos(self):
        return self.get_cant_procesadores() * self.get_multiplicador_nucleos()
    
class Ram():
    def __init__(self):
        self.cant_ram = 0
        
    def set_cant_ram(self, cantidad):
        self.cant_ram = cantidad
        
    def get_cant_ram(self):
        return self.cant_ram
    
class Storage():
    def __init__(self):
        self.lista_storage = []
        
    def add_storage(self, storage):
        self.lista_storage.append(storage)
    
class OracleShape():
    def __init__(self):
        self.nombre = ''
        self.procesador = ''
        self.ram = ''
        
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
    
    def set_procesador(self, procesador):
        self.procesador = procesador
        
    def set_ram(self, ram):
        self.ram = ram
    
class DinamicShape(OracleShape):
    def __init__(self):
        pass
    
    
class StaticShape(OracleShape):
    def __init__(self):
        pass
    
class SistemaOperativo():
    def __init__(self):
        self.SO = ''
        self.version = ''
        self.edicion = ''
        self.arquitectura = ''
        
    def set_SO(self, SO):
        self.SO = SO
        
    def set_version(self, version):
        self.version = version
        
    def set_edicion(self, edicion):
        self.edicion = edicion
        
    def set_arquitectura(self, arquitectura):
        self.arquitectura = arquitectura
    
