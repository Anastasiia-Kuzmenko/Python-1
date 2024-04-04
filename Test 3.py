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
    l.sotr()
    print(l)
    return '-'.join(l)
print(transform_str(s))




#Тема 2: “Аргументы функции”
#Написать функцию, которая принимает произвольное число чисел, вычисляет
# их среднее арифметическое и возвращает только те числа, которые меньше полученного среднего арифметического.

