# Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.

number = int(input('N = '))
result = [round((1 + 1 / i) ** i, 2) for i in range(1, number + 1)]
print(f'Последовательность: {result}\nСумма: {round(sum(result), 2)}')
