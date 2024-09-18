# Enunciado:
# Crea una clase Persona que tenga atributos privados para el nombre y la edad. 
# Crea métodos públicos para establecer y obtener el nombre y la edad, garantizando que la edad no pueda ser negativa.

#Andres Felipe Sanchez Romero

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre= nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

