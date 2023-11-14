""" 
Функция enumerate применяется к итерируему объекту и возвращает новый итератор с кортежами из индекса 
и элементов входных данных.

enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]

Функция enumerate позволяет пронумеровать набор данных

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3')]
"""
users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)