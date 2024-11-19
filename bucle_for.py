numero = int(input('ingrese un numero: '))
for i in range(1, 10000):
    if i == numero:
        print(' su numero existe entre el 1 y el 10000')
    else:
        print('su numero no existe en 10000')
        break