
dinero_disponible = 50000 # esta es mi variable global
lista = [1,2,3]

def ingresar_y_actualizar():
    global dinero_disponible # voy a hacer uso de la variable
    while True:
        try:
            dinero_ingresar = float(input("Ingrese dinero a depositar: "))
        except:
            print("Error en los parametros")
        if dinero_ingresar > 0 :
            break
        else:
            print("Por favor ingrese una suma positiva")

    dinero_disponible += dinero_ingresar
    return dinero_disponible

print(f"nuevo Monto = {ingresar_y_actualizar()}")
