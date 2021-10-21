import os

#path actual
absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
print(path+"\\archivo.txt")##\\ por caracteres especiales

try:
    fichero = open(path+"\\archivo2.txt", 'w')
    fichero.write("Contenido a escribir")
    fichero.close()
except:
    print("no existe el archivo")
   
