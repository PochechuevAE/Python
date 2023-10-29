""" 
Задача на строки: Напишите функцию, которая проверяет,
является ли заданная строка палиндромом (читается одинаково слева направо и справа налево). "A роза упала на лапу Азора"
"""

a = "А роза упала на лапу Азора"
a = a.lower()
forbidden = ('.','?','!',':',';','-','—',' ',)
for symbol in forbidden: 
    if symbol in a: 
        a = a.replace(symbol, "")
b = a[::-1]        
if a == b:
    print("Строка палиндром")
else:
    print("Строка не палиндром") 
