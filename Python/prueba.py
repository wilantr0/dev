cumpleaños = input("Introdueix el teu aniversari amb aquest format, dd/m ").split('/')
cumpleaños1 = input("Introdueix l'aniversari d'un amic amb aquest format, dd/m ").split('/')
cumpleaños2 = input("Introdueix l'aniversari d'un altre amic amb aquest format, dd/m ").split('/')

if cumpleaños[1] > cumpleaños1[1] and cumpleaños[1] > cumpleaños2[1]:
    print('Mateu és el més gran')
    
elif cumpleaños1[1] > cumpleaños[1] and cumpleaños1[1]>cumpleaños2[1]:
    print('Guillermo és el més gran')

elif cumpleaños2[1] > cumpleaños[1] and cumpleaños2[1]>cumpleaños1[1]:
    print('Carles és el més gran')

elif cumpleaños[1] == cumpleaños1[1] or cumpleaños[1] == cumpleaños2[1] or cumpleaños1[1] == cumpleaños2[1]:
    print('Hi ha dos que són del mateix més')
else:
    print('Sabia que arribarieu a trencar-me el codi')
