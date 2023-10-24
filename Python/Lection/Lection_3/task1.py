# def sum_numbers(n, y = "Hello"):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa 
    
# a = sum_numbers(5, "qwewr")
# print(sum_numbers(5))   
# print(a)

# def sum_str(*args): # передаем неограниченое кол-во аргументов в функцию
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 'r'))
# print(sum_str('1', '8', '9'))

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n -1) + fib(n -2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)        