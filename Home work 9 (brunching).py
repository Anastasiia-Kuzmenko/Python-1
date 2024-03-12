result = 0
for i in range(100):
    result += i
    print(result)

x = 42
if x <= 0:
    print('Negative: ')
else:
    print('Pozitive rezult')

#Написать программу, которая будет конвертировать значение температуры из градусов Цельсия в Фаренгейты и наоборот.
#Входные данные: 60C, 45F, ….
#Результат: 140F, 7C, ….
#Расчетные формулы:

#c = (F-32) * 5/9
#F = C * 9/5 + 32

#Тестовые значения:
#60С     140F
#90C     194F
#100C    212F

#45F     7.22С
#90F     32.22С
#125f    51.67С

#50a     wrong value

t = '76F'
suffix = t[-1] #проверяем температура задана в C или А
val = int(t[:-1])
if suffix in ['C', 'c']:
    conv_val = val * 9/5 + 32
    res = str(round(conv_val, 2)) + 'F'
elif suffix in ['F', 'f']:
    conv_val = (val - 32) * 5/9
    res = str(round(conv_val, 2)) + 'C'
else:
    res = 'wrong value'
print(t, ' is ', res)

#Напишите программу расчета суммы двух целых чисел. Однако если
# полученная сумма находится в интервале от 15 до 20, вывести на экран
#число 20

a = 10
b = 8
sum = a + b
if sum in range(15, 21):
    print(20)
else:
    print(sum)

#Даны длины сторон треуголлника. Проверить, является ли треугольник
#равносторонним, равнобедернным или разносторонним.

k = 10
m = 20
n = 20

if k == m == n:
    print('Треугольник равносторонний')
elif k == m or m == n or n == k:
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')

#Написать программму решения квадратного уравнения
# ax^2 + bx + c = 0
# Исходные данные: a,b,c
# Результат: корни квадратного уравнения х1 и Х2 или сообщение
# о том что корней нет

from math import sqrt

a1 = 4
b1 = 10
c1 = 5
D = b1**2 - 4 * a1 * c1
if D >= 0:
    x1 = (-b1 + sqrt(D)) / (2 * a1)
    x2 = (-b1 - sqrt(D)) / (2 * a1)
    print(round(x1), round(x2))
else:
    print('корней нет')

#Составить программу нахождения действительных и комплексных корней
#квадратного уравнения ax^2 + bx + c = 0.
#Исходные данные: a, b, c
#Результат: действительные корни: x1 и x2, -
#или комплексные корни: x1 + ix2 и x1 - ix2

#Тестовые значения:
#a   b   c       x1      x2
#2   4   10      -1+2i   -1-2i
#4   10  5       -0.69   -1.81

from math import sqrt, fabs

A1 = 4
B1 = 10
C1 = 5
D = B1**2 - 4 * A1 * C1
if D >= 0:
    x1 = (-B1 + sqrt(D)) / (2 * A1)
    x2 = (-B1 - sqrt(D)) / (2 * A1)
    print(round(x1), round(x2))
else:
    x1 = -B1 / (2 * A1)
    x2 = sqrt(fabs(D))/(2 * A1)
    print(complex(x1, x2), complex(x1, -x2))

#	Отредактируйте решение задачи о паролях из контрольной работы таким образом,
#	чтобы программа после выполнения всех проверок выводила бы на экран сообщение о том,
#	является ли пароль безопасным.  Критерии безопасности пароля:
#a.	длина пароля не менее 5 символов
#b.	содержит буквы латинского алфавита как в верхнем, так и в нижнем регистре: A-Z, a-z
#c.	содержит цифры от 0 до 9
#d.	содержит хотя бы один из символов: @, #, %, &

password = 'bdfjkjdA6'
cond1 = len(password) >= 5
cond2 = not password.islower() and not password.isupper()
cond3 = len({'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'} & set(password)) > 0
cond4 = len({'@', '#', '%', '&'} & set(password)) > 0
if cond1 and cond2 and cond3 and cond4:
    print('Password is true')
else:
    print('Password is wrong')

#	Решите предыдущую задачу для случая, когда пароль считается безопасным при выполнении хотя бы трех критериев из списка.
password = 'bdfjkjd6'
criteria_met = 0
cond1 = len(password) >= 5
cond2 = not password.islower() and not password.isupper()
cond3 = len({'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'} & set(password)) > 0
cond4 = len({'@', '#', '%', '&'} & set(password)) > 0
if cond1:
    criteria_met += 1
if cond2:
    criteria_met += 1
if cond3:
    criteria_met += 1
if cond4:
    criteria_met += 1

if criteria_met >= 3:
    print('Password is metch')
else:
    print('Pasword non metch')

#	Напишите программу расчета “человеческого” возраста для собаки. Расчет должен производиться следующим образом:
# первые два года жизни каждый год эквивалентен 10.5 человеческим годам,
# далее каждый год может быть приравнен к 4 человеческим годам.

dog_age = 5
if dog_age <= 2:
    human_age = dog_age * 10.5
else:
    human_age = 21 + (dog_age - 2) * 4
print("Human age:", human_age, "year")

#	В магазине продаются следующие товары:
#	smart watch ($600), phone ($1000),
#	playstation ($450), laptop ($1550),
#	music player ($400) и tablet ($400).
#	Майкл хочет сделать подарок родителям.
#	В магазине проводится акция: если он купит товары на $1000,
#	то любой следующий товар он получит со скидкой 30%.
#	У Майкла есть $1300. Хватит ли у него денег, чтобы купить музыкальный плеер маме, у
#	мные часы папе и плейстейшн себе?

shop = {'smart watch': 600, 'phone': 1000, 	'playstation': 450, 'laptop': 1550, 'music player': 400, 'tablet': 400}
mike_have = 1300
total_cost = shop['smart watch'] + shop['music player'] + shop['tablet']

if total_cost >= 1000:
    total_cost += (shop['tablet'] * 0.7)
if mike_have >= total_cost:
     print("Mike can")
else:
     print("Mike dont have enaf money")





