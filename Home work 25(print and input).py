#Тема 1: “Ветвления”
#1.	Дана точка M с координатами (x, y). Определить месторасположение этой точки в декартовой системе координат:
#a.	является началом координат
#b.	лежит на одной из координатных осей
#c.	расположена в одном из координатных углов

m = (10, 0)
#x = int(input('Put coordinats x: '))
#y = int(input('Put coordinats y: '))
#m = (x, y)
if m[0] == 0 and m[1] == 0:
    print('origin')
elif m[0] == 0:
    print('lies on the axis OY')
elif m[1] == 0:
    print('lies on the axis OX')
else:
    print('lies in one of the coordinate angels')


#Дан массив целых чисел. Найти его минимальный и максимальный элементы.
# Если минимальный элемент расположен раньше максимального,
# найти среднее арифметическое всех элементов между ними,
# а если после - заменить данные элементы на их среднее геометрическое.


l = [14, 2, 6, 8, 5, 9, 3, 0, 2, 5, 4]
#l = input('Enter a list of number: ')
#l = list(map(int, l.split()))
#print(l)

max_l = max(l)
min_l = min(l)
max_l_ind = l.index(max_l)
min_l_ind = l.index(min_l)
if min_l_ind < max_l_ind:
    sub_l = l[min_l_ind + 1: max_l_ind]
    res = sum(sub_l)/len(sub_l)
    print('average: {:.2f}'.format(res))
else:
    sub_l = l[max_l_ind+1:min_l_ind]
    sr_geom = 1
    for i in sub_l:
        sr_geom *= i
    sr_geom **= 1/len(sub_l)
    sr_geom = round(sr_geom, 2)
    l[max_l_ind+1:min_l_ind] = [sr_geom]*len(sub_l)
    print('Geometric mean: {:.2f} {}'.format(sr_geom, l))

#Тема 2: “Циклы с условием”
#Дано натуральное число N. Определить самую большую цифру и ее позицию в числе.
# Например, для числа 573867 наибольшей является цифра 8, а ее позиция - четвертая слева.
N = 593867
#N = int(input('Enter natural number N: '))
max = 0
courent_ind = len(str(N))
while N > 0:
    sym = N % 10
    if sym > max:
        max = sym
        max_ind = courent_ind
    N //= 10
    courent_ind -= 1
print(max, max_ind)

#Дана последовательность вещественных чисел. Определить среднее арифметическое среди
#кратных 7 элементов последовательности.
l = [2.4, 9.2, 7.0, 14.0, 0.7, 12.4]
#l = input('Enter numbers: ').split()
#l = list(map(float, l))

i = 0
nums = []
while i<len(l):
    if l[i]%7 == 0: #not l[i]%7
        nums.append(l[i])
    i += 1
if nums:
    res = sum(nums)/len(nums)
    print(res)
else:
    print('Not found')

#Дан некоторый текст. Определить количество вхождений в него каждого символа.
text = "Дан некоторый текст. Определить количество вхождений в него каждого символа."
#text = input('Enter string: ')

res = {}
for sym in text:
    if sym in res.keys():
        res[sym] += 1
    else:
        res[sym] = 1
print(res)


#Найти среднее арифметическое делителей числа N.
N = 28
#N = int(input('Enter number N: '))
deliteli = []
for i in range(1, N+1):
    if N%i == 0:
        deliteli.append(i)
print(deliteli)
res = sum(deliteli)/len(deliteli)
print(round(res, 2))

#Тема 4: “Операторы передачи управления”

#Дана строка, представляющая из себя некоторое выражение.
# Проверить корректность использования скобок в заданном выражении:
#a.количество открывающихся скобок каждого
# вида должно соответствовать количеству закрывающихся скобок этого же вида;
#b.	порядок следования открывающихся и закрывающихся скобок должен быть верным.
#Например, выражение “aaa(bc[def](ggg(hh)))” можно считать верным, а выражение
# “aaa(bc[def](ggg(hh))” будет неправильным, так как в нем количество
# открывающихся круглых скобок не соответствует количеству закрывающихся.
# Выражение “aaa(bc[def(g]gg(hh)))” также будет неверным, т.к. в нем
# не соблюдена правильная очередность открывающихся и закрывающихся скобок.

s = 'aaa(bc[def](ggg(hh)))'
tmp = []
braces = {')': '(', ']': '[', '}': '{'}
for sym in s:
    if sym in braces.values():
        tmp.append(sym)
    elif sym in braces.keys():
        if len(tmp) == 0 or braces[sym]!=tmp.pop():
            print('wrong')
            break
else:
    if len(tmp) > 0:
        print('wrong')
    else:
        print('right')
#Вычислить произведение последних трех чисел не кратных
# 5 в диапазоне от 20 до 50.

result = 1
count = 0
for i in range(50, 19, -1):
    if i%5 != 0:
        result *= i
        count +=1
    if count == 3:
        break
print(result)

#	Найти 2-ое, 6-ое и 11-ое по счету числа кратные 7,
#	но не кратные 13 в диапазоне от 1000 до 2000.

ind = [2, 6, 11]
cur_ind = 0
res = []
for i in range(1000, 2001):
    if i%7!=0 or i%13 == 0:
        continue
    cur_ind += 1
    if cur_ind in ind:
        res.append(i)
    if cur_ind == ind[-1]:
        break
print(res)

#Тема 5: “Условие else в циклах”
#Дана последовательность чисел. Проверить, есть ли в ней хотя бы одно число
# с делителями 2, 5 и 7.
# Если да, вывести его на экран. Если нет, вывести соответствующее сообщение.

l = [3, 4, 6, 9, 10, 12, 13, 18, 70]
for num in l:
    if num%2 == 0 and num%5 == 0 and num%7 == 0:
        print(num)
        break
else:
    print('Numbers is absent')
#Дана последовательность чисел.
# Проверить, являются ли все элементы
# последовательности нечетными числами.
l = [3, 4, 6, 9, 10, 12]
for num in l:
    if num % 2 == 0:
        print('No')
        break
else:
    ('Yes')

#Дан список продуктов с ценами на них:
# ‘milk’ - $12, ‘bread’ - $10, ‘meat’ - $60, ‘vegetable mix’ - $20, ‘fruit mix’ - $35, ‘fish’ - $45, ‘eggs’ - $15, ‘cake’ - $15.
# У Марты есть $100.
# Какое максимальное количество продуктов она может купить?
# Выведите на экран список этих продуктов. В случае если Марта сможет купить все продукты из списка,
# выведите соответствующее сообщение. Решите эту же задачу

goods = {'milk': 12, 'bread': 10, 'meat': 60, 'vegetable mix': 20, 'fruit mix': 35, 'fish': 45, 'eggs': 15, 'cake': 15}
goods_sort = {'bread': 10, 'milk': 12, 'eggs': 15, 'cake': 15, 'vegetable mix': 20, 'fruit mix': 35, 'fish': 45, 'meat': 60}
sum = 250 # max сумма денег на которую совершаем покупку
max_count = 0 #кол-во пролуктов на кот. совершаем покупку
for name, price in goods_sort.items():
    sum -= price
    if sum < 0:
        print(max_count)
        break
    print(name, end=' ')
    max_count += 1
else:
    print('\nAll goods byed')

#Тема 6: “Матрицы”
#Преобразуйте матрицу A(n, m) таким образом, чтобы строки с
# нечетными индексами были упорядочены по убыванию, а с четными - по возрастанию.
A = [[1, 4, 6],
    [6, 3, 0],
     [2, 9, 4]]
for row_num in range(0, len(A)):
    if(row_num + 1) % 2 == 0:
        A[row_num].sort()
    else:
        A[row_num].sort(reverse=True)
print(A)

#Дана квадратная матрица.
# Проверьте, является ли она диагональной.
m=  [[2, 0, 0, 0, 0],
     [0, 3, 0, 0, 0],
     [0, 0, 5, 0, 0],
     [0, 0, 0, 5, 0],
     [0, 0, 0, 0, 2]]
is_diag = True
for i in range(0, len(m)):
    for j in range(0, len(m[i])):
        if i != j and m[i][j] != 0:
            is_diag = False
            break
    if not is_diag:
        break
print(is_diag)

#Дана квадратная матрица.
# Проверьте, является ли она нижнетреугольной.
# Если да, преобразуйте ее таким образом, чтобы
# она стала верхнетреугольной.
m = [[2, 0, 0, 0, 0],
     [0, 3, 0, 0, 0],
     [7, 0, 5, 0, 0],
     [0, 4, 0, 5, 0],
     [0, 0, 0, 0, 2]]
is_ntr = True
for i in range(0, len(m)):
    for j in range(i+1, len(m[i])):
        if m[i][j] != 0:
            is_ntr = False
            break
    if not is_ntr:
        break
print(is_ntr)
if is_ntr:
    for i in range(0, len(m)):
        for j in range(i+1, len(m[i])):
         m[i][j], m[j][i] = m[j][i], m[i][j]
    for row in m:
        print(row)