basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
a = 'orange' in basket
print(a)
b = 'grape' in basket
print(b)

c = set('abracadabra')
d = set('alacazam')
print(c, d)
difference = c - d
association = a | b
intersections = a & b
k = a ^ b
print(difference, association, intersections, k)

#Проверить колв -во уникальных символов в данном тексте

s = "Дан небольшой текс. Проверить колличество уникальных символов в данном тексте. "
s = s.lower() #приводим все символы к нижненему регистру
unic_symb = set(s)
print(unic_symb)
print(len(unic_symb)) #len(s) (возвращает кол-во элементов множества)


#Даны два списка чисел, содержащие 10 и 15 элементов соответственно.
#Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания,
#а все остальные - в порядке убывания.

l1 = [11, 2, 3, 14, 5, 6, 17, 8, 9, 10]
l2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

s1 = set(l1) #преобразовываем список в множество
s2 = set(l2)
print(s1, s2)
common_elem = s1 & s2 #находим общие элементы также можно использовать метод s1.intersection(s2)
sorted_common_elem = sorted(common_elem) #сортируем в порядке возрастания
print('общие элементы в порядке возрастания: ', sorted_common_elem)
other_elem = s1 ^ s2 #находим отличающиеся элементы также можно использовать s1.symmetric_difference(s2)
print(other_elem)
sorted_other_elem = sorted(other_elem, reverse=True)
print('разные элементы в порядке убывания: ', sorted_other_elem)

#Дан набор множеств: найти кол- во уникальных элементов во всех множествах. Найти минимальный и максимальный элемент среди них.

s3 = {1, 2}
s4 = {3}
s5 = {4, 5}
s6 = {3, 2, 6}
s7 = {6}
s8 = {7, 8}
s9 = {9, 8}
mn = s3 | s4 | s5| s5 | s7 | s8 | s9 #объеденяем множества также можно использовать метод s3.union(s4,s5....)
print(mn)
count = len(mn)
print('Unic elems coutn: ', count)
print('min elem: ', min(mn))
print('max elem: ', max(mn))



#Марина, Женя и Света занимаются рисованием, а Костя, Женя и Илья - дополнительно посещают уроки музыки.
#Определите, сколько человек занимается только одним видом искусства и выведите список их имен.
#Ученик, занимающийся в обоих кружках, решил бросить занятия рисованием.
#Произведите соответствующие изменения.

drawing = {'Marina', 'Zhenya', 'Sveta'}
music = {'Kostya', 'Zhenya', 'Ilya'}
only_one_hobby = drawing.symmetric_difference(music) #можно использовать drawing ^ music
print('Only one hoby: ', only_one_hobby)
both_hobbies = drawing.intersection(music) #можно использовать music & drawing
print('Both hobbies: ', both_hobbies)
drawing = drawing - both_hobbies
print('Drawing: ', drawing)

#Известно, что в классе 5 учеников (Костя, Маша, Данила, Ваня и Егор) увлекаются историей,
# и 7 учеников (Света, Ваня, Сергей, Марина, Костя, Маша и Антон) интересуются биологией.
# Кроме этого 2 ученика (Антон и Николай) активно занимаются спортом. Найдите, кто из учеников увлекается и историей,
# и биологией одновременно? Есть ли в классе ученики, которые преуспели во всех трех дисциплинах?
# Кто из спортсменов также интересуется биологией? Сколько всего учеников занято на дополнительных занятиях?
# Выведите их имена в алфавитном порядке.

history = {'Kostya', 'Masha', 'Danylo', 'Vanya', 'Egor'}
biology = {'Sveta', 'Vanya', 'Sergey', 'Maryna', 'Kostya', 'Masha', 'Anton'}
sport = {'Anton', 'Nikolay'}
history_and_biology = history & biology
print('History and byology: ', history_and_biology)
history_biology_sport = history.intersection(biology, sport)
print('all subject: ', history_biology_sport)
biology_and_sport = sport & biology
print('Sport and biology: ', biology_and_sport)
count1 = len(history) + len(biology) + len(sport)
print(count1)
all_students = history | biology | sport
sorted_on_alpabet = sorted(all_students)
print('On alpabet: ', sorted_on_alpabet)

#Даны три пересекающихся множества A, B и C. Проверьте справедливость равенства: (A - B) - C = (A - C) - (B - C).
#Подтвердите полученный результат с помощью кругов Эйлера.

a1 = {'36', '44', '11', '6', '8'}
b1 = {'37', '44', '11', '6', '8'}
c1 = {'38', '44', '11', '6', '8'}
equlity = (a1 - b1) - c1 == (a1 - c1) - (b1 - c1)
print(equlity)

#3.	Дано несколько чисел: 543731, 4472, 999999, 347623 и 1000001.
# Найти для каждого числа количество уникальных цифр, которое оно содержит, а также минимальную и максимальную цифру.


numbers = [543731, 4472, 999999, 347623, 1000001]
for number in numbers:
    number_str = str(numbers)  # Преобразуем число в строку
    digits_set = set(number_str)  # Создаем множество из символов строки
    print(digits_set)
    unik = len(digits_set)
    print(unik)
    min1 = min(digits_set)
    max1 = max(digits_set)
    print('Min: ', min, 'Max: ', max)

#4.	В зоопарке содержаться следующие виды животных:
# хищники (тигры, львы, волки и медведи), птицы (попугаи, совы, пеликаны, пингвины, орлы и фламинго) и
# травоядные (кролики, слоны, жирафы, зебры, носороги и косули).
# Составьте полный перечень всех животных в зоопарке, отсортированный в алфавитном порядке.
# Сколько млекопитающих содержится в зоопарке? Руководством зоопарка было принято решение
# всех сов и орлов перевести в соседний зоопарк, а вместо них привезти журавлей, пеликанов и павлинов.
# Отредактируйте список птиц в соответствии с произведенными изменениями, а также общий перечень всех животных зоопарка.

predators = {'Tiger', 'Lion', 'Wolf', 'Beer'}
birds = {'Parrots', 'Owl', 'Pelican', 'Pinguin', 'Eagle', 'Flamingo'}
herbivores = {'Rabbit', 'Elephant', 'Giraffe', 'Zebra', 'Rhinoceros', 'Roe'}
all_animals = predators | birds | herbivores
on_alpabet = sorted(all_animals)
print('All animals on alpabet: ', on_alpabet)
print('Count mlecopit: ', len(all_animals))
birds.discard('Owl') #удаляем элемент из множесва
birds.discard('Eagle')
birds.add('Crane')
birds.add('Pelican') #добавляем элемет в множество
birds.add('Peacok')
print('Update birds: ', birds)
all_animals = predators | birds | herbivores
print(all_animals)

