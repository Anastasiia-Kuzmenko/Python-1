#Дана последовательность из N целых чисел. Сформировать последовательность,
# каждый элемент которой равен сумме цифр соответствующего элемента исходной
# последовательности. Найти сумму цифр в сформированной последовательности.
l = [18, 23, 35, 47, 57, 69, 79, 89, 97]
def digit_sum(n):
    s = 0
    while n>0:
        s += n%10
        n//=10
    return s
result = []
for elem in l:
    result.append(digit_sum(elem))
print('New: ', result)
s = 0
for elem in result:
    s += digit_sum(elem)
print('Sum elem in new: ', s)

#Вывести на экран последовательность из первых 100 простых чисел. Найти сумму элементов полученной последовательности.

count = 0 # счетчик первых простых чисел
res =  [] #будет храниться созданная последовательность


def is_prime(n):
    for i in range(2, n//2+1):
        if n%i ==0:
            return False #если число делится значит число составное
        return True
i = 2
while count<100:
    if is_prime(i):
        res.append(i)
        count +=1
    i += 1
print(res, len(res))
print(sum(res))

#Написать функцию, которая принимает в качестве аргумента строку
# и подсчитывает в ней количество символов в верхнем и нижнем регистре.
def str_count(s): # s строка которую будет принимать функция
    upper_num = 0
    lower_num = 0
    for char in s: #пишем проверку для нашей строки
         if char.isupper(): #если элемет с большой буквы то
             upper_num += 1 #добавляем этот элемент в наш счетчик
         elif char.islower():
             lower_num += 1
    return{'upper_num': upper_num, 'lower_num': lower_num} #возвращаем значения в виде словаря клю значение
print(str_count('FFFFijdwjhLL'))

#Написать функцию, которая выводит на экран первые N строк
# треугольника Паскаля. *Треугольник Паскаля - это бесконечная
# таблица чисел, имеющая форму треугольника, в котором на вершине
# и по бокам стоят единицы, а каждый центральный элемент равен сумме
# двух элементов, расположенных над ним.


def PrintPasTriangle(rows):
    row = [1]
    for i in range(rows):
        print(row)
        row = [sum(x) for x in zip([0] + row, row + [0])]


PrintPasTriangle(6)

def get_row(prev_row):
    row =[1]
    for i in range(0, len(prev_row)-1):
        row.append(prev_row[i]+prev_row[i+1])
    row.append(1)
    return row

def print_tr_Paskal(n): #n кол-во строк которое нужно вывести
    cur_row = [1]
    for i in range(1, n+1):
        print(cur_row)
        next_row = get_row(cur_row)
        cur_row = next_row
print_tr_Paskal(6)

#Написать функцию, которая принимает строку с разделенными дефисом
# словами и возвращает эту же строку со словами отсортированными в
# алфавитном порядке. Например, строка “green-red-yellow-black-white”
# должна быть преобразована в строку “black-green-red-white-yellow”.



s = 'green-red-yellow-black-white'
def transform_str(s):
    l = s.split('-')
    print(l)
    l.sort()
    print(l)
    return '-'.join(l)
print(transform_str(s))




#Тема 2: “Аргументы функции”
#Написать функцию, которая принимает произвольное число чисел, вычисляет
# их среднее арифметическое и возвращает только те числа, которые меньше полученного среднего арифметического.

def count(*args):
    k = [] #сохраняем в эту переменную подходящие нам числа
    sr_arifm = sum(args)/len(args)
    print(sr_arifm)
    for num in args:
        if num<sr_arifm:
            k.append(num) #добавляем в нашу последовательность подходящие числа
    return k
print(count(1, 2, 3, 4, 5, 6, 7, 8, 9))


#Написать функцию, которая принимает произвольное число чисел и
# преобразовывает их таким образом, чтобы цифры каждого числа
# (по умолчанию) были записаны в обратном порядке. Предусмотреть
# возможность по запросу пользователя выполнять преобразования
# только над нечетными числами.
def revers_num(n):
    s = str(n)
    return int(s[::-1])
def m(*args, only_odd=False):
    res = []
    for i in args:
        if not only_odd or (only_odd and i%2 != 0):
            res.append(revers_num(i))
    return res
print(m(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
print(m(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))

#Написать функцию, принимающую некоторую информацию о
# сотруднике и выводящую ее на экран согласно следующему
# шаблону:
"""
имя
фамилия
пустая строка (в случае наличия других полей)
		другие поля в алфавитном порядке их заголовков
		разделитель, состоящий из записанных подряд 30-ти дефисов “-”.
	
Например:
	Name: Anna
	Last Name: Minker
	
	Age: 27
	Phone: 123456789
	------------------------------
	Name: John
	Last Name: Bold
	
	Age: 32
	Country: USA
	Email: john.bold.@mail.com
	Phone: 987654321

Если переданная информация не содержит имени или 
фамилии сотрудника, вывести сообщение об ошибке.
"""
def print_info(**kwargs):
    if 'name' not in kwargs or 'surname' not in kwargs:
        print('invalid data')
        return None
    print('Name: ', kwargs['name'])
    print('Last name: ', kwargs['surname'])
    if len(kwargs)>2:
        print()
        key = list(kwargs.keys())[2:]
        key.sort()
        for k in key:
            print(k, ': ', kwargs[k])
    print('-'*30)
print_info(name='Anna', surname='Minker', age=27, phone=23132)


#Тема 3: “Анонимные функции”
#Дана последовательность чисел. Удалите из нее все положительные числа.
# Вычислите сумму отрицательных чисел и напечатайте ее абсолютное значение.
# Решите задачу с использованием lambda-функций.
j = [1, -45, 87, -1, 67, -45, 12, 11]
j = list(filter(lambda i: i<0, j))
print(j)
print(abs(sum(j)))

#Дан список имен. Найдите сумму длин имен списка после удаления всех имен,
# начинающихся с маленькой буквы. Решите задачу с использованием lambda-функций.

names = ['Alex', 'Miron', 'Andy', 'Ivan', 'Maksym', 'kolya', 'kostya', 'olya', 'Katya', 'mikle']
names = list(filter(lambda name: name[0].isupper(), names))
print(names)
res = 0
for n in names:
    res += len(n)
print(res)

#Преобразуйте заданную последовательность чисел таким образом,
# чтобы каждый элемент новой последовательности был равен произведению
# соответствующего элемента исходной последовательности и его порядкового
# номера, возведенного в куб. Решите задачу с использованием lambda-функций.

o = [1, 45, 87, 1, 67, 12, 11]
result = list(map(lambda elem: elem*o.index(elem)**3, o))
print(result)

#Дан список городов. Сгенерируйте еще один список,
# содержащий количество вхождений букв ‘a’ и ‘A’ в
# название каждого города. Решите задачу с использованием lambda-функций.

citys = ['Dnipro', 'Kyiv', 'Milan', 'Viena', 'Paris', 'London']
res_1 = list(map(lambda elem: elem.count('a')+elem.count('A'), citys))
print(res_1)

#Дан список игроков команды, причем для каждого игрока указаны его имя,
# фамилия и игровой рейтинг (по шкале от 1 до 10, где 10 - наивысший балл).
# Отсортируйте список игроков по фамилии, а затем по их рейтингу от лучшего
# к худшему и наоборот. Решите задачу с использованием lambda-функций.

team = [{'name': 'Antony', 'last name': 'Bloom', 'raiting': 9},
        {'name': 'Alon', 'last name': 'Riddler', 'raiting': 10},
        {'name': 'Greg', 'last name': 'Mc Queen', 'raiting': 4},
        {'name': 'Michael', 'last name': 'Andres', 'raiting': 6}]

res_0 = sorted(team, key=lambda item: item['last name'])
print(res_0)
raiting_team = sorted(team, key=lambda item: item['raiting'], reverse=True )
print(raiting_team)
raiting_team = sorted(team, key=lambda item: item['raiting'])
print(raiting_team)

#Тема 4: “Рекурсивные функции”
#Напишите рекурсивную функцию, вычисляющую сумму чисел
# следующей последовательности:
#n + (n-2) + (n-4) ….  (n-x)

def foo(n):
    if n<=0:
        return 0
    return n+foo(n-2)
print(foo(6))

#Написать рекурсивную функцию, вычисляющую сумму элементов списка,
# элементы которого также могут быть списком.
# Например, для списка [1, 2, [3, 4], [5, 6]] сумма элементов равна 21.

l = [1, 2, [3, 4], [5, 6]]
def foo(l):
    s = 0
    for elem in l:
        if type(elem) is list:
            s += foo(elem)
        else:
            s += elem
    return s
print(foo(l))

#Написать рекурсивную функцию поиска максимального элемента
# числовой последовательности.

l = [4, 6, 7, 8, 90, 65, 111]
def foo(l):
    if len(l)>1:
        return max(l[0], foo(l[1:]))
    else:
        return l[0]
print(foo(l))

#Тема 5: “Область видимости переменных”
#Напишите функцию, ведущую подсчет количества посещений указанного города.
# Функция должна принимать в качестве аргумента название города и возвращать
# некоторую внутреннюю функцию, которая каждый раз при ее вызове будет
# увеличивать счетчик посещений на 1. При решении задачи используйте нелокальную
# область видимости.

def foo(city):
    s = 0
    def incr():
        nonlocal s
        s += 1
        print(city, s)
    return incr()
res1 = foo('Dnipro')


res2 = foo('Kyiv')


#Написать функцию, вычисляющую площадь прямоугольного параллелепипеда с ребрами a, b и c.
# Данная функция должна содержать внутри себе еще одну функцию, вычисляющую площадь прямоугольника.
# Решить задачу для случаев, когда общая площадь определена как глобальная и как локальная переменная.
# Внести изменения в функции таким образом, чтобы общая площадь могла использоваться как нелокальная переменная.

#локальная переменная

def rect_paral_square(a, b, c):
    def rect_square(i, j):
        return i*j
    s = 2*(rect_square(a, b) + rect_square(a, c) + rect_square(c, b))
    return s
print(rect_paral_square(2, 4, 6))

#глобальная переменная
s = 0
def rect_paral_square(a, b, c):
    def rect_square(i, j):
        return i*j
    global s
    s = 2*(rect_square(a, b) + rect_square(a, c) + rect_square(c, b))
    return s
rect_paral_square(2, 4, 6)
print(s)

#нелокальная переменная

def rect_paral_square(a, b, c):
    s = 0
    def add_rect_square(i, j):
        nonlocal s
        s += i*j


    add_rect_square(a, b)
    add_rect_square(a, c)
    add_rect_square(c, b)
    return 2*s


print(rect_paral_square(2, 4, 6))

