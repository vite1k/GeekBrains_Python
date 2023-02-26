"""
Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*

385916 -> yes
123456 -> no
"""

num = input("Введите номер билета: ")

# Проверяем, что номер состоит ровно из 6 цифр
if len(num) != 6 or not num.isdigit():
    print("Ошибка: номер билета должен состоять ровно из 6 цифр")
else:
    # Вычисляем суммы первых и последних трех цифр
    first_half_sum = int(num[0]) + int(num[1]) + int(num[2])
    second_half_sum = int(num[3]) + int(num[4]) + int(num[5])

    # Проверяем, равны ли суммы первых и последних трех цифр
    if first_half_sum == second_half_sum:
        print("Да, билет счастливый!")
    else:
        print("Нет, билет несчастливый :(")