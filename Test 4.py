"""
#Напишите программу, которая спрашивала бы у пользователя его имя, пол, возраст и место жительства,
# а затем выводила бы полученную информацию на экран в следующем формате:
#This is [name].
#He (she) is [age] years old.
#He (she) lives in [city].

name = input('Enter yor name')
sex = input('Enter your sex (m/f): ')
age = input('Enter your age: ')
adress = input('Enter your adress')
print()
print(f'This is {name}')
print(f'{"He" if sex == "m" else "She"} is {age} years old.')
print(f'{"He" if sex == "m" else "She"} lives in {adress}.')

"""
#Напишите программу, которая предлагает пользователю решить пример: 4*100-54. В случае,
# если пользователь ошибается, программа должна вывести соответствующее сообщение и правильный ответ.
# А в случае, если пользователь прав, - поздравить его с правильным ответом.
"""
print('4*100 - 54')
user_answer = int(input('Your answer: '))
corect_answer = 4*100 - 54
if user_answer == corect_answer:
    print("Congratulations! That's a correct answer!")
else:
    print("Unfortunately, that's a wrong answer : -(")
    print(f"The correct answer is {corect_answer}")
"""
"""
#Напишите программу, “угадывающую” число, задуманное пользователем. Программа должна работать следующим образом:
#a.	после запуска пользователь получает приглашение загадать двузначное число.
#b.	программа поэтапно просит пользователя разделить задуманное число на 3, 5 и 7 и ввести полученные остатки от деления.
#c.	программа умножает полученные значения на 70, 21 и 15 соответственно, и складывает результаты.
#d.	программа делит полученную сумму на 105 и выводит остаток от деления на экран вместе с сообщением о том, что задуманное число отгадано.

input('Guess a two-digit number and press Enter button for continue...')
ost3 = int(input('Divide the conceived number by 3 and enter the remainder: '))
ost5 = int(input('Divide the conceived number by 5 and enter the remainder: '))
ost7 = int(input('Divide the conceived number by 7 and enter the remainder: '))

res = (ost3 * 70 + ost5 * 21 + ost7 * 15) % 105
print('*'*30)
print(f'You guessed a number {res}')
"""
"""
#Напишите программу, запрашивающую у пользователя 4 числа.
# Отдельно сложите первые два числа, а затем вторые два числа.
# Разделите первую сумму на вторую и выведите результат на экран так,
# чтобы ответ содержал знак и две цифры после запятой.

num1 = int(input('Plese enter the first number: '))
num2 = int(input('Plese enter the second number: '))
num3 = int(input('Plese enter the three number: '))
num4 = int(input('Plese enter the four number: '))
res1 = num1 + num2
res2 = num3 + num4
res= res1/res2
print('The result is {:+.2f} '.format(res))
"""

#Результаты экзамена хранятся в словаре: {‘John’: 75, ‘Ann’: 80, ‘Ally’: 60}.
# Используя форматированный вывод, выведите результаты экзамена сначала в одной строке,
# а затем построчно для каждого студента. При этом результаты должны быть отсортированы в
# порядке убывания полученных баллов.

exam_res = {'John': 75, 'Ann': 80, 'Ally': 60}
exam_res_sorted = sorted(exam_res.items(), key=lambda pair: pair[1], reverse=True)
print(exam_res_sorted)
exam_res_str = ', '.join(map(lambda item: f'{item[0]} - {item[1]}', exam_res_sorted))
print(f'Exam results: {exam_res_str}')
print('*'*50) #разделитель
print('Exam results: ')
for elem in exam_res_sorted:
    print(f'{elem[0]} - {elem[1]}')
"""
#Дан кортеж, состоящий из 4х элементов: (2, 123.4567, 10000, 12345.67).
# Используя форматированный вывод, преобразуйте данные значения в следующую строку:
#‘File_002 :      123.46,  1.00e+04,  1.23e+04’

l = (2, 123.4567, 10000, 12345.67)
tmpl = 'File_{0:03} :\t{1:.2f}, \t{2:.e}, \t{3:.2e}'
print(tmpl.format(*l))
"""
"""
#Решите предыдущую задачу, используя поочередно другие два метода форматирования строк.
l = (2, 123.4567, 10000, 12345.67)
#method format()
tmpl = 'File_{0:03} :\t{1:.2f}, \t{2:.e}, \t{3:.2e}'
print(tmpl.format(*l))

#f-string
print('\nf-strings:')
print(f'File_{[0]:03} :\t{l[2]:.2e}, \t{l[2]:.2e}, \t{l[3]:.2e}')

#old style
print('\n0ld style: ')
print('File_%03d :\t%.2f, \t%.2e, \t%.2e' % l)

"""

#Дана последовательность чисел (количество чисел может изменяться).
# Используя форматированный вывод, выведите на экран количество чисел в последовательности, а затем и сами числа.
#Например, для чисел (2, 3, 5) вывод может иметь следующий вид:
#“The 3 numbers are: 2, 3, 5.”


