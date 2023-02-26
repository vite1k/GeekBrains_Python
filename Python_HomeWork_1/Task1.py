"""
Задача 1: Найдите сумму цифр трехзначного числа.
*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

num = int(input("Введите трехзначное число: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num //= 10

print("Сумма цифр трехзначного числа:", sum)