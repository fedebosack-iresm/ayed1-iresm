flag = True
while flag:
    try:
        dato_1 = str(input("Ingrese la contraseña "))
        if dato_1.lower() == "python":
            print("La contraseña es correcta")
            flag = False
    except:
        print("ERROR.")