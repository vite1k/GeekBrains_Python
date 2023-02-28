"""
Задача No25. Решение в группах
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.
"""
"""
stroka = input()
d={}
for i in stroka:
    d[i]= d.get (i,0)+1

for k,n in d.items():
    print (f'{k}_{n}')
"""
"""
string = input("Введите строку: ")
char_counts = {}

if len(string) == 0:
    print("Строка пуста.")
else:
    for i in string:
        if i in char_counts:
            char_counts[i] += 1
        else:
            char_counts[i] = 1

    result = []
    for i, count in char_counts.items():
        result.append(f"{i}_{count}")

    print(" ".join(result))
"""
"""
Пользователь вводит текст(строка).
Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. 
Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
Output: 13
"""
"""
text = input("Введите текст: ")
words = set(word.lower() for word in text.split())
num_unique_words = len(words)
print("Количество различных слов:", num_unique_words)
"""
"""
Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
“Задана последовательность неотрицательных целых чисел.
Требуется определить значение наибольшего элемента последовательности,
которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
"""

a = input("Введите последовательность чисел: ")
seq_list = a.split()

max_num = 0
for i in seq_list:
    if i == "0":
        break
    i = int(i)
    if i > max_num:
        max_num = i

print("Наибольший элемент последовательности:", max_num)


