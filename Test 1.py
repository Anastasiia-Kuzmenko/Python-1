# Тема 1: “Типы и модель данных”
# 1.	Выполнить следующие действия:
# a.	создать переменную А и присвоить ей значение 5. Вывести на экран тип данных и идентификатор созданного объекта.
A = 5
print('Type: ', type(A))
print('Id: ', id(A))

# b.создать переменную В и присвоить ей значение 12. Вывести на экран тип данных и идентификатор созданного объекта.
B = 12
print('Type: ', type(B))
print('Id: ', id(B))

# c.создать переменную С и присвоить ей значение 5.7. Вывести на экран тип данных и идентификатор созданного объекта.
C = 5.7
print('Type: ', type(C))
print('Id: ', id(C))

# d.присвоить переменной А значение 12. Проверить, изменился ли ее идентификатор, и совпадает ли он с идентификатором
# переменной В. Почему?
A = 12
print(A is B)
#в Python числа от -5 до 256 кэшируются, и для них используются одни и те же объекты в памяти (индентификатор)

# e.	присвоить переменной А значение переменной С. Проверить, изменился ли ее идентификатор,
# и совпадает ли он с идентификатором переменной С. Почему?
A = C
print('Id: ', id(A))
#в Python числа от -5 до 256 кэшируются, и для них используются одни и те же объекты в памяти (индентификатор)

# f.путем множественного присваивания создать переменные D, E и F и присвоить каждой из них значение 125.
# Вывести на экран и сравнить между собой идентификаторы созданных объектов.
D = E = F = 125
print(id(D), id(E), id(F))

#Тема 2: “Тип None. Логический тип данных”
#1.	Создать переменные a, b, c и присвоить им значения 9, 17 и 5 соответственно. Проверить выполнение следующих условий:

a, b, c = 9, 17, 5
#a.	a больше b
print('a>b: ', a > b)
#b.	a не равно разности b и c
print(a != b - c)
#c.	b равно сумме a и c
print(b == a + c)
#d.	c меньше или равно сумме a и b
print(c <= a + b)
#e.	a меньше b, но больше c
print(a < b and a > c)
#f.	b больше a или b больше c
print(b > a or b > c )

#2.	Создать пустую переменную. Проверить ее на истинность и ложность. Объясните полученный результат.
#Дано логическое выражение ¬А ˄ (С ˅ А) ˄ (В ˅ ¬С).
# Укажите значения логических переменных A, B и С, при которых значение выражения будет ложным
k = None
print('is True: ', a is True)
print('is False: ', a is False)

#Дано логическое выражение ¬А ˄ (С ˅ А) ˄ (В ˅ ¬С).
# Укажите значения логических переменных A, B и С, при которых значение выражения будет ложным

A1 = 0
B1 = 1
C1 = 1
result = not A1 and (C1 or A1) and (B1 or not C1)
print(result)

#Тема 3: “Числовой тип данных”
import math
a = 100
y = (((1 + a + math.pow(a, 2)) / (2 * a + math.pow(a, 2))) + 2 -
     ((1 - a + math.pow(a, 2)) / (2 * a - math.pow(a, 2))) *
     (5 - 2 * math.pow(a, 2)))
print(y)

a = math.radians(90) #перводим в градусы
b = math.radians(90)
c = math.radians(90)
y1 = 1/4 * (math.sin(a + b - c) + math.sin(b + c - a) +
     math.sin(c + a - b) -  math.sin(a + b +c))
print('y1: ', y1)

#Тема 4: “Последовательности”
#1.	Дан список, состоящий из 4х элементов: ‘abc’, ‘xyz’, ‘aba’, ‘1221’.
# Проверить для каждого элемента выполнение следующих условий:
# длина элемента больше 2х и первый и последний символ у него совпадают.
my_list = ['abc', 'xyz', 'aba', '1221']
element1 = my_list[0]
print(element1, len(element1) > 2 and element1[0] == element1[-1])
element2 = my_list[1]
print(element2, len(element2) > 2 and element2[0] == element2[-1])
element3 = my_list[2]
print(element3, len(element3) > 2 and element3[0] == element3[-1])
element4 = my_list[3]
print(element4, len(element4) > 2 and element4[0] == element4[-1])

#2.	Дан список цветов: ‘red’, ‘green’, ‘white’, ‘black’, ‘pink’, ‘yellow’.
# Создайте еще один список и переместите в него 1-ый, 5-ый и 6-ой элементы.
my_list1 = ['red', 'green', 'white', 'black', 'pink', 'yellow']
new_list = [my_list1[0], my_list1[4], my_list1[5]]
print(new_list)

#3.	Даны несколько списков: [-8, 1, 2, -2, 0], [1, 1, 0, 0, 2, -2, -2], [1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 34].
# Для каждого из списков найти второе наименьшее значение в нем (правильные ответы выделены жирным шрифтом).
list1 = [-8, 1, 2, -2, 0]
list2 = [1, 1, 0, 0, 2, -2, -2]
list3 = [1, -1, 0, -9, 4, -5]
list4 = [1, 4, 0, 23, 6, 34]
s1 = set(list1) #убираем повторяющиеся элементы
s2 = set(list2)
s3 = set(list3)
s4 = set(list4)
second_min1 = sorted(set(list1))[1]
second_min2 = sorted(set(list2))[1]
second_min3 = sorted(set(list3))[1]
second_min4 = sorted(set(list4))[1]

print("Second min:", second_min1)
print("Second min:", second_min2)
print("Second min:", second_min3)
print("Second min:", second_min4)

#4.	Дан список гостей, посетивших вечеринку, причем гости в этом списке располагаются в порядке их прибытия:
# Adela, Fleda, Owen, May, Mona, Gilbert, Ford (Adela приехала на вечеринку первая, а Ford - последний).
# Гость, прибывший после того, как половина гостей уже была на вечеринке, считается в меру опоздавшим,
# в то время как гость, прибывший последним, считается опоздавшим неприлично. Определите, попадают ли в одну из этих
# категорий (и если да, то в какую) следующие гости: May, Fleda, Gilbert и Ford.
guests = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
ind_v_meru_op = int(len(guests) / 2) #ищем индекс гостя в меру опоздавшего
ind_op_nepr = len(guests) - 1
name = 'Ford'
ind_name = guests.index(name)
print('V mery opozd: ', ind_name > ind_v_meru_op and ind_name != ind_op_nepr)
print('Opozd ne prilichno: ', ind_name == ind_op_nepr)

#5.	Спортивный обозреватель хранит записи о каждой спортивной команде следующим образом:
# первым в списке идет имя тренера команды, затем - капитана, и далее имена всех участников
# в соответствии с их порядковым номером игрока. Также у него имеется список всех спортивных команд,
# первое место в котором занимает лучшая команда, и далее по убывающей к самой худшей.
# Выведите на экран имя капитана худшей команды.

team1 = ['Alex', 'Mark', 'Player1', 'Player2', 'Player3', 'Player4', 'Player5']
team2 = ['Antony', 'Tom', 'Player1', 'Player2', 'Player3', 'Player4', 'Player5']
team3 = ['Michael', 'Noam', 'Player1', 'Player2', 'Player3', 'Player4', 'Player5']

common_list = ['team2', 'team1', 'team3']

print('capitan: ', common_list[-1][1])


#6.	Дано некоторое целое число. Вывести на экран сумму всех целых чисел от 0 и до заданного числа включительно.

n = 10
l = range(0, n+1)
sum_elem = sum(l)
print('summa: ', sum_elem)

#Тема 5: “Текстовые последовательности”

#1.	Напишите программу, которая позволит выполнять проверку пароля на сложность в соответствии со следующими критериями:
#a.	длина пароля не менее 5 символов
#b.	содержит буквы латинского алфавита как в верхнем, так и в нижнем регистре: A-Z, a-z
#c.	содержит цифры от 0 до 9
#d.	содержит хотя бы один из символов: @, #, %, &

password = 'bdfjkjdA6&'
cond1 = len(password) >= 5
cond2 = not password.islower() and not password.isupper()
cond3 = len({'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'} & set(password)) > 0
cond4 = len({'@', '#', '%', '&'} & set(password)) > 0
print('Password is true: ', cond1 and cond2 and cond3 and cond4)

#2.	Вы находитесь в квест-комнате по мультфильму WALL-E! Вы нашли записку:
#"In a distant, but not so unrealistic, future where mankind has
# abandoned earth because it has become covered with trash from
# products sold by the powerful multi-national Buy N Large corporation,
# WALLE, a garbage collecting robot has been left to clean up the mess.
# Mesmerized with trinkets of Earth's history and show tunes, WALLE is alone on
# Earth except for a sprightly pet cockroach. One day, EVE, a sleek (and dangerous)
# reconnaissance robot, is sent to Earth to  find proof that life is once again sustainable."
#Чтобы выбраться из комнаты, необходимо выполнить следующие шаги:
#a.	вывести на экран длину текста в обнаруженной записке
#b.	вывести на экран весь текст в нижнем регистре
#c.	заменить все вхождения некорректно написанного имени WALLE на его правильную форму WALL-E.
#d.	подсчитать, сколько раз в тексте было использовано слово Earth.
text = ("In a distant, but not so unrealistic, future where mankind has abandoned earth because "
        " it has become covered with trash from products sold by the powerful multi-national Buy "
        "N Large corporation, WALLE, a garbage collecting robot has been left to clean up the mess. "
        "Mesmerized with trinkets of Earth's history and show tunes, WALLE is alone on Earth except "
        "for a sprightly pet cockroach. One day, EVE, a sleek (and dangerous) reconnaissance robot, "
        "is sent to Earth to  find proof that life is once again sustainable.")
text_1 = len(text)
print('Lenght text: ', text_1)
text_2 = text.lower()
print('Lowcarse: ', text_2)
text_3 = text.replace('WALLE', 'WALL-E')
print('Change name: ', text_3)
text_4 = text.count('Earth')
print('count earth: ', text_4)

#Тема 6: “Бинарные последовательности”
#1.	Дана байтовая строка. Заменить в ней все вхождения первого символа на знак доллара $,
# кроме самого первого символа. Например, строка b’restart’ должна превратиться в строку b’resta$t’.

bytes_1 = b'restart'

#2.	Дана строка: “Th$e *ly-ri cs; i!s >no>t *th&at$ p=oo+r!$”.
# Представить данную строку в виде массива байт и удалить из нее каждый третий символ, начиная с третьего.
# Вывести полученную строку на экран.

#3.	Вам пришло закодированное методом cp037 сообщение:
# '\xe6\x88\x81\xa3@\x89\xa2@\xa8\x96\xa4\x99@\x86\x81\xa5\x96\xa4\x99\x89\xa3\x85@\x97\x99\x96\x87\x99\x81\x94\x94\x89\x95\x87@\x93\x81\x95\x87\xa4\x81\x87\x85o'.

#Напишите ответ и закодируйте его тем же методом. В случае возникновения ошибки кодирования-декодирования, проигнорируйте ее.

