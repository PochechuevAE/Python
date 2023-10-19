# Создать список, состоящий из четных чисел в диапазоне от 1 до 100
# Решение:
list_1 = []
for i in range(1, 101):
    if i % 2 == 0:
        list_1.append(i)
print(list_1)

# а проще записать так
print()
list_2 = [i for i in range(1, 101) if i % 2 == 0]
print(list_2)

list_3 = [(i, i) for i in range(1, 101) if i % 2 == 0]
print("создали Кортэж:")
print(list_3)

list_4 = [i * 2 for i in range(10) if i % 2 == 0]
print("умножаем/вычитаем и прочее значения")
print(list_4)

list_5 = [(i, i * i) for i in range(10) if i % 2 == 0]
print("создали Кортэж: (i, квадрат i): ")
print(list_5)

