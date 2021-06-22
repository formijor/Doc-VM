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
    
class OracleShape():
    def __init__(self):
        pass
    
class OracleDinamic(OracleShape):
    def __init__(self):
        pass
    
class SistemaOperativo():
    def __init__(self):
        pass
    
