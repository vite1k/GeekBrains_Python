# my_dict = {4: "four", "two":2, (1,2,3): 'Это кортеж'}
#
# storage = {'ананас': 4, 'киви': 4, 'банан': 4, 'арбуз': 5, "дыня": 8}
# delivery = {'ананас': 7, "арбуз": 10, "инжир": 7}
# print(storage)
# print(delivery)
#
# # storage.update(delivery)
# keys = set()
# for key in storage:
#     keys.add(key)
# for key in delivery:
#     keys.add(key)
#
# for key in keys:
#     storage[key] = storage.get(key, 0) + delivery.get(key, 0)
# def buy(name: str):
#     storage[name] = storage.get(name) - 1
# buy('банан')
# print(storage.get('ананас', 'Такого продукта у нас нет'))
# print(storage)
#
# for k, v in storage.items():
#     print(f'на складе {v} позиций товара "{k}')

# my_list = ['jkd', '32', 'jsj', '42', 'sddf', "42"]
# item = '42'
#
# for i in range(len(my_list)):
#     if item in my_list[i]:
#         print('yes!')
#         break
# else:
#     print('no')


item = input('введите искомое значение: ')

my_list = ['jkd', '32', 'jsj', '42', 'sddf', 'jkd', '42']

count = 0
for i in range(len(my_list)):
    if my_list[i] == item:
        count += 1

        if count == 2:
            print(f'В нашем списке искомое значение {item} второй раз появляется под индексом {i}')
            break
else:
    print('-1')
