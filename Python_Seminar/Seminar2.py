"""
n = int(input())
flag = True
while flag:
    print(n)
    n -= 1
    if n == 0:
        flag = False
else:
    print(100)
"""
"""
stroka = "Vsem privet!"
print(stroka[::-1])
"""
"""
n = int(input("Введите значение n: "))
result = 1
i = 1

while i <= n:
    result *= i
    i += 1

print("Значение n! равно", result)
"""
"""
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, 
выведите число -1.
"""
"""
n = int(input())

prev_num = 0
current_num = 1
temp = None
count = 0
while current_num <= n:
    temp = prev_num
    prev_num = current_num + prev_num
    current_num = temp
    count += 1
    if n == current_num:
        print(count)
        break
else:
    print ("Число не является числом Фибонначи")
"""
"""
Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это 
самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, 
а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, 
сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который 
среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, 
помогающую синоптикам в работе.

Дано число дней N, ввести температуру и посчитать сколько дней подряд максимально было "+"

N = 7

2
3
-1
4
5
6
-6

Ответ 3
"""
"""
n = int(input("Введите количество дней: "))
max_days = 0
current_days = 0
i = 0

while i < n:
    temp = int(input("Введите среднесуточную температуру: "))
    if temp > 0:
        current_days += 1
        if current_days > max_days:
            max_days = current_days
    else:
        current_days = 0
    i += 1

print(f"Самая длинная оттепель длилась дней - {max_days}.")
"""
# n - число арбузов
# найти минимум и максимум веса

n = int(input("Введите количество арбузов: "))
max = 0
min = 10000000
for i in range(n):
    ves_arbyz = int(input("Введите вес арбуза: "))
    if ves_arbyz < min:
        min = ves_arbyz
    if ves_arbyz > max:
        max = ves_arbyz
print(max, min)

