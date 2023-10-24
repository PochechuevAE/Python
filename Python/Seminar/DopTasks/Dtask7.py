""" 
Напишите программу, 
которая принимает строку от пользователя и подсчитывает, 
сколько раз каждый символ встречается в этой строке.
"""

def getLetersCount(some_str: str) -> str:
    d1 = {}
    for char in some_str:    
        if char.isspace():
            continue              
        if char in d1:
            d1[char] += 1        
        else:
            d1[char] = 1

    for letter, frequency in d1.items():
        print(f"'{letter}': {frequency} раз(a)")

test = input("Введите строку: ")
print(getLetersCount(test))