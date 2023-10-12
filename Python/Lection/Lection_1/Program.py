# print(5, 8, 6) # функция вывода на экран

# n = 10 # Задать переменную любого типа
# print(n)
# x = None # неизвестное значение
# print(x)
# y = 1.89
# print(y)
# y = 'fdsf'
# print(y)
# y1 = "sdasd"
# print(type(y)) # Выводит тип переменной на экран

# b = 's"d\'a"f' # Знак "\" а после него ' выводит кавычку в строеке либо просто юзаем ""
# print(b)
# """ # три апострофа это многострочный комментарий
# print(5)
# #print(5, 8)
# print(5, 9)
# print(5)
# """
# # print(5, 8) Нажать Ctrl+K затем Ctrl+C
# # print(5, 9)
# # print(5)

# # Интерпаляция
# a = 5
# b = 5.89
# c = 'Yes'

# print(a,' - ', b, ' - ', c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a, b, c))

# Ввод данных
# print('Введите первое число')
# a = int(input())
# b = int(input('Введите второе число: '))
# print(a, ' + ', b, ' = ', a + b)

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# Округление чисел
# a = 5.4324
# b = 6.446746
# print(a*b)
# print(round(a*b, 3))

# Сокращенное присваивание
#i++
# iter = 2
# iter += 3 # iter = iter + 3 сложение
# iter -= 4 # iter = iter - 4 вычитание
# iter *= 5 # iter = iter * 5 умножение
# iter /= 6 # iter = iter / 6 деление с остатком
# iter //= 7 # iter = iter // 7 деление целое
# iter %= 8 # iter = iter % 8 остаток от деления
# iter **= 9 # iter = iter ** 9 возведение в степень

# Логические операции
# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
#a = 1 == 2
#print(a)
# a = 1 != 2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 3 < 5 < 10
# print(a)

# if и if-else
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура! Это же МАША')
# elif username == 'Марина':
#     print('Я так ждал тебя Марина')
# elif username == 'Алексей':
#     print('Лёха рулит')
# elif username == 'Катя':
#     print('Я люблю тебя, Катушка')
# else:
#     print('Привет, ', username)

# while
# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i = i + 1
# else:
#     print('Пожалуй ')
#     print('хватит ')
# print(i)

# Метод флага лучше брэйка
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток от деления числа n на число i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: #делитель числа не может превышать введенное число делимое на 2
#         print(n)
#         flag = False
#     i += 1
