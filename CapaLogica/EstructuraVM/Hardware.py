'''
Created on 21 jun. 2021

@author: monto
'''

class Procesador():
    def __init__(self):
        self.modelo = ''
        self.cant_procesadores = 0
    
    def set_modelo(self, modelo):
        self.modelo = modelo
    
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
        self.shape = 'Dinamico'
        self.tipo = ''
        
    def set_tipo(self, tipo):
        self.tipo = tipo
    
    
class StaticShape(OracleShape):
    def __init__(self):
        self.shape = 'Estatico'
        self.tipo = ''
        
    def set_tipo(self, tipo):
        self.tipo = tipo
    
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
    
class MaquinaVirtual():
    def __init__(self):
        self.hostname = None
        self.dominio = None
        self.ambiente = None
        self.es_cluster = None
        self.cluster = None
        self.ip = None
        self.shape = None
        self.SO = None
        self.storage = None
        
    def set_hostname(self, hostname):
        self.hostname = hostname
        
    def set_dominio(self, dominio):
        self.dominio = dominio
        
    def set_ambiente(self, ambiente):
        self.ambiente = ambiente
        
    def set_es_cluster(self, es_cluster):
        self.es_cluster = es_cluster
        
    def set_cluster(self, nombre):
        self.cluster = nombre
        
    def set_ip(self, ip):
        self.ip = ip
        
    def set_shape(self, shape):
        self.shape = shape
    
    def set_SO(self, SO):
        self.SO = SO
        
    def set_storage(self, storage):
        self.storage = storage
    
    

