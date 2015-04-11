"""
5.­ Realice el ejercicio anterior utilizando la librería pickle


import pickle
listapeli=["Monty Python","Gladiador","Star wars","Señor de los anillos","Spiderman"]
print (listapeli)
archivosal=open('pickle.txt','wb')
pickle.dump(listapeli,archivosal)
archivosal.close()
archivoent=open('pickle.txt','rb')
nuevalista=pickle.load(archivoent)
print (nuevalista)
archivoent.close()

"""





