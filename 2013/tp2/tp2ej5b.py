"""b) Modifique el ejercicio anterior para que a los numeros impares los eleve al cuadrado y a los pares al cubo."""

lista=[2, 3, 4, 5, 6]
for i in range(0,len(lista)):
        print'entro al for'
        if lista[i]%2==1:
                lista[i]=lista[i]**2
                print'entro al if'
        else:
                lista[i]=lista[i]**3
                print'entro al else'
print lista
