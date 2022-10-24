import time
def validation(range):
  while True:  
    rango = "-".join(range)
    print("Ara has d'escollir 3 dels 4 numeros dels que has fet servir")
    el1, el2, el3 = input(f"Aquestos són els nombres que pots fer servir[{rango}]: "). split(", ")
    time.sleep(0.5)
    print()
    if el1 > el3 and el2 > el3:
            print(f"{el3} és el numero més petit, per tant")
            print(f"{el1} i {el2} > {el3}")
            print()
            time.sleep(0.3)
            if el1 < el3 and el2 < el3:
                print(f"{el3} és el numero més gran, per tant")
                print(f"{el1} i {el2} < {el3}")
                break
            elif el1 < el2 and el3 < el2:
                print(f"{el2} és el numero més gran, per tant")
                print(f"{el1} i {el3} < {el2}")
                break
            elif el2 < el1 and el3 < el1:
                print(f"{el1} és el numero més gran, per tant")
                print(f"{el2} i {el3} < {el1}")
                break
    elif el1 > el2 and el3 > el2:
            print(f"{el2} és el numero més petit, per tant")
            print(f"{el1} i {el3} > {el2}")
            print()
            time.sleep(0.3)
            if el1 < el3 and el2 < el3:
                print(f"{el3} és el numero més gran, per tant")
                print(f"{el1} i {el2} < {el3}")
                break
            elif el1 < el2 and el3 < el2:
                print(f"{el2} és el numero més gran, per tant")
                print(f"{el1} i {el3} < {el2}")
                break
            elif el2 < el1 and el3 < el1:
                print(f"{el1} és el numero més gran, per tant")
                print(f"{el2} i {el3} < {el1}")
                break
    elif el2 > el1 and el3 > el1:
            print(f"{el1} és el numero més petit, per tant")
            print(f"{el2} i {el3} > {el1}")
            print()
            time.sleep(0.3)
            if el1 < el3 and el2 < el3:
                print(f"{el3} és el numero més gran, per tant")
                print(f"{el1} i {el2} < {el3}")
                break
            elif el1 < el2 and el3 < el2:
                print(f"{el2} és el numero més gran, per tant")
                print(f"{el1} i {el3} < {el2}")
                break
            elif el2 < el1 and el3 < el1:
                print(f"{el1} és el numero més gran, per tant")
                print(f"{el2} i {el3} < {el1}")
                break
    elif el1 == el2 or el2 == el1 and el1<el3:
            print(f"{el3} és el numero més gran, per tant")
            print(f"{el1} = {el2} < {el3} ")
            break
    elif el1 == el3 or el3 == el1 and el1<el2:
            print(f"{el2} és el numero més gran, per tant")
            print(f"{el1} = {el3} < {el2}")
            break
    elif el3 == el2 or el2 == el3 and el2<el2:
            print(f"{el1} és el numero més gran, per tant")
            print(f"{el2} = {el3} < {el1} ")
            break
    elif el1 and el2 and el3 not in range:
            print("Has d'escollir entre els numeros que has fet servir")
            time.sleep(0.5)
            continue

def options(num1, num2):
    op = input("""
    Indica quina operació vols realitzar?\n
    S/s || Suma\n
    R/r || Resta\n
    M/m || Multiplicació\n
    D/d || Divisió\n
    E/e || Exponent\n
    A/a || Arrel quadrada\n

    """)

    op = op.lower()

    if op == "s":
        print(f"La suma de {num1}+{num2} és: {int(num1)+int(num2)}")

    elif op == "r":
        print(f"La resta de {num1}-{num2} és: {int(num1)-int(num2)}")

    elif op == "m":
        print(f"La multiplicació de {num1}*{num2} és: {int(num1)*int(num2)}")

    elif op == "d":
        print(f"La divisió de {num1}/{num2} és: {int(num1)/int(num2)}")

    elif op == "e":
        print(f"El resultat de {num1}**{num2} és: {int(num1)**int(num2)}")

    elif op == "a":
        print(f"La arrel quadrada de {num1} i de {num2} és: {int(num1)**0.5} i {int(num2)**0.5}")

    else:
        print("Ho sento aquesta opció no és correcta")


def options1(num3, num4):
    while True:
        op = input("""
        Indica quina operació vols realitzar?\n
        S/s || Suma\n
        R/r || Resta\n
        M/m || Multiplicació\n
        D/d || Divisió\n
        E/e || Exponent\n
        A/a || Arrel quadrada\n

        """)

        op = op.lower()

        if op == "s":
            print(f"La suma de {num3}+{num4} és: {int(num3)+int(num4)}")
            break

        elif op == "r":
            print(f"La resta de {num3}-{num4} és: {int(num3)-int(num4)}")
            break

        elif op == "m":
            print(f"La multiplicació de {num3}*{num4} és: {int(num3)*int(num4)}")
            break

        elif op == "d":
            print(f"La divisió de {num3}/{num4} és: {int(num3)/int(num4)}")
            break

        elif op == "e":
            print(f"El resultat de {num3}**{num4} és: {int(num3)**int(num4)}")
            break

        elif op == "a":
            print(f"La arrel quadrada de {num3} i de {num4} és: {int(num3)**0.5} i {int(num4)**0.5}")
            break

        else:
            print("Ho sento aquesta opció no és correcta")
            continue
        
while True:
    print()
    num1 = input("Introdueix el primer nombre: ")
    num2 = input("Introdueix el segon nombre: ")

    options(num1, num2)
    

    num3 = input("Introdueix el tercer nombre: ")
    num4 = input("Introdueix el quart nombre: ")

    options1(num3, num4)

    nums = [num1, num2, num3, num4]
    validation(nums)