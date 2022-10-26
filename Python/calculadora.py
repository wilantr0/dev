import time #modul per controlar el temps

def validation(range): # Ordena i agrupa els numeros
  while True:  
    rango = "-".join(range)
    time.sleep(0.3) # Espera 0.3 segons
    print()
    time.sleep(0.3)
    print()
    time.sleep
    print("Ara has d'escollir 3 dels 4 numeros dels que has fet servir")
    el1, el2, el3 = input(f"Aquestos són els nombres que pots fer servir[{rango}] (Enrecorda't de posar la coma i l'espai): "). split(", ")
    time.sleep(0.5)
    print()
    if el1 and el2 and el3 not in range:
            print("Has d'escollir entre els numeros que has fet servir")
            time.sleep(0.5)
            continue
    elif el1 > el3 and el2 > el3:
            print(f"{int(el3)} és el numero més petit, per tant")
            print(f"{int(el1)} i {int(el2)} > {int(el3)}")
            print()
            time.sleep(0.3)
            if el1 < el3 and el2 < el3:
                print(f"{int(el3)} és el numero més gran, per tant")
                print(f"{int(el1)} i {int(el2)} < {int(el3)}")
                break
            elif el1 < el2 and el3 < el2:
                print(f"{int(el2)} és el numero més gran, per tant")
                print(f"{int(el1)} i {int(el3)} < {int(el2)}")
                break
            elif el2 < el1 and el3 < el1:
                print(f"{int(el1)} és el numero més gran, per tant")
                print(f"{int(el2)} i {int(el3)} < {int(el1)}")
                break
    elif el1 > el2 and el3 > el2:
            print(f"{int(el2)} és el numero més petit, per tant")
            print(f"{int(el1)} i {int(el3)} > {int(el2)}")
            print()
            time.sleep(0.3)
            if el1 < el3 and el2 < el3:
                print(f"{int(el3)} és el numero més gran, per tant")
                print(f"{int(el1)} i {int(el2)} < {int(el3)}")
                break
            elif el1 < el2 and el3 < el2:
                print(f"{int(el2)} és el numero més gran, per tant")
                print(f"{int(el1)} i {int(el3)} < {int(el2)}")
                break
            elif el2 < el1 and el3 < el1:
                print(f"{int(el1)} és el numero més gran, per tant")
                print(f"{int(el2)} i {int(el3)} < {int(el1)}")
                break
    elif el2 > el1 and el3 > el1:
            print(f"{int(el1)} és el numero més petit, per tant")
            print(f"{int(el2)} i {int(el3)} > {int(el1)}")
            print()
            time.sleep(0.3)
            if el1 < el3 and el2 < el3:
                print(f"{int(el3)} és el numero més gran, per tant")
                print(f"{int(el1)} i {int(el2)} < {int(el3)}")
                break
            elif el1 < el2 and el3 < el2:
                print(f"{int(el2)} és el numero més gran, per tant")
                print(f"{int(el1)} i {int(el3)} < {int(el2)}")
                break
            elif el2 < el1 and el3 < el1:
                print(f"{int(el1)} és el numero més gran, per tant")
                print(f"{int(el2)} i {int(el3)} < {int(el1)}")
                break
    elif el1 == el2 or el2 == el1 and el1<el3:
            print(f"{int(el3)} és el numero més gran, per tant")
            print(f"{int(el1)} = {int(el2)} < {int(el3)} ")
            break
    elif el1 == el3 or el3 == el1 and el1<el2:
            print(f"{int(el2)} és el numero més gran, per tant")
            print(f"{int(el1)} = {int(el3)} < {int(el2)}")
            break
    elif el3 == el2 or el2 == el3 and el2<el2:
            print(f"{int(el1)} és el numero més gran, per tant")
            print(f"{int(el2)} = {int(el3)} < {int(el1)} ")
            break

def options(num1, num2): #Calcula els nombres donats
    op = input("""
    Indica quina operació vols realitzar?
    S/s || Suma
    R/r || Resta
    M/m || Multiplicació
    D/d || Divisió
    E/e || Exponent
    A/a || Arrel quadrada

    """)

    op = op.lower() #Passa les lletres a minuscules

    if op == "s":
        print(f"La suma de {num1}+{num2} és: {float(num1)+float(num2)}")

    elif op == "r":
        print(f"La resta de {num1}-{num2} és: {float(num1)-float(num2)}")

    elif op == "m":
        print(f"La multiplicació de {num1}*{num2} és: {float(num1)*float(num2)}")

    elif op == "d":
        print(f"La divisió de {num1}/{num2} és: {float(num1)/float(num2)}")

    elif op == "e":
        print(f"El resultat de {num1}**{num2} és: {float(num1)**float(num2)}")

    elif op == "a":
        print(f"La arrel quadrada de {num1} i de {num2} és: {float(num1)**0.5} i {float(num2)**0.5}")

    else:
        print("Ho sento aquesta opció no és correcta")

        while True:
            op = input("""
            Indica quina operació vols realitzar?
            S/s || Suma
            R/r || Resta
            M/m || Multiplicació
            D/d || Divisió
            E/e || Exponent
            A/a || Arrel quadrada
            """)

            op = op.lower()

            if op == "s":
                print(f"La suma de {num1}+{num2} és: {float(num1)+float(num2)}")
                break

            elif op == "r":
                print(f"La resta de {num1}-{num2} és: {float(num1)-float(num2)}")
                break

            elif op == "m":
                print(f"La multiplicació de {num1}*{num2} és: {float(num1)*float(num2)}")
                break

            elif op == "d":
                print(f"La divisió de {num1}/{num2} és: {float(num1)/float(num2)}")
                break

            elif op == "e":
                print(f"El resultat de {num1}**{num2} és: {float(num1)**float(num2)}")
                break

            elif op == "a":
                print(f"La arrel quadrada de {num1} i de {num2} és: {float(num1)**0.5} i {float(num2)**0.5} consecutivament")
                break

            else:
                print("Ho sento aquesta opció no és correcta")
                continue
while True:
    print("""
    |------------------------------|
       Benvingut a la calculadora
    |------------------------------|
    """)
    time.sleep(1)
    print()
    num1 = input("Introdueix el primer nombre: ")
    num2 = input("Introdueix el segon nombre: ")

    options(num1, num2)
    print()
    time.sleep(1)
    num3 = input("Introdueix el tercer nombre: ")
    num4 = input("Introdueix el quart nombre: ")

    options(num3, num4)

    nums = [num1, num2, num3, num4]
    validation(nums)

    sn = input("Vols fer una altra operació? S(i) o N(o)")
    sn = sn.lower()
    if sn == "s":
        continue
    elif sn == "n":
        print("Adeu fins la propera")
        break
    else:
        break