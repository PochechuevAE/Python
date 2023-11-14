""" 
В списке хранятся числа. нужно выбрать только четные числа и составить список пар (число, квадрат числа).
Пример: 
1 2 3 5 8 15 23 38
Получилось:
[(2, 4), (8, 64), (38, 1444)]
"""

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)

# itog = []
# for i in range(len(data)):
#     if data[i] % 2 == 0:
#         itog.append((data[i], data[i]**2))
# print(itog)

# print([(data[i], data[i]**2) for i in range(len(data)) if data[i] % 2 == 0])


# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)


