import time
contraseña = input(" por favor escriba una contraseña  ")
contraseña_2 = input(" por favor confirme su contraseña ")
if contraseña != contraseña_2 :
    print (" las contraseña no coinciden,intentelo de nuevo ")
else: 
    print (" su contraseña ha sido guardada")
time.sleep(1)
idk = input("por favor introduzca su contraseña")
if idk != contraseña:
    print ("contraseña incorrecta vuelva intentarlo")
else:
    print ("bienvenido a este programa  ")
    