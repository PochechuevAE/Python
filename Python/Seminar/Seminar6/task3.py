""" 
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21

"""

def fib(n):
    if n in [1,  2]:
        return n - 1 
    return fib(n - 1) + fib(n - 2)

def fib_summ(n):
    str = []
    for i in range(1, n + 1):
        str.append(fib(i))
    return str      
        
n = int(input("Введите номер элемента ряда фибоначи, которое хотите посмотреть: "))
print(f"{n} элемент последовательности Фибоначи равен {fib(n)}")
print(fib_summ(n))