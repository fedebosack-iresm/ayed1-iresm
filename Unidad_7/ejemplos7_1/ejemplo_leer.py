import os

#path actual
absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
print(path+"\\archivo.txt")##\\ por caracteres especiales

# Metodo read()
"""
try:
    fichero = open(path+"\\archivo.txt", 'r')
    print(fichero.read())
    fichero.close()
except:
    print("no existe el archivo")
"""
# Metodo readline()
try:
    fichero = open(path+"\\archivo.txt", 'r')
    linea = fichero.readline()
    while  linea != "":
        print(linea,end="")
        linea = fichero.readline()
    fichero.close()
except:
    print("no existe el archivo")
