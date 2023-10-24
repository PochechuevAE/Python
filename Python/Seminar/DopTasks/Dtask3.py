""" 
Сумма элементов списка: Напишите функцию, которая вычисляет сумму всех элементов рандомного списка.

"""
import random

m = []
for i in range(random.randint(1, 10)):
    m.append(random.randint(-10, 10))
print(f"Сгенерирован список {m}")

sum = sum(m)
print(f"Сумма элементов списка равна {sum}")

