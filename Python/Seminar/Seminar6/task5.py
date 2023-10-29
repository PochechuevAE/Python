""" 
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes

"""
import random

def check_simple(num: int, devisor: int):
    if num % devisor == 0:
        return False
    if devisor ^ 2 > num:
        return True
    return check_simple(num, devisor + 1)


num = random.randint(0, 10)

print(f"Дано число {num}, сейчас проверим, является ли оно простыи")
print(check_simple(num, 2))
