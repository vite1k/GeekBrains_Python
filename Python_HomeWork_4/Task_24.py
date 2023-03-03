"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
"""
n = int(input())  # количество кустов на грядке
a = list(map(int, input().split()))  # урожайность ягод на каждом кусте

max_berries = 0  # переменная для хранения максимального количества ягод

for i in range(n):
    berries = a[i] + a[(i+1)%n] + a[(i-1+n)%n]  # сумма ягод на текущем кусте и двух соседних
    max_berries = max(max_berries, berries)  # выбираем максимальное количество ягод

print(max_berries)  # выводим максимальное количество ягод
