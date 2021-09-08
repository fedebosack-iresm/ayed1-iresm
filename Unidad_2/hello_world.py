#polideportivo
futbol = True
basket = True
voley = False
#condiciones de los amigos
condicion_amigo1 = futbol
condicion_amigo2 = basket or voley
condicion_amigo3 = not voley

van_los_amigos = (condicion_amigo1) and (condicion_amigo2) and (condicion_amigo3)

print(f"Los amigos van a ir? {van_los_amigos}")