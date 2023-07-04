# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии
# Каждое число вводится с новой строки.

def cerat_arr(arr1, multiplier, quantity):
    progressive = [arr1 + (i - 1) * multiplier for i in range(1, quantity + 1)]
    return progressive

quantity = int(input('Введите колличество элементов списка = '))
arr1 = int(input('Введите первый элемент списка = '))
multiplier = int(input('Введите множетель для арифметической прогрессии = '))

list_1 = cerat_arr(arr1, multiplier, quantity)

print(f'Ваш список арифметической прогрессии {list_1}')

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

import random

def serch_index(arr, min, max):
    list_1 = []
    for i in range(len(arr)):
        if max >= arr[i] >= min:
            list_1.append(i)
    return list_1


num = int(input('Введите колличество элементов списка = '))
n_min = int(input('Введите минимальное значение списка = '))
n_max = int(input('Введите максимальное значение списка = '))

arr_list = [random.randint(n_min, n_max) for i in range(num)]
print(*arr_list)

d_min = int(input('Введите минимум диапозона = '))
d_max = int(input('Введите максимум диапозона = '))

list_1 = serch_index(arr_list, d_min, d_max)

print(*list_1)