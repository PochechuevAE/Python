"""

list_1 = [] # Создание пустого списка
list_2 = list () # Создание пустого списка
list_1 = [7, 9, 11, 13, 15, 17] # Создание заполненого списка

print(list_1[0]) # [7] нумерация с нуля -1 - нумерация будет с конца
print(*list_1) # 7 но не в скобках

for i in list_1:
    print(i) # поочередно выводит каждый элемент списка

print(len(list_1)) # выводит кол-во элементов списка

list_1 = [1, 5]
print(list_1)
list_1.append(8) # Добавляет указаный элемент в конец списка
print(list_1)
list_1.append(85)
print(list_1)

list_1 = []
print(list_1)
for i in range(5): # Переменная i принимает значения от 0 до 4
    list_1.append(i) # при каждой итерации добавляет в список значение i
    print(list_1)
    
"""
# Удаление последнего элемента списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# print(list_1.pop()) # удалит 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # удалит 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # удалит -1
# print(list_1) # [12, 7]

# Удаление конкретного элемента
# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# print(list_1.pop(0)) # Удалить 0 элемент => 12
# print(list_1) # [7, -1, 21, 0]

# Добавление элемента на нудную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# print(list_1.insert(2, 11)) # добавит 11 на 2 позицию
# print(list_1)

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])                        # 1
# print(list_1[1])                        # 2
# print(list_1[len(list_1)-1])            # 10
# print(list_1[-1])                       # 10
# print(list_1[-5])                       # 6
# print(list_1[:])                        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])                       # [1, 2]
# print(list_1[len(list_1)-2:])           # [9, 10]
# print(list_1[2:9])                      # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[5:-18])                    # []
# print(list_1[0:len(list_1):6])          # [1, 7]
# print(list_1[::6])                      # [1, 7]

""" 
**************************************************
Кортэж - это неизменяемый список. Юзается в случае защиты каких - либо данных 
от изменений (намеренных или случайных). Кортэж занимает меньше места в памяти и работает быстрее, по сравнению со списком.
**************************************************
"""
# t = () # Создание пустого кортэжа
# print(type(t)) # class <'tuple'>
# t = (1, ) # class <'tuple'>
# print(type(t))
# t = (1) # class <'int'> не кортэж
# print(type(t))
# t = (19, 5, 1990)
# print(type(t))

# v = [1, 8, 9] # Создан список
# print(v)
# print(type(v))  

# v = tuple(v) # Список преобразован в кортэж
# print(type(v)) 
# print(v)

# a, b, c = v # множественное присваивание a = 1, b = 2 => a, b = 1, 2 || a = 1, b = 1 => a = b =1 
# print(a, b, c)

# t = (1, 2, 3, 4, 5,)
# # print(t[1])
# for i in t:
#     print(i)
# print()

# for i in range(len(t)):
#     print(t[i])
# print()

# t[0] = 2 # ошибка, ибо tuple не поддерживает изменение аргументов

""" 
*************************************
Словари - отличие от списка в том, что в списке юзают индекс элемента в качестве ключа, а в словаре
юзают (строка, число) для обозначения элемента
*************************************
"""
# dictionary = {} 
# dictionary = {'up': 'w', 'left': 'a', 'down': 's', 'right': 'd'}
# print(dictionary)            # {'up': 'w', 'left': 'a', 'down': 's', 'right': 'd'}
# print(dictionary['left'])    # a
# print(dictionary['up'])      # w
# dictionary['left'] = 'A'     # замена элемента 'left'
# print(dictionary['left'])    # A
# # print(dictionary['type'])  # KeyError: 'type' нет такого ключа
# del dictionary['left']       # Удаление элемента
# print(dictionary)
# for item in dictionary:
#     print(item)
#     print('{}: {}'.format(item, dictionary[item]))

# d = {} # || d = dict() - создали пустой словарь
# d['q'] = 'qwerty'
# print(d)
# d['w'] = 'werty'
# print(d)
# print(d['q'])
# print(d['w'])

""" 
*************************************
Множества - содержат в себе уникальные элементы, не обязательно упорядоченные.
Может содержать в себе значения любых типов. Множества можно объединять, пересечение, разность
*************************************
"""
# colors = {'red', 'green', 'blue'}
# print(colors)                        # {'red', 'green', 'blue'}
# colors.add('red') # не добавит, т.к red уже есть
# print(colors)                        # {'red', 'green', 'blue'}
# colors.add('gray') # добавит в рандомное место
# print(colors)                        # {'red', 'gray', 'green', 'blue'}
# colors.remove('red')
# print(colors)                        # {'blue', 'green', 'gray'}
# # colors.remove('red')               # KeyError: 'red'
# # print(colors)     
# colors.discard('red')                # проверяет, есть ли значение, если есть - удаляет, если нет - ок
# colors.clear()                       # {}
# print(colors)                        # set()
# q = set()                            # создали пустое множество

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                           # копируем множество в переменную с
# print(c)                               # c = {1, 2, 3, 5, 8}
# u = a.union(b)                         # объединяем а в b (все не уникальные)
# print(u)                               # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)                  # пересечение (те элементы, которые есть в обоих множ)
# print(i)                               # i = {8, 2, 5}
# d1 = a.difference(b)                   # разность (берем а и вычитаем все, что есть в b) и выводим, что осталось
# print(d1)                              # d1 = {1, 3}
# dr = b.difference(a)                   # разность (берем b и вычитаем все, что есть в a) и выводим, что осталось
# print(dr)                              # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))
# print(q)                               # q = {1, 21, 3, 13}

# a = {1, 8, 6}
# b = frozenset(a)                         # замороженое множество => не изменяемое
# print(b)                                 # frozenset({8, 1, 6})

