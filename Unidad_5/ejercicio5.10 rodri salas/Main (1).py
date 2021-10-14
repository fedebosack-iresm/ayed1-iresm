"""
El programa debe:
*   Simular la conversion de un alfabeto a otro: Por ejemplo el moorse 
    (NO ES ESTRICTAMENTE NECESARIO USAR ESTE ALFABETO, PUEDE SER INVENTADO)

```
 alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]
```

*   Contar con 6 funciones disponibles en el menu:
    1. Mostrar el alfabeto A --->LISTO
    2. Mostrar el alfabeto B --->LISTO
    3. Modificar una letra del Alfabeto A y el alfabeto B (debe ser la misma) --->LISTO
    4. Conversion de alfabeto A a alfabeto B: ejemplo **abc --> .--...-.-.** --->LISTO
    5. Conversion de alfabeto B a alfabeto A: ejemplo **.--...-.-. --> abc** --->LISTO
    6. Verificacion de existencia de una letra del alfabeto (debe seleccionar A o B) --->LISTO

*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
"""
import Funciones as fn

alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]

while True:
    opcion=input("""Por favor ingrese una opcion:
    1. Mostrar el alfabeto A 
    2. Mostrar el alfabeto B 
    3. Modificar una letra del Alfabeto A y el alfabeto B (debe ser la misma)
    4. Conversion de alfabeto A a alfabeto B: ejemplo **abc --> .--...-.-.**
    5. Conversion de alfabeto B a alfabeto A: ejemplo **.--...-.-. --> abc**
    6. Verificacion de existencia de una letra del alfabeto (debe seleccionar A o B)
    7. Salir
    Opcion: """)
    if opcion=="1":
        fn.imprimir_abc_a(alfabeto_a)
    elif opcion=="2":
        fn.imprimir_abc_b(alfabeto_b)
    elif opcion=="3":
        fn.modificar_letras_en_ambos (alfabeto_a,alfabeto_b)
    elif opcion=="4":
       fn.conversion_de_a_b(alfabeto_a,alfabeto_b)
    elif opcion=="5":
       fn.conversion_de_b_a(alfabeto_a,alfabeto_b)
    elif opcion=="6":
       fn.verificar_existencia(alfabeto_a,alfabeto_b)
    elif opcion=="7":
        break
    else:
        print("Reintentar, valor incorrecto.")