# на входе целое или вещественное число. Посчитать количество цифр этого числа

# 0,001 ->4
# 0 - > 1
# 100 -> 3
# number = float(input("Введите число: "))
# count = 0

number = float(input("Введите число: "))

# Находим целую часть числа
integer_part = int(number)
print(f"Целая часть числа: {integer_part}")
# Находим десятичную часть числа
decimal_part = abs(number - integer_part)
print(f"Десятичная часть числа: {decimal_part}")
# Инициализируем счетчики для целой и десятичной частей
count_integer = 0
count_decimal = 0

# Подсчет цифр в целой части
while integer_part > 0:
    integer_part //= 10
    count_integer += 1

# Подсчет цифр в десятичной части
while decimal_part > 0:
    decimal_part *= 10
    digit = int(decimal_part)
    count_decimal += 1
    decimal_part -= digit

# Вывод результата
print(f"Целая часть: {count_integer} цифр, Десятичная часть: {count_decimal} цифр")
print(f"В итоге в числе {count_integer + count_decimal} цифр")
#