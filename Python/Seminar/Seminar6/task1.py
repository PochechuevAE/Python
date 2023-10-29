# надо найти сумму всех чисел, от 1 до n, где n вводит пользователь

def summa_cikle(num):
    res = 0
    while True:
        if num == 0:
            break
        res += num
        num -= 1
    return res

def summa_rec(num):
    if num == 0:
        return 0
    return num + summa_cikle(num - 1)  

num = int(input("Введите число: "))
print(f"Сумма всех натуральных числе от 1 до {num} равна {summa_cikle(num)}")
print(f"Сумма всех натуральных числе от 1 до {num} по рекурсии равна {summa_rec(num)}")