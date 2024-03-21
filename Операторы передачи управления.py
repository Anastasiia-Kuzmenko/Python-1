#Сын вернулся из магазина со списком покупок.
#Символом ‘v’ он отметил те продукты, которые ему удалось купить:
#молоко, хлеб (v), пирог, вишня (v), огурцы (v), сыр, сметана, шоколад (v).
#Выведите на экран список продуктов, которые мальчик не смог приобрести.

l = {'milk': '', 'bread': 'v', 'pie': '', 'chery': 'v', 'cucamber': 'v', 'cheese': '', 'cream': '', 'chocolate': 'v'}
for k, v in l.items():
    if v == 'v':
        continue
    print(k)

#Дана строка 'Break and Continue operators'.
#Выведите на экран данную строку до символа ‘p’ включительно,
# пропуская при этом каждый третий символ.

s = 'Break and Continue operators'
for i in range(0, len(s)):
    if s[i] == 'p':
        if (i + 1) % 3 != 0:
          print(s[i], end='')
        break
    if i > 0 and (i + 1) % 3 == 0:
        continue
    print(s[i], end='')

#Дан список слов: ['snow', 'rain', 'wind', 'sun', 'clouds']. Выведите на экран:
#- все слова, длина которых больше 3-х символов
#- все слова, расположенные до слова длиной 3 символа
k = ['snow', 'rain', 'wind', 'sun', 'clouds']
for elem in k:
    if len(elem) <= 3:
        continue
    print(elem, end='')
print()
for elem in k:
    if len(elem) == 3:
        break
    print(elem, end='')


# Дан диапазон чисел от 1 до 9. Необходимо написать программу,
# которая будет последовательно суммировать числа из диапазона,
# пока не будет достигнута сумма, равная 15, и затем выведет на экран количество чисел,
# которые для этого потребовалось сложить.
# Напишите два варианта решения задачи: с использованием цикла for и с использованием цикла while

m = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
count = 0
for num in m:
    total += num
    count += 1
    if total >= 15:
        break
print('Count number: ', count)

m = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
count = 0
index = 0

while total < 15 and index < len(m):
    total += m[index]
    count += 1
    index += 1
print('Count number: ', count)

#	Выведите на экран все числа от 5  до 25 следующим образом:
#a.	Числа кратные 3 или 6 - пропустите
#b.	Для чисел, кратных 5, напечатайте строку “N кратно 5”, где N - текущее число
#c.	Все остальные числа напечатайте как есть


for i in range(5, 26):
    if i % 3 == 0 or i % 6 == 0:
        continue
    elif i % 5 == 0:
        print(f"{i} кратно 5")
    else:
        print(i)

# Дан список имен: [‘Rose’, ‘Nina’, ‘Phillip’, ‘Alex’, ‘Jimmy’, ‘Max’].
# Вывести на экран приветственную строку в формате ‘Hello name’ для всех имен длиной не более 4-х символов.
# При этом все имена, следующие за именем, содержащим букву ‘x’,  должны быть проигнорированы.

names = ['Rose', 'Nina', 'Phillip', 'Alex', 'Jimmy', 'Max']
ignore_next = False

for name in names:
    if len(name) <= 4 and not ignore_next:
        print('Hello', name)
    if 'x' in name:
        ignore_next = True
    else:
        ignore_next = False


#Написать программу, которая будет запрашивать у пользователя пароль до тех пор,
#пока он не удовлетворит следующим критериям:
#- длина пароля не менее 8 символов
# пароль не содержит в себе имя пользователя


name = input('name: ')
psw = input('psw: ')
while True:
    if len(psw)<8:
        print('To short psw')
    elif name in psw:
        print('Psw contains name')
    else:
        print('Psw was set!')
        break
    psw = input('psw: ')

#Написать программу, которая будет запрашивать у пользователя пароль до тех пор,
#пока он не удовлетворит следующим критериям:
#- длина пароля не менее 8 символов
# пароль не содержит в себе имя пользователя


name = input('name: ')
psw = input('psw: ')
while True:
    if len(psw)<8:
        print('To short psw')
    elif name in psw:
        print('Psw contains name')
    else:
        print('Psw was set!')
        break
    psw = input('psw: ')