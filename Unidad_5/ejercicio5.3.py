"""
##**Ejercicio 5.3**
Crear una funcion que debe:

*    Pedir al usuario 5 materias (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
*    Verficiar que sea un nombre correcto
*    Almacenar los nombres en una lista
*    Mostrar las materias en orden alfabetico
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
def orden_de_palabras():
    lista_materias= []
    for i in range(5):
        lista_materias = input("ingrese una materia: ") 
    
    lista_materias.sort()
    print(lista_materias)

orden_de_palabras()