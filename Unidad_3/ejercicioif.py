"""
El programa debe:

- Pedir el ingreso de un número positivos al usuario y almacenar la respuesta en la variable numero.
- Verificar que se trate de un numero entero y sino mostrar un error
- Comprobar si el número es negativo. Si lo es, el programa debe avisa que no era eso lo que se había pedido. (si no hay error)
- Si el numero es positivo indicar que es positivo
- Finalmente imprimir siempre el valor introducido por el usuario.(si no hay error)
"""
try:
    numero = int(input("por favor ingrese un numero: "))
    if numero < 0:
        print("¡Pedi un numero positivo!")
    else:
        print("¡soy un numero positivo!")

    print(f"El numero que ingrese fue: {numero}")
except:
    print("no ingreso un numero entero")