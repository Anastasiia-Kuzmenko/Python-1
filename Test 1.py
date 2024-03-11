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

byte_1 = b'restart'
first_symbol = byte_1[0:1]
print(first_symbol)
new_byte_1 = first_symbol + byte_1[1:].replace(first_symbol, b'$')
print(new_byte_1)

#2.	Дана строка: “Th$e *ly-ri cs; i!s >no>t *th&at$ p=oo+r!$”.
# Представить данную строку в виде массива байт и удалить из нее каждый третий символ, начиная с третьего.
# Вывести полученную строку на экран.
str1 = 'Th$e *ly-ri cs; i!s >no>t *th&at$ p=oo+r!$'
byte_arr = bytearray(str1.encode())
print(byte_arr)
del byte_arr[2::3]
print(byte_arr.decode())

#3.	Вам пришло закодированное методом cp037 сообщение:
# '\xe6\x88\x81\xa3@\x89\xa2@\xa8\x96\xa4\x99@\x86\x81\xa5\x96\xa4\x99\x89\xa3\x85@\x97\x99\x96\x87\x99\x81\x94\x94\x89\x95\x87@\x93\x81\x95\x87\xa4\x81\x87\x85o'.
#Напишите ответ и закодируйте его тем же методом. В случае возникновения ошибки кодирования-декодирования, проигнорируйте ее.

coded = b'\xe6\x88\x81\xa3@\x89\xa2@\xa8\x96\xa4\x99@\x86\x81\xa5\x96\xa4\x99\x89\xa3\x85@\x97\x99\x96\x87\x99\x81\x94\x94\x89\x95\x87@\x93\x81\x95\x87\xa4\x81\x87\x85o'
decoded = coded.decode('cp037', errors = 'ignore')
print(decoded)
answer = 'Python!'
coded_answer = answer.encode('cp037', errors = 'ignore')
print(coded_answer)

#Тема 7: “Множества”
#1.	Подсчитайте количество уникальных символов в высказывании Уильяма Шекспира:
# “All the world’s a stage, and all the men and women merely players.
# They have their exits and their entrances; and one man in his time plays many parts.”
# (одна и та же буква в разных регистрах считается как один символ).
# Согласно таблице ASCII какой из символов данного высказывания является минимальным, а какой максимальным?

text_shekspir = 'All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; and one man in his time plays many parts.'
sh = text_shekspir.lower()
str_set = set(sh)
print("Unique symbol:", str_set)
print('Count symbol: ', len(str_set))
print('min symbol: ', min(str_set))
print('max symbol: ', max(str_set))

#2.	Дано два множества {1, 2, 3, 4, 5} и {4, 5, 6, 7, 8}. Найти:
#a.	объединение множеств
#b.	пересечение множеств
#c.	симметричную разность множеств
#d.	элементы из второго множества, входящие в первое, и удалить их из первого
#e.	является ли второе множество супермножеством для {5, 7, 4} и {8, 4, 3}
#f.	является ли второе множество правильным супермножеством для {5, 8, 4, 7, 6}
s_1 = {1, 2, 3, 4, 5}
s_2 = {4, 5, 6, 7, 8}
first = s_1 | s_2
print('two in one: ', first)
second = s_1 & s_2
print('intersection: ', second)
three = s_1.symmetric_difference(s_2)
print('difference: ', three)
s_3 = {5, 7, 4}
s_4 = {8, 4, 3}
s_5 = s_3 | s_4
four = s_2 >= (s_5)
print(four)
s_6 = {5, 8, 4, 7, 6}
five = s_2 > (s_6)
print(five)

#3.	Среди учеников старших классов провели олимпиады по физике и математике.
# Результаты выглядят следующим образом: на олимпиаде по математике 1 место занял Матвей,
# 2 место - Евгения, 3 место - Михаил, 4 место - Максим и 5 место - Наталья, а в олимпиаде
# по физике призовая тройка выглядит следующим образом: 1 место - Максим, 2 место - Матвей и 3 место -
# Александр. Администрацией школы было решено наградить всех победителей, а также особый приз выдать ребятам,
# занявшим призовые места по двум дисциплинам сразу.
#Создайте общий список победителей двух олимпиад. Список призеров в олимпиаде по
# математике отредактируйте и удалите из него тех ребят, которые не вошли в
# тройку призеров в олимпиаде по физике, после чего удалите список призеров по физике.

winner_math = {'Matvey', 'Yevhenia', 'Mykhaio', 'Maksym', 'Natalya'}
winner_physics = {'Maksym', 'Matvey', 'Aleksandr'}

common_winner = winner_math | winner_physics
print(str(common_winner))

both = winner_physics & winner_math
print(both)

winner_math = both
print(winner_math)
del winner_physics

#Тема 8: “Словари”
#1.	Перечень сетевых интерфейсов и основная информация о них представлены в виде следующей структуры данных:
# [{‘interface’: ‘Ethernet0’, ‘ip’: ‘1.1.1.1’, ‘status’: ‘up’},
# {‘interface’: ‘Ethernet1’, ‘ip’: ‘2.2.2.2’, ‘status’: ‘down’},
# {‘interface’: ‘Serial0’, ‘ip’: ‘3.3.3.3’, ‘status’: ‘up’},
# {‘interface’: ‘Serial1’, ‘ip’: ‘4.4.4.4’, ‘status’: ‘up’}].

dict_1 = [{'interface': 'Ethernet0', 'ip': '1.1.1.1', 'status': 'up'},
          {'interface': 'Ethernet1', 'ip': '2.2.2.2', 'status': 'down'},
          {'interface': 'Serial0', 'ip': '3.3.3.3', 'status': 'up'},
          {'interface': 'Serial1', 'ip': '4.4.4.4', 'status': 'up'}]

#a.	выведите на экран общее количество интерфейсов
print('interfaces: ', len(dict_1))

#b.	выведите на экран информацию (название, ip-адрес и статус), соответствующую второму интерфейсу в списке
print('The second interface: ', dict_1[1])

#c.	выведите на экран статус последнего интерфейса в списке
print('Status: ', dict_1[-1])

#d.	проверьте, добавлена ли графа ‘notes’ для первого интерфейса и выведите ее содержимое на экран. Если такой графы нет,
# то сперва добавьте ее с текстом “need to reset”
dict_1[0].setdefault('notes', 'need to reset')
print(dict_1[0])

#e.	добавьте в список еще один ethernet интерфейс с ip-адресом, как у третьего интерфейса, и статусом ‘down’.
# После этого измените ip-адрес третьего интерфейса на ‘3.3.3.4’
dict_1.append({'interface': 'Ethernet2', 'ip': dict_1[2]['ip'], 'status': 'down'})
dict_1[2]['ip'] = '3.3.3.4'
print(dict_1)

#f.	выведите на экран содержимое графы ‘notes’ первого интерфейса, а затем удалите ее
print(dict_1[0].pop('notes'))
print(dict_1)

#g.	переведите четвертый интерфейс в состояние ‘down’, а затем удалите его из списка
dict_1[3]['status'] = 'down'
print(dict_1[3])
del dict_1[3]
print(dict_1)

#2.	Дан список товаров и их цены: {‘smart watch’: 550, ‘phone’: 1000, ‘playstation’: 500,
# ‘laptop’: 1550, ‘music player’: 600, ‘tablet’: 400}.
from math import ceil
t = {'smart watch': 550, 'phone': 1000, 'playstation': 500, 'laptop': 1550, 'music player': 600, 'tablet': 400}

#a.	выведите на экран общую стоимость всех товаров
print('Common cost: ', sum(t.values()))

#b.	выведите на экран названия товаров в алфавитном порядке, а затем наоборот
t_names = t.keys()
print(sorted(t_names))
print(sorted(t_names, reverse=True))

#c.	все музыкальные плееры кроме одного были распроданы, поэтому на последний экземпляр магазин решил сделать 50% скидку.
# Внесите соответствующие изменения в список товаров.
t['music player'] = int(t['music player'] * 0.5)
print(t)

#d.	сколько планшетов необходимо продать магазину, чтобы превысить выручку,
# полученную от продажи пяти телефонов и трех ноутбуков?
sum = 5 * t['phone'] + 3 * t['laptop']
print(sum)
tablet_count = ceil(sum / t['tablet'])
print(tablet_count)
print(sum, tablet_count, tablet_count * t['tablet'])

#e.	магазин решил провести лотерею среди своих постоянных покупателей.
# Выберите произвольным образом приз для победителя лотереи, а затем удалите его из списка.
prize = t.popitem()
print('Prize: ', prize)
print(t)

#f.	в магазин поступило несколько новых устройств: ‘iphone’ - 1300, ‘music player’ - 850,
# ‘headphones’ - 200. Обновите список товаров и их цены.
t.update({'iphone': 1300, 'music player': 850, 'headphones': 200})
print(t)

result = 0
for i in range(100):
    result += i
    print(result)