""" 
Сортировка списка: Реализуйте алгоритм сортировки списка 
(например, сортировка пузырьком или быстрая сортировка) без использования стандартных функций сортировки.

"""
m = []
import random

for i in range(random.randint(1, 10)):
    m.append(random.randint(-10, 10))
print(f"Сгенерирован список {m}")


for i in range(len(m)):
    for j in range(len(m)-i-1):
        if m[j] > m[j+1]:
             m[j], m[j+1] = m[j+1], m[j]
            
print(f"Отсортированный список: {m}")

