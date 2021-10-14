'''##**Ejercicio 5.6 (Programa de Inventario de verduleria)**
Crear un prgrama que debe:
*    Contar con un stock de frutas y otro de verduras (El stock indica si venden o no esa fruta o verdura, no la cantidad) - dos listas que inician vacias
*    Contar con un menu y 3 funciones

      1. Agregar frutas o verduras al correspondiente stock (verificando que que sean nuevas)
      2. Consultar el stock de frutas o verduras
      3. Eliminar un elemento del stock'''
frutas = []
verduras = []

def agregarStock():
    while True:
        frutaOverdura = input('que desea agregar?\n1.fruta\n2.verdura\n3.fin  ')
        if frutaOverdura == "1":
            elemento = input('escriba la fruta que quiere agregar: ')
            if elemento not in frutas:
                frutas.append(elemento)
            else:
                print('el elemento ya existe')
        elif frutaOverdura == "2":
            elemento = input('escriba la verdura que quiere agregar: ')
            if elemento not in verduras:
                verduras.append(elemento)
            else:
                print('el elemento ya existe')
        elif frutaOverdura == "3":
            print(frutas,verduras)
            break
        else:
            print("debe ingresar una de las opciones (1-2-3) ")

def consultarStock():
    print("Las frutas disponibles son: ")
    for fruta in frutas:
        print(fruta,end=",")    
    print("\nLas verduras disponibles son: ")
    for verdura in verduras:
        print(verdura,end=",")
    print("\n") 

def eliminarDeStock():
    objetoRemover = input("Escriba el elemento que desea eliminar del stock: ")
    if objetoRemover in frutas:
        frutas.remove(objetoRemover)
        print(f"{objetoRemover} se removio del stock.\n")
    elif objetoRemover in verduras:
        verduras.remove(objetoRemover)
        print(f"{objetoRemover} se removio del stock.\n")
    else:
        print(f"Error {objetoRemover} no se encuentra en el stock.\n")        
    

while True:
    opcion=input(
    """Por favor ingrese una opcion:
    1. Agregar fruta o verdura al stock
    2. consultar stock
    3. borrar elemento del stock
    4. Salir  """
    )
    if (opcion=="1"):
        agregarStock()
    elif (opcion=="2"):
        consultarStock()
    elif (opcion=="3"):
        eliminarDeStock()
    elif (opcion=="4"):
        break
    else:
        print("ninguna opcion correcta")