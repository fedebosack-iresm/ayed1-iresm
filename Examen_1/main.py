import funciones as fn
while True:
    opcion=input("""\nIngrese una opcion
    1. Ver lista de alumnos
    2. Agregar un nuevo alumno
    3. Cambiar de edad de alumno
    4. Ver lista de materias
    5. Agregar materias
    6. Salir

    Opcion: """)
    if opcion == "1":
        fn.listar()
    elif opcion == "2":
        fn.agregar_alumno()
    elif opcion == "3":  
        fn.editar_edad()
    elif opcion == "4":
        fn.listar_materias()
    elif opcion == "5":
        fn.agregar_materias()
    elif opcion == "6":
        break
    else:
        print("\nValor ingresado incorrecto, reintentar.")