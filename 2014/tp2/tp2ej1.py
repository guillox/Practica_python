"""
1.- a) Dadas las instrucciones  if, else y elif vistas en teoría programe los ejemplos ahí
vistos e indique qué realizan (haga varias corridas modificando los valores en las 
variables).

"""
dia = "1 de enero"
if dia == "1 de enero":
    print("¡FELIZ AÑO NUEVO!")

sexo = "M"
if sexo == "M":
    print("la persona es mujer")
else:
    print("la persona es hombre")

hora = 14
if hora <= 6 and hora >= 12:
    print("buenos dias!!")
elif hora > 12 and hora < 20:
    print("buenas tardes !!")
else:
    print ("Buenas noches!!")


