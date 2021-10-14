"""
Crear una funcion que debe: (usar listas)

*    Pedir al usuario cantidad de personas
*    Pedir al usuario una a una la edad de las personas
*    Finalizado la carga de las edades debe imprimir por pantalla la edad mayor
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
def ordenar_edades():
    while True:
        try:
            personas = int(input('Ingrese la cantidad de personas: '))
            break
        except:
            print("Ingrese un numero")

    edades = []
    for i in range(personas):
        while True:
            try:
                edadesingresadas = int(input(f'Ingrese la edad de la persona #{i+1}: '))
                edades.append(edadesingresadas)
                break
            except:
                print("Ingrese un numero")
        
    edades.sort()
    print(f'La edad mayor ingresada es {edades[-1]}\nLa lista completa es: {edades}')

ordenar_edades()