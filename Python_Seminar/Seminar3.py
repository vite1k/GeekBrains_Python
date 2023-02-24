"""
Дан список чисел. Определите, сколько в нем встречается различных чисел.
"""
"""
spisok = [1, 1, 2, 0, -1, 3, 4, 4]
unique_count = 0
list = []
for number in spisok:
    if number not in list:
        unique_count += 1
        list.append(number)

print(unique_count) 
"""
"""
numbers = [1, 1, 2, 0, -1, 3, 4, 4]
list = len(set(numbers))
print(list)
"""
"""
Задача No19. Решение в группах
Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3 
Output: [4, 5, 1, 2, 3]
"""
"""
spisok = [1, 2, 3, 4, 5, 6, 7]
k = int(input("Введите на сколько нужно сдвинуть элементы вправо: "))
n = len(spisok)
shift_index = k % n
for i in range(shift_index):
    last = spisok[-1]
    for j in range(n - 1, 0, -1):
        spisok[j] = spisok[j - 1]
    spisok[0] = last
print(spisok)
"""
"""
Задача No21. Решение в группах
Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
"""
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
unique_values = set()

for item in data:
    for value in item.values():
        unique_values.add(value.strip())

print(unique_values)
"""

array = [1, 4, 3, 4]
count = 0

for i in range(1, len(array)):
    if array[i] > array[i - 1]:
        count += 1

print(count)
