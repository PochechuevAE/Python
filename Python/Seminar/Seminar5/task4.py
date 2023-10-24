""" 
Пользователь вводит натуральное k.
Надо сформировать многочлен такой степени, 
где все коэффициенты случайные от -10 до 10.

например, k=2 -> -x^2 + 3*x - 8 = 0
тут коэффициенты -1, 3, -8
например, k=3 -> 3*x^3 - 2*x = 0
тут коэффициенты 3, 0, -2, 0

"""

import random

def polynomial (k: int):
    coeff = [random.randint(-10,10) for _ in range(k+1)]
    output_str = "" 
    for i in range(len(coeff)):
        if i==0 and abs(coeff[0]) == 1:
            if coeff[0] > 0:
                output_str += f"x^{k-i} + "
            else:
                output_str += f"-x^{k-i} + "
        elif coeff[i] != 0:
                        
            output_str += f"{coeff[i]}*x^{k-i} + "
    return output_str.replace('+ -', '- ').replace('*x^0', '').replace('x^1 ', 'x ').replace(' 1*', ' ')[:-3] + " = 0"



k = int(input("Введите кол-во коэфициентов"))
print(polynomial(k))
    