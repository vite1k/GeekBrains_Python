"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""

# Первый вариант (простой):
def exponentiation(a, b):
    if b == 0:
        return 1
    else:
        return a * exponentiation(a, b - 1)

# Второй вариант (более эффективный):
def recursive_power(a,b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        temp = recursive_power(a, b // 2)
        return temp * temp
    else:
        temp = recursive_power(a, (b - 1) // 2)
        return a * temp * temp

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print(f"{a} в степени {b} равно {exponentiation(a,b)}")
print(f"{a} в степени {b}, если решать через более эффективный метод равно {recursive_power(a,b)}")