# 1.	Определите, сколько раз в тексте встречается заданное слово (рычит)
# (взять произвольный текст и проверить решение для 2-3 разных слов).



#2.	Дана строка. Проверить, сколько слов заканчивается на букву “я”.

l = "Я точно знаю, что мечты сбываются, ведь ты у меня есть"
l = l.replace(',', ' ')
l = l.replace('.', ' ')
print(l)
count = sum(1 for l in l if l.endswith("я") or l.endswith("Я"))
print("amount world 'я':", count)

#3.	Дана строка. Подсчитать количество букв “т” в строке.
k = "Я точно знаю, что мечты сбываются, ведь ты у меня есть"
count_t = len([char for char in k if char == 'т' or char == 'Т'])
print("amount 'т':", count_t)


#4.	Дана строка, состоящая из одного слова.
# Преобразуйте строку таким образом, чтобы все буквы были разделены между собой пробелами.

n = "слово"
split_world = ' '.join(n)
print(split_world)
