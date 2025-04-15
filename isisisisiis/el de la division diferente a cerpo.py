import time
num_1 = int(input ("hola!, por favor escribe un numero: "))
num_2 = int(input ("ahora escribe otro por favor :"))
time.sleep(2)
print ("ahora vamos a hacer matematicas, y si dividimos estos dos digitos y da igual a cero te diremos que es un error matematico")
time.sleep(1)
if  num_2 == 0 or num_1 == 0:
    print ("error matematico!! no se puede dividir con cero")
else: 
   valor_div = (num_1 / num_2) 
   print (f"oooh re bien el valor que nos da esta division es {valor_div:.3f}")