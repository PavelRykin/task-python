# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

import string

number = input('Введите вещественное число: ')
result = []
for i in number:
    if i != '.':
        result += i

result2 = 0

for i in result:
    result2 += int(i)

print(result2)
