"""  
Угадай число: Создайте игру, в которой компьютер загадывает случайное число от 1 до 100, 
а игрок должен угадать его, получая подсказки (больше/меньше).

"""

import random

def guess_the_number():
    # Генерируем случайное число от 1 до 100
    secret_number = random.randint(1, 100)

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать его.")

    attempts = 0  # Для подсчета попыток

    while True:
        try:
            guess = int(input("Ваш вариант: "))
            attempts += 1  # Увеличиваем счетчик попыток

            if guess < secret_number:
                print("Загаданное число больше.")
            elif guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} с {attempts} попытки.")
                break  # Выходим из цикла, игра завершена
        except ValueError:
            print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    guess_the_number()
    