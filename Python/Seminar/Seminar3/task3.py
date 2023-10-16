"""
Задача №11. Решение в группах
Дано натуральное число f > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=f. Если А не
является числом Фибоначчи, выведите число -1.

Input: 5
Output: 6
"""
"""
def find_fibonacci_index(f):
    a, b = 0, 1  # Первые два числа Фибоначчи
    n = 2  # Начинаем с третьего числа (индекс 2)

    while b < f:
        a, b = b, a + b
        n += 1

    if b == f:
        return n
    else:
        return -1

# Пример использования:
f = int(input("Введите натуральное число f: "))
result = find_fibonacci_index(f)

if result != -1:
    print(f"Число f является {result}-м числом Фибоначчи.")
else:
    print("Число f не является числом Фибоначчи.")

"""

f = int(input("Введите натуральное число f: "))

first, second = 0, 1  # Первые два числа Фибоначчи
current = 1 
n = 1 

while current < f:
    current = first + second
    # first, second = second, first + second
    second = first
    first = current
    n += 1

if current == f:
    print(n)
else:
    print(-1)
    
