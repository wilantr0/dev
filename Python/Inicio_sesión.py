#calculadora amb un registre previ

name = "admin"
password = "1234"
passwordInit = ""
nameInit = ""
action = ""


#funció de calculadora
def calculadora():
    operación = ""
    operacion = 0.0
    print("""       
           CALCULADORA             
                                   
       Indica a continuació        
   quina operació vols realitzar:
      Ex. 2*2 || 2+2 || 2/2
   
   """)

    operación = input("            ")
    operacion = eval(operación)  #Passa l'string a operació matemàtica
    print(f'El resultat de la operació és {operacion}')

    while True:
        opt = input("Vols fer una altra operació?(S/n) ")
        if opt == 's' or opt == 'S':
            calculadora()
        elif opt == 'n' or opt == 'N':
            print("")
            break
        else:
            print('Siusplau introdueix un caracter correcte')
            continue


def iniciar_sesion():
    print('Nombre de usuario:')
    nameInit = input()
    print('Contraseña:')
    passwordInit = input()
    if nameInit == name and passwordInit == password:
        calculadora()
    elif passwordInit == "" or nameInit == "":
        print("Usuario o contraseña incorrecto")
        iniciar_sesion()
    elif passwordInit != password and nameInit != password:
        print('Nombre y contraseña incorrectos. Por favor vuelva a intentarlo')
        iniciar_sesion()
    elif nameInit != name:
        print("Nombre de usuario incorrecto")
        iniciar_sesion()
    elif passwordInit != password:
        print('Contraseña incorrecta')
        iniciar_sesion()


print("Registro e inicio de sesión")
while True:
    action = input(
        'Si quieres registrarte pulsa R y si quieres iniciar sesión pulsa I: ')

    if action == "R" or action == "r":
        print("Introduce tu nombre de usuario:")
        name = input()
        print("Gracias! Ahora pon tu contraseña:")
        password = input()
        action = input("Para iniciar sesion pulsa I para salir pulsa X: ")
        if action == "X" or action == "x":
            print("Adios", name)
        elif action == "I" or action == "i":
            iniciar_sesion()
        else:
            print('Indique un valor valido')
    elif action == "I" or action == "i":
        iniciar_sesion()
    else:
        print('Indique un valor valido')
