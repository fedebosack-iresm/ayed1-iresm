"""
Crear una clase de Peliculas:
*   Cuyo constructutor debe inicializar los atributos nombre, año, genero, nacionalidad, puntuacion
*   Se deben crear 4 metodos en la clase:
    1.  Presentar la pelicula: La pelicula {nombre} de {genero} del {año} obtuvo una puntuacion de {puntuacion}  
        y fue filmada en {nacionalidad}
    2. Retornar si el año de la pelicula es mayor o igual o menor al pasado por parametro
    3. Cambiar el genero de una pelicula
    4. Modificar puntuacion de la pelicula"""
class Pelicula:
    #constructor
    def __init__(self,nombre,año,genero,nacionalidad,puntuacion):
        self.nombre = nombre #unico
        self.año = año
        self.genero = genero
        self.nacionalidad = nacionalidad
        self.puntuacion = puntuacion

    def presentar_pelicula(self):
        print(f"""La pelicula {self.nombre} de {self.genero} del {self.año} obtuvo una puntuacion de {self.puntuacion} y fue filmada en {self.nacionalidad}""")

    #Retornar si el año de la pelicula es mayor o igual o menor al pasado por parametro
    def mayor_menor_igual(self,año_comparar):
        if self.año > año_comparar:
            print(f"El año de la pelicula es mayor a {año_comparar}")
        elif self.año == año_comparar:
            print(f"El año de la pelicula es igual a {año_comparar}")
        else:
            print(f"El año de la pelicula es menor a {año_comparar}")

    def cambiar_genero(self,nuevo_genero):
        self.genero = nuevo_genero
        print(f"El nuevo genero de la pelicula es {self.genero}")

    def modificar_puntuacion(self,nueva_puntuacion):
        self.puntuacion = nueva_puntuacion
        print(f"La nueva puntuacion de la pelicula es {self.puntuacion}")