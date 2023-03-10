"""
39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
Затем число M - количество элементов во втором массиве. Затем элементы второго массива
"""
# from random import randint
#
# n = int(input("Введите количество элементов первого массива: "))
# a = []
# for i in range(n):
#     a.append(randint(0, 100))
# print(a)
#
# m = int(input("Введите количество элементов второго массива: "))
# b = set()
# for i in range(m):
#     b.add(randint(0, 100))
# print(b)
#
# for x in a:
#     if x not in b:
#         print(x, end=' ')

"""
Дан массив, состоящий из целых чисел. 
Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, 
оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве 
Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

Получение и заполнение массива - в файл1
поиск кол-ва элементов - в файл2
"""

# from functions import count_neighbors as C_N
#
# def input_array():
#     n = int(input("Введите количество элементов в массиве: "))
#     arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
#     return arr
#
# arr = input_array()
# count = C_N(arr)
# print("Количество элементов, у которых два соседних и оба соседних элемента меньше данного: ", count)

"""
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) 
равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
 
Сумма делителей n не включая n = m
Сумма делителей m не включая m = n

По данному числу k выведите все пары дружественных чисел,
 каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 10^5. 
Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, 
разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
"""
# def divisor_sum(n):
#     """Вычисляет сумму делителей числа n (исключая само n)."""
#     return sum(i for i in range(1, n) if n % i == 0)
#
# def find_amicable_numbers(k):
#     """Находит все пары дружественных чисел не превосходящих k."""
#     result = set()
#     for n in range(1, k+1):
#         m = divisor_sum(n)
#         if m != n and divisor_sum(m) == n and m <= k:
#             result.add(tuple(sorted((n, m))))
#     return sorted(result)
#
# # Пример использования:
# k = 10000
# pairs = find_amicable_numbers(k)
# for pair in pairs:
#     print(pair[0], pair[1])

# def SumOfDividers(x):
#     sum = 0
#     for i in range(1, x // 2 + 1):
#         if x % i == 0:
#             sum += i
#     return sum
#
#
# k = (int(input('Введите: ')))
#
# for n in range(k):
#
#     j = SumOfDividers(n)
#
#     if n < j and n < k and n == SumOfDividers(j):
#         print(n, j)