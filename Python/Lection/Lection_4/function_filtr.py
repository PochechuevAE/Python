data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data)) # Фильтрует список и возвращает только то, на что функция дала true
print(res)