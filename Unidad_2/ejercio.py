"""
El programa debe:

- pedir por teclado el dinero actual de una persona
- pedir por teclado el precio del insumo que quiere comprar en USD
- convertir ese dinero a dolares (1USD -> 170$)
- devoler por pantalla True en caso que pueda comprar, False en caso que no


"""
try:
    dinero_actual_usd = float(input("ingrese su dinero actual (pesos):"))/170
    precio_insumo = float(input("ingrese el precio del insumo que desea comprar (USD):"))
    print(dinero_actual_usd>=precio_insumo)
except:
    print("Error de escritura")