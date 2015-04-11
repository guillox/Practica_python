"""d) ¿Cómo podría lograr con la instrucción p r i n t  la siguiente salida?
Fernandez , Gaston        5.56
Sin completar con blancos manualmente luego del nombre y con la información de la                          
siguiente manera: ( "Fernandez","Gaston " , 5 . 5 6 )
print  ( "%15s  %s  Python"   %   ( " Seminario " , " de " ) )
ejemplos
>>> "Name: %s, age: %d" % ('John', 35) 
'Name: John, age: 35' 
>>> i = 45 
>>> 'dec: %d/oct: %#o/hex: %#X' % (i, i, i) 
'dec: 45/oct: 055/hex: 0X2D' 
>>> "MM/DD/YY = %02d/%02d/%02d" % (12, 7, 41) 
'MM/DD/YY = 12/07/41' 
>>> 'Total with tax: $%.2f' % (13.00 * 1.0825) 
'Total with tax: $14.07' 
>>> d = {'web': 'user', 'page': 42} 
>>> 'http://xxx.yyy.zzz/%(web)s/%(page)d.html' % d 
'http://xxx.yyy.zzz/user/42.html' 
"""

print ( "%s, %s  %15.2f"   %   ( "Fernandez" , "Gaston",5.56 ))
