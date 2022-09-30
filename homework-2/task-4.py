# Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2

from random import randint, random


questien = input('Запускаем программу? да или нет?))) ')

if questien == "нет" or questien == "no":
    exit()

size = int(input('Укажите, сколько должно быть позиций? '))
list = []
for i in range(0, size):
    list.append(randint(0, 10))
print(f'вот сгенерированные номера позиций: {list}')

number = int(input('Задайте N: '))
list2 = []
for i in range(number * 2 + 1):
    list2.append(-number + i)
print(f'Вот получившийся список -N до N {list2}')

sum = 0
for i in list:
    for j in list2:
        if i == list2.index(j):
            sum += j

print(
    f'Сумма чисел под сгенерированными индексами в получившимся списке равна: {sum}')
