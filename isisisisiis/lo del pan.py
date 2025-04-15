precio_pan = 3.49
precio_pan_con_descuento = 1.40
x = int(input(" ¿cuantas barras de pan que no son del dia se vendieron? "))
print ("el valor de un pan del dia es de 3.49 pesos y los que no son del dia tienen un descuento del 60%, por lo tal tendrian un valor de 1.40 pesos")
valor_total = ( precio_pan_con_descuento * x)
print (f"por ende el valor total de la compra sera de:{valor_total:.2f} pesos")