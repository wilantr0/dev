def options():
    op = input("""
    Indica quina operació vols realitzar?/n
    S/s || Suma\n
    R/r || Resta\n
    M/m || Multiplicació\n
    D/d || Divisió\n
    E/e || Exponent\n
    A/a || Arrel quadrada\n

    """)

    op = op.lower()
    return op

def operations(op, num1, num2):
    if op == "s":
        print(f"La suma de {num1}+{num2} és: {int(num1)+int(num2)}")
    elif op == "r":
        print(f"La resta de {num1}-{num2} és: {int(num1)-int(num2)}")
    elif op == "m":
        print(f"La multiplicació de {num1}*{num2} és: {int(num1)*int(num2)}")
    elif op == "d":
        print(f"La divisió de {num1}/{num2} és: {int(num1)/int(num2)}")
    elif op == "r":
        print(f"El resultat de {num1}**{num2} és: {int(num1)**int(num2)}")
    elif op == "r":
        print(f"La arrel quadrada de {num1} i de {num2} és: {int(num1)**0.5} i {int(num2)**0.5}")
    else:
        print("Ho sento aquesta opció no és correcta")
        options()
def validation(valores):
    if valores == 3:
        pass

    return range
while True:
    print()
    num1 = input("Introdueix el primer nombre: ")
    num2 = input("Introdueix el segon nombre: ")

    op = options()
    operations(op, num1, num2)

    num3 = input("Introdueix el tercer nombre: ")
    num4 = input("Introdueix el quart nombre: ")

    op = options()
    operations(op, num3, num4)

    valores = [num1, num2, num3, num4]

