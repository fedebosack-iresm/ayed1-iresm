"""
Ejercicio
El programa debe:
*    Pedir al usuario una cantidad de tramos de un viaje
*    Pedir al usuario la duracion en minutos de cada tramo
*    calcular el tiempo total de viaje
*    No deben generar errores
"""
while True:
    try:
        cantidad_tramos = -1
        while cantidad_tramos<=0:
            cantidad_tramos = int(input("Ingrese la cantidad de tramos: "))

        tiempo_total_viaje=0
        for i in range(cantidad_tramos):
            while True:
                tiempo_tramo=int(input(f"Ingrese la duracion del tramo {i+1}: "))
                if(tiempo_tramo<0):
                    print("Por favor ingrese un numero mayor o igual a cero")
                else:
                    tiempo_total_viaje +=tiempo_tramo
                    break
        print(f"El tiempo total del viaje fue de: {round(tiempo_total_viaje/60,2)} horas")
        break
    except:
        print("error en las variables")