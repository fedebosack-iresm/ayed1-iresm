class Auto:
    def __init__(self,patente,modelo):
        self.patente = patente
        self.modelo = modelo
    
    def get_patente(self):
        return self.patente

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def get_nombre(self):
        return self.nombre