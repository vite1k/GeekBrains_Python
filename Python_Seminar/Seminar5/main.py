"""
Требуется найти N-е число Фибоначчи
"""
"""
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Введите номер числа Фибоначчи: "))
fib = fibonacci(n)
print("Число Фибоначчи под номером", n, "равно", fib)
"""
"""
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
"""
"""
def replace_grades(grades):
    min_grade = min(grades)
    max_grade = max(grades)
    new_grades = []
    for grade in grades:
        if grade == max_grade:
            new_grades.append(min_grade)
        else:
            new_grades.append(grade)
    return new_grades


n = int(input("Введите количество оценок: "))
grades = []
for i in range(n):
    grade = int(input("Введите оценку: "))
    grades.append(grade)

grades = replace_grades(grades)
print(grades)
"""
"""
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
"""
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
num = int(input("Введите число: "))
if is_prime(num):
    print(num, "является простым числом")
else:
    print(num, "не является простым числом")
"""
def reverse_sequence(n):
    if n == 0:
        return
    element = int(input())
    reverse_sequence(n-1)
    print(element)

n = int(input("Введите длину последовательности: "))
print("Введите последовательность:")
reverse_sequence(n)
