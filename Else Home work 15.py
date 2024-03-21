#Для приготовления пирога необходимы следующие ингредиенты: масло, мука, сахар, яйца, сливки, орехи, вишня и ванилин.
#Маша составила список имеющихся у нее продуктов: сахар, яблоки, груши, орехи, яйца, мука, крахмал, маргарин, молоко, мед.
#Проверьте, сможет ли Маша приготовить пирог и выведите соответствующее сообщение на экран.
# решение через множества
ingr = {'масло', 'мука', 'сахар', 'яйца', 'сливки', 'орехи', 'вишня', 'ванилин'}
exist_ingr = {'сахар', 'яблоки', 'груши', 'орехи', 'яйца', 'мука', 'крахмал', 'маргарин', 'молоко', 'мед'}
if exist_ingr >= ingr:
    print('Yes')
else:
    print('No')
# решение через циклы
for elem in ingr:
    if elem not in exist_ingr:
        print('No')
        break
else:
    print('Yes')
#Дан список слов: ['snow', 'rain', 'wind', 'sun', 'clouds'].
#Проверьте, есть ли среди них хотя бы одно слово с длиной менее 4-х символов.
#Выведите соответствующее сообщение на экран.
#Решите эту же задачу для случая, когда нужно найти хотя бы 2 таких слова.
#only 1 world
l = ['snow', 'rain', 'wind', 'sun', 'clouds']
for elem in l:
    if len(elem) < 4:
        print('Yes')
        break
else:
    print('No')

# at leat 2 world
count = 0
for elem in l:
    if len(elem) < 4:
        count += 1
    if count == 2:
        print('Yes')
        break
else:
    print('No')
#Написать программу, которая будет подсчитывать количество букв и цифр в заданной строке.
#В случае, если обнаружен символ, не являющийся ни буквой, ни цифрой,
#необходимо вывести этот символ и соответствующее сообщение на экран.
#Если такие символы отсутствуют,  вывести сообщение с количеством букв и цифр.
s = 'nkjvcbjehwu4hui4r3miw9j'
l_count = 0
n_count = 0
for sym in s:
    if sym.isalpha():
        l_count += 1
    elif sym.isdigit():
        n_count += 1
    else:
        print(sym, 'error')
        break
else:
    print('Letter:', l_count)
    print('Count: ', n_count)

#	Дана последовательность чисел.
#	Проверить содержит ли она хотя бы одно четное число.
#	Если да, то вывести его на экран.
#	Если нет, то вывести сообщение о том, что четные числа не найдены.

n = [1, 1, 3, 1, 5, 3, 7, 7, 9, 1]
n_count = 0
for i in n:
    if i % 2 == 0:
        print('even numbe', i)
        break
else:
    print('even number not found')

# Дана строка “Python else loop”.
# Проверьте, содержит ли она букву ‘l’.
# Если да и следующей за ней идет одна из букв: ‘a’, ’o’ или ‘e’, - напечатайте эти буквы.
# В противном случае выведите сообщение о том, что искомые комбинации не найдены.
v = 'Python else loop'
found_combination = False

for i in range(len(v)):
    if v[i] == 'l' and i + 1 < len(v) and v[i + 1] in ['a', 'o', 'e']:
        print(v[i + 1])
        found_combination = True

if not found_combination:
    print('combination not found')

#Перепишите программу проверки надежности пароля из предыдущего урока,
# ограничив количество попыток ввода пароля. Если за три попытки пароль
# так и не был установлен, вывести соответствующее сообщение на экран.

name = input('name: ')
attempts = 3

while attempts > 0:
    psw = input('Input password: ')
    if len(psw) < 8:
        print('Wrong password')
    elif name in psw:
        print('Password mast not metch wit name')
    else:
        print('Password is correct!')
        break
    attempts -= 1
    if attempts == 0:
        print('Count is over')


