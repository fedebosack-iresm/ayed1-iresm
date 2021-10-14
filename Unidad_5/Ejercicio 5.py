"""
El programa debe:
*    Contar con 4 funciones:
        1.  Conversor de Grados Celcius a Fahrenheit(temperatura en °C).(buscar regla)
        2.  Conversor de cm3 a litros (cantidad de cm3)
        3.  Conversor de litros a cm3 (cantidad de litros)
        4.  Pesos a Dolares (pesos)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
'''Conversor de grados a celcius'''
def convensor_de_grados_celcius_a_fahrenheit (temperatura_en_c):
    return print(f"{temperatura_en_c} grados celcius son {((9/5)*temperatura_en_c)+32} grados Fahrenheit ")
    
'''Conversor de grados a celcius'''
def convensor_de_cm3_a_litros (cantidad_de_cm3):
    return print(f"{cantidad_de_cm3} cm3 es igual a {cantidad_de_cm3/1000} litros.")

def conversor_de_litros_a_cm3 (cantidad_de_litros):
    return print(f"{cantidad_de_litros} litros es igual a {cantidad_de_litros*1000} cm3.")

def pesos_a_dolares (pesos):
    return print(f"{pesos} pesos es igual a {pesos/180} dolares.")


while True:
    condicion=input("""
    Por favor ingrese que función desea realizar.
    1. Conversor de Grados Celcius a Fahrenheit
    2. Conversor de cm3 a litros 
    3. Conversor de litros a cm3
    4. Pesos a Dolares
    5. Salir

    Opcion: """)
    if condicion=="1":
        while True:
            try:
                temperatura_en_c=float(input("Ingrese la cantidad de grados celcius a convertir a Fahrenheit: "))
                break
            except:
                print("Ha ingresado un valor erroneo, reintentar.")
        convensor_de_grados_celcius_a_fahrenheit(temperatura_en_c)
    elif condicion=="2":
        while True:
            try:
                cantidad_de_cm3=float(input("Por favor ingrese una cantidad de cm3 para pasar a litros: "))
                if cantidad_de_cm3<0:
                    print("Recurde que no puede ser negativa la cantidad en cm3, reintentar.")
                else:
                    break
            except:
                print("Ha ingresado un valor incorrecto, reintentar.")
        convensor_de_cm3_a_litros(cantidad_de_cm3)
    elif condicion=="3":
        while True:
            try:
                cantidad_de_litros=float(input("Por favor ingrese una cantidad de litros para pasar a cm3: "))
                if cantidad_de_litros<0:
                    print("Recurde que no puede ser negativa la cantidad en litros, reintentar.")
                else:
                    break
            except:
                print("Ha ingresado un valor incorrecto, reintentar.")
        conversor_de_litros_a_cm3(cantidad_de_litros)
    elif condicion=="4":
        while True:
            try:
                pesos=float(input("Ingrese una cantidad de pesos a convertir en dolares: "))
                if pesos<0:
                    print("Error, usted no puede tener una cantidad negativa de pesos. Reintentar.")
                else:
                    break
            except:
                print("Ha ingresado un valor no valido, reintentar.")
        pesos_a_dolares(pesos)
    elif condicion=="5":
        break
    else:
        print("Error, no ha introducido una opción valida. Reintentar.")