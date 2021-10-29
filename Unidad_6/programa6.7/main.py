"""
####**Ejercicio 6.7 (Zoologico)**
*   Simular un programa de gestion de animales de un zoologico, que cuente con dos clases Animales y Empleados
*   La Clase Animales tiene los atributos (nombre, tipo_animal, fecha_nacimiento, encargado_cuidar (Nombre de objeto empleado))
    *   Crear 3 clases que hereden de animal segun su sector del zoologico)
        1. Animales en jaulas.
        2. Animales sueltos.
        3. Animales en el agua
*   La Clase Empleados tiene los atributos (legajo, nombre, apellido, lista_animales_a_cuidar(clase animal))
      *  un empleado puede cuidar animales de diferentes sectores
*   Contar con 6 funciones disponibles en el menu **(estas funciones deben estar incluidas en una clase llamada GestorZoologico)**:
    1. Crear instancias de animales (se puede elegir entre los tres sectores)  y guardarlos en una lista
    2. Crear instancia de Empleados y guardarlos en una lista
        * Los empleados se les pueden asignar animales luego, los animales al crearlos en el sistema tienen q contar siosi con un encargado
    3. Asignar a un empleado un animal a cuidar
    4. Cambiar de encargado un animal
    5. imprmir lista de animales (con toda su informacions)
    6. imprimir lista de Empleados (con toda su informacions)

*   Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
"""
import GestorZoo as gz

gestor = gz.GestorZoo()

while True:
    opcion = input(
    """
-----------Menu principal-----------
Por favor ingrese una opcion:
    1. Crear Empleado
    2. Crear Animal
    3. 
    4. 
    5. imprmiir Empleados
    6. imprimir Animal
    7. Salir
    Opcion: """
    )
    if (opcion=="1"):
        gestor.crear_instancia_empleado()
    elif (opcion=="2"):
        pass
    elif (opcion=="3"):
        pass
    elif (opcion=="4"):
        pass
    elif (opcion=="5"):
        gestor.imprimir_empleados()
    elif (opcion=="6"):
        pass
    elif (opcion=="7"):
        break
    else:
        print("ninguna opcion correcta")