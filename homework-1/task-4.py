# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат #точек в этой четверти (x и y).

quarter = int(input('Введите номер чертверти: '))

if quarter < 1 or quarter > 4:
    print('Введите одну из 4 четвертей!')
elif quarter == 1:
    print('this x>0 and y>0')
elif quarter == 2:
    print('this x<0 and y>0')
elif quarter == 3:
    print('this x<0 and y<0')
elif quarter == 4:
    print('this x>0 and y<0')
