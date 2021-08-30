"""
El programa debe:
*   mostrar el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
*  si el usuario escribe "hola" o "chau" que no se haga el eco
"""
numero=int(input("ingrese un numero entero: "))
for i in range(numero,0,-1):
    print(i,end=",")