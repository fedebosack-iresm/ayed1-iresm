import Pelicula as pl
lista_peliculas = []

def crear_peliculas():
    #nombre
    while True:
        nombre=input("Ingrese el nombre: ").capitalize()
        if not nombre.isalpha():
            print("Un nombre no puede tener simbolos")
        else:
            lista_peliculas.append(nombre)
            break