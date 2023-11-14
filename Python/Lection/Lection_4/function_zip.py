""" 
Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов 
входных данных

zip([1, 2, 3], ['о','д','т'], ['f', 's', 't'])
[(1, 'о','f'), (2, 'д','s'), (3, 'т','t')]

На выходе получаем набор данных, состоящих из элементов соответствующих исходному набору.
"""
# Пример

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)
print('--------------------------------------------')
# Функция zip() пробегает по минимальному входящему набору данных
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)

