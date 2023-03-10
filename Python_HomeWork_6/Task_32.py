"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
def find_indexes(lst, min_value, max_value):
    indexes = []
    for i in range(len(lst)):
        if min_value <= lst[i] <= max_value:
            indexes.append(i)
    return indexes

# Ввод массива, минимального и максимального значения пользователем
my_list = input("Введите элементы массива через пробел: ").split()
my_list = [int(i) for i in my_list]
min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))

# Поиск индексов элементов, которые находятся в заданном диапазоне
result_indexes = find_indexes(my_list, min_value, max_value)

# Вывод результата на экран
print(result_indexes)
