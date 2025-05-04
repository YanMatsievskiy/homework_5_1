'''Задача 1. Список имён'''

name = input('Введите строку из имен, разделенных пробелами: ')
names = list(name.split())
names_lexic = sorted(names)
print('Список имен в лексикографическом порядке:')
print(names_lexic)
