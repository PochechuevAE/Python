# """ 
# Парольный генератор: Создайте программу, которая генерирует случайные пароли заданной длины,
# учитывая разные типы символов (буквы, цифры, специальные символы).

# """
# lengthOfpass = 0
# import random

# alphabet = [chr(i) for i in range(97, 123)]
# alphabetA = [chr(i) for i in range(65, 91)]

    
# def generatPass():
#     while True:   
#         try:
#             lengthOfpass = int(input("Введите длинну пароля: "))
#             if lengthOfpass < 30:
#                 print("Начинаем генерацию: ")
#                 print()
#                 password = []
#                 for i in range(0, lengthOfpass):
#                     password.append(random.randint(0, 10))
#                 for index, x in enumerate(password):
#                     if random.randint(0, 1):
#                         password[index] = random.choice(alphabet)                           
#                 for index, x in enumerate(password):
#                     if random.random() < 1/10:
#                         password[index] = random.choice(alphabetA)
#                 for index, x in enumerate(password):
#                     if random.random() < 1/10:
#                         password[index] = random.choice(['*', '#', '-', '%'])
#                 print("Ваш пароль: ")
#                 print(*password, sep="")
#                 print()
#                 break
#         except ValueError:
#             print("Пожалуйста, введите целое число.")
        
# if __name__ == "__main__":
#     generatPass()

import random
import string

def generate_password(length=12):
    # Определите символы, которые будут использоваться для генерации пароля
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Составьте строку, содержащую все возможные символы для пароля
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Генерируйте пароль, выбирая случайные символы из общего списка
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

if __name__ == "__main__":
    password_length = int(input("Введите длину пароля: "))
    password = generate_password(password_length)
    print(f"Сгенерированный пароль: {password}")
