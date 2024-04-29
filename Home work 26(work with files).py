# Создать текстовый файл и записать в него n вещественныз чисел
file_name = 'res_1.txt'
l = [4.5, 7.6, 8.7, 6.8]
def get_line(l):
    l = list(map(str, l))
    return ' '.join(l)
with open(file_name, 'w') as f:
    f.write(get_line(l))
print('Done!')

#В текстовом  файле nums.txt хранятся вещественные числа.
#Вывести их на экран и вычислить их колличество
file_name = 'res_1.txt'
with open(file_name, 'r') as f:
    nums = f.read()
print(nums)
nums_list = list(map(float, nums.split( )))
print(nums_list)
print(len(nums_list))

#В файле nums.txt хранятся вещественные числа. Дописать в файл эти же числа, упорядочив их по возрастанию.
import os
relative_path = "nums.txt"
absolute_path = os.path.abspath(relative_path)

with open(relative_path, 'r') as file:
    lines = file.readlines() #открываем файл для чтения
numbers = []
for line in lines:
    try:
        number = float(line.strip())
        numbers.append(number)
    except ValueError:
        continue
numbers.sort()
print(numbers)
with open(relative_path, 'a') as file:
    file.write('\n')
    for number in numbers:
        file.write(f'{numbers}\n')
print(file)

#Создать двоичный файл nums.dat и записать в него целое число n, а затем в следующей строке n вещественных чисел.
file_name = 'nums.dat'
n = 5
with open('nums.dat', 'a', encoding='utf-8') as f:
    data = '5'
    f.write(data)
print('Done')

#Вывести на экран содержимое созданного в предыдущей задаче двоичного файла.

with open('nums.dat', 'r') as file:
    read_file = file.read()
print(read_file)

#В файле matrx.txt построчно хранится матрица целых чисел A(n,n). Найти два наибольших простых числа.
# Первое из них заменить минимальным элементом матрицы, а второе - максимальным элементом.
# Записать полученную матрицу в файл result.txt.

with open("/Users/anastasia/Downloads/mtrxs.txt", "r") as my_file:
  file_contents = my_file.read()
print(file_contents)

def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n