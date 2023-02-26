"""
Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""

n = int(input("n = "))
m = int(input("m = "))
k = int(input("k = "))
# Проверяем, что k не больше, чем общее количество долек шоколадки
if k > n * m:
    print("no")
else:
    # Проверяем, что k делится нацело на n или m (т.е. можно разломить шоколадку на две части)
    if k % n == 0 or k % m == 0:
        print("yes")
    else:
        print("no")