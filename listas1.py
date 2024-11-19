lista = []
contador = 0
while True:
    print('añadir un elemento a la lista (1), salir del programa (2)')
    accion = int(input('Que accion desea realizar? '))
    if accion == 1: 
        lista.append(input('añada un elemento a la lista: '))
        continue
    if accion == 2:
        break 
    else:
        print('esa entrada no es valida. ')
        continue
for i in lista:
    
    contador += 1
    print(f'{contador}. {i}')