#reflex, pygame, psyculare, streamlead
numero = int(input('escriba un numero entero: '))
booleano = True
string = str(input('escriba cualquier cosa'))
flotante = float(input("escriba un numero decimal: "))
lista = []
lista.append(numero)
lista.append(booleano)
lista.append(string)
lista.append(flotante )
contador = 0
for i in lista:
    contador += 1 
    print(f'{contador}. {i}')