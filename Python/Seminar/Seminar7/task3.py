""" 
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.


"""

import random

print(sp := [random.randint(1, 10) for i in range(random.randint(1, 10))])
# sp = [1, 2, 3, 4, 5]
result = 0
for i in range(len(sp)):
    # print(sp[i - 1], sp[i], sp[(i+1) % len(sp)])
    if sp[i] > sp[(i+1) % len(sp)] and sp[i] > sp[i-1]:
        result += 1

print(result)
print(sum([1 for i in range(len(sp)) if sp[i] > sp[(i+1) % len(sp)] and sp[i] > sp[i-1]]))
print([1 if sp[i] > sp[(i+1) % len(sp)] and sp[i] > sp[i-1] else 0 for i in range(len(sp))])
