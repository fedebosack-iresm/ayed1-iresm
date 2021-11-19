'''
************************************************************
 MATERIA: Algoritmos y Estructuras de Datos 1
 EXAMEN: 1° Examen
 APELLIDO Y NOMBRE: 
 DNI: 
 CARRERA: 
 AÑO: 2021 
 Se envia mail con asunto: "[AYEDI 2021 - Apellido, Nombre - 1°Examen]"
 ************************************************************
 Items a evaluar:
 1. Requerimientos y comprension de consignas
 2. Estructura (modularización), legibilidad y comentarios del codigo.

¡Cualquier duda con el enunciado consultar al docente!
************************************************************
ENUNCIADO: "Programa de Gestión de alumnos y Materias"

Introduccion: 
    El siguiente programa consiste en un software de gestion de alumnos y gestion de materias
    de una institucion educativa.
    El programa debe permitir agregar y quitar alumnos al sistema junto con su informacion personal: 
    Nombre, Edad y mail.
    El programa debe permitir agregar Materias al sistema.

Requerimientos:
El programa debe:
*   Contar con un menu donde permita al usuario elegir entre las siguientes funciones:
    1. Ver lista de alumnos (Formato: nombre_usuario - Edad - Mail)
    2. Permitir al usuario del programa agregar un nuevo alumno (Indicando: nombre_usuario - Edad - Mail)
       Verificando: Que el nombre_usuario no exista previamente, la edad entre 10 y 18 años y que el mail cuente con un @.
       (Ayuda: metodo in de list sirve tambien para strings)
    3. Editar la edad de un alumno verificando que este entre 10 y 18 años, se edita mediante el nombre.
    4. Ver lista de materias (Formato: Materias)
    5. Agregar materias al sistema (verificando que no exista previamente)
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
lista_alumnos=[["fede","feli","cris"],[55,66,77],["fede@","feli@","cris"]]

def agregar_alumno():
    while True:
        nombre = input("ingrese el nombre:")
        if nombre in lista_alumnos[0]:
            print("el nombre ya existe")
        else:
            break
    
    while True:
        try:
            edad = int(input("ingrese la edad:"))
            if(edad >= 10 and edad <=18):
                print("Ok")
                break
            else:
                print("debe estar entre 10 y 18")
        except:
            print("error")
    while True:    
        mail = input("ingrese el mail:")
        if "@" in mail:
            break
        else:
            print("El mail debe contener un @")
    
    lista_alumnos[0].append(nombre)
    lista_alumnos[1].append(edad)
    lista_alumnos[2].append(mail)

def listar():
    for i in range(len(lista_alumnos[0])):
        print(f"{lista_alumnos[0][i]} - {lista_alumnos[1][i]} - {lista_alumnos[2][i]}")

def editar_edad():
    listar()
    while True:
        nombre = input("indique el nombre de la persona a cambiar la edad")
        if nombre in lista_alumnos[0]:
            index = lista_alumnos[0].index(nombre)
            while True:
                try:
                    edad = int(input("ingrese la nueva edad:"))
                    if(edad >= 10 and edad <=18):
                        break
                except:
                    print("debe estar entre 10 y 18")
            lista_alumnos[1][index] = edad
            break
        else:
            print("el nombre no existe")