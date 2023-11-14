""" 
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива

"""

import random

# def check_numbers(firstArray, secondArray):
    

m = random.randint(1,10)
n = random.randint(1, 10)
print(sp1 := [random.randint(0, 10) for i in range(m)])
print(sp2 := [random.randint(0, 10) for i in range(n)])

result = []
for item in sp1:
    if item not in set(sp2):
        result.append(item)
        
print(result)

print([item for item in sp1 if item not in set(sp2)])



