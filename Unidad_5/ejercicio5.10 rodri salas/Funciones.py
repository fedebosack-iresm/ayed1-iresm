def imprimir_abc_a(alfabeto_a):
    for i in range(len(alfabeto_a)):
        if i+1==len(alfabeto_a):
            print(alfabeto_a[i])
        else:
            print(alfabeto_a[i],end=" - ")
    return


def imprimir_abc_b(alfabeto_b):
    for i in range(len(alfabeto_b)):
        if i+1==len(alfabeto_b):
            print(alfabeto_b[i])
        else:
            print(alfabeto_b[i],end=" || ")
    return

def modificar_letras_en_ambos (alfabeto_a,alfabeto_b):
    indice=0
    while True:
        letra_a_buscar = input("Ingrese cual letra desea modificar: ")
        if letra_a_buscar in alfabeto_a:
            #print(alfabeto_a.index(letra_a_buscar)+1)
            indice = alfabeto_a.index(letra_a_buscar)+1
            #print(indice)
            break
        elif letra_a_buscar in alfabeto_b:
            indice = alfabeto_b.index(letra_a_buscar)+1
            break
            #print(indice)
        else:
            print("La letra no se encuentra en ningún alfabeto disponible.")
            break
    letra_nueva = input(f"Ingrese la palabra/letra nuevo que sustituira a {letra_a_buscar}: ")
    alfabeto_a[indice-1] = letra_nueva
    alfabeto_b[indice-1] = letra_nueva
    print("Se actualizaron los alfabetos!!!")
    return


def conversion_de_a_b(alfabeto_a,alfabeto_b):
    for i in range(len(alfabeto_a)):
        for j in range(len(alfabeto_b)):
               alfabeto_b[i]=alfabeto_a[i]
    print(alfabeto_b)
    return


def conversion_de_b_a(alfabeto_a,alfabeto_b):
    for i in range(len(alfabeto_b)):
        for j in range(len(alfabeto_a)):
               alfabeto_a[i]=alfabeto_b[i]
    print(alfabeto_a)
    return


def verificar_existencia(alfabeto_a,alfabeto_b):
    while True:
        try:
            opcion = int(input("1. Si desea buscar una letra en el alfabeto A.\n2. Si desea buscar una letra en el alfabeto B.\nOpcion: "))
            if opcion == 1:
                print("Usted ha selecionado buscar una letra en el alfabeto A.")
                while True:
                    letra_a_buscar = input("Por favor ingrese la letra buscar: ")
                    if letra_a_buscar in alfabeto_a:
                        print("La letra si está en el alfabeto")
                        return
                    else:
                        print("La letra no esta en el alfabeto")
                        return
            elif opcion == 2:
                print("Usted ha selecionado buscar una letra en el alfabeto B.")
                while True:
                    letra_a_buscar = input("Por favor ingrese la letra buscar: ")
                    if letra_a_buscar in alfabeto_b:
                        print("La letra si está en el alfabeto")
                        return
                    else:
                        print("La letra no esta en el alfabeto")
                        return
            else:
                print("Reintentar, opcion incorrecta.")
        except:
            print("Reintentar, opcion incorrecta.")
