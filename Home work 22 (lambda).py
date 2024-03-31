#Написать функцию, которая принимает один аргумент, который в дальнейшем будет
#умножаться на заданное число.

def func_compute(n):
    return lambda x: x * n
result = func_compute(2)
print(result(15)) #30
print(result(20))

#Написать программу в которой с помощью функции sorted() и lambda
#функции отсортировать слова в списке по их 2 -й букве
l = ['here', 'will', 'be', 'some', 'lambda', 'sorting', 'function']
print(l)
res = sorted(l, key = lambda i: i[1]) #i очередной эллемент последовательности
print(res)

#Написать программу проверяющую начинается ли заданная строка с заданного символа,
#с помощью lambda функции

starts_with = lambda s: True if s.startswith('P') else False
print(starts_with('Python'))
print(starts_with('Java'))

#проверяемая буква также передается как параметр
def starts_with(letter):
    return lambda s: True if s.startswith(letter) else False
res = starts_with('A')
print(res('Antony'))

# Дан списоок слов. Отфильтровать список с использованием Lambda функции
#оставив в нем только слова палиндромы

words = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
res = list(filter(lambda word: word == word[::-1], words))
print(res)

#Дан список чисел. Использую lambda - функцию возведите в квадрат и в куб все элементы данного списка
nums =[3, 5, 7, 8, 9, 6]
square_nums = list(map(lambda i: i**2, nums))
cube_nums = list(map(lambda i: i**3, nums))
print(square_nums)
print(cube_nums)

#Используя функцию sorted() и lambda-функцию, отсортируйте список кортежей по последнему символу их второго элемента.
k = [('Магазин', 'railway_fork'), ('Игры', 'games'), ('Информация о боте', 'menu_item'),
 ('Пополнить счет', 'info')]
k_sorted = list(sorted(k, key = lambda i: i[1][-1], reverse = False))
print(k_sorted)

#Написать программу, сортирующую список словарей по значению
# некоторого общего ключа  с помощью lambda-функции (например, список сотрудников по их возрасту).

dictionary = [{"name": "Tom", "age": 10}, {"name": "Mark", "age": 5}, {"name": "Pam", "age": 7}]
sort_dict = list(sorted(dictionary,  key=lambda x: x['age']))
print(sort_dict)

#Напишите программу, которая будет считать количество четных и нечетных чисел в заданном списке с помощью lambda-функции.
numbers = [1, 2, 3, 4, 5, 6, 7, 7, 9, 10]
count_even = sum(map(lambda even: even%2 == 0, numbers))
count_noteven = sum(map(lambda noteven: noteven%2 != 0, numbers))
print('Count even: ', count_even)
print('Count noteven: ', count_noteven)

#Напишите программу, которая будет складывать соответствующие элементы заданных
# списков чисел с помощью функции map и lambda-функции. Например: для списков
# [1, 2, 3] и [4, 5, 6] результатом будет [5, 7, 9].
one = [1, 8, 3]
two = [4, 5, 6]
r = list(map(lambda x: x[0] + x[1], zip(one, two)))
print(r)