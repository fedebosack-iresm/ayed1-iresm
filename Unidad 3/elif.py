condicion=input("""Por favor ingrese una opcion
- imprimir
- 1
- 2
- salir
ingreso : """)

if condicion.isnumeric():
  if int(condicion)==1:
    print("ingreso 1")
  elif int(condicion)==2:
    print("ingreso 2")
  else:
    print("numero ingresado incorrecto!")
else:
  if condicion=="imprimir":
    print("ingreso imprimir")
  elif condicion=="salir":
    print("ingreso salir")
  else:
    print("cadena ingresada incorrecto!")