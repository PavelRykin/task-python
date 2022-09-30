# Реализуйте алгоритм перемешивания списка.

from random import randint
import random


print('Давайте создадим список!')
count = int(input('Сколько элементов вы хотите добавить в список? '))
list = []
for i in range(count):
    list.append(randint(0, 10))
print('Вот получившийся сгенерированный список', end="\n")
print(list)
random.shuffle(list)
print('Вот получившийся перемешанный список', end="\n")
print(list)
