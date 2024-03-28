#Написать функцию, которая выводит ряд Фибоначчи до заданной границы N.
#Например, для N = 15 ряд будет выглядеть следующим образом:
#0, 1, 1, 2, 3, 5, 8, 13.
def fib(N):
    a, b = 0, 1
    while a<N:
        print(a, end=' ')
        a, b = b, a + b
    print()
fib(15)
fib(25)
#Дана последовательность целых чисел. Найти минимальное
#среди простых чисел и максимальное среди чисел, не являющихся простыми
l = [3, 4, 5, 6, 7, 8, 10, 11]
def is_prime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True
def is_neutral(n):
    return n in [0, 1]
min_l = max(l) #10000000000
max_l = min(l) #-100000000000
for i in l:
    if is_neutral(i):
        continue
    is_pr = is_prime(i)
    if is_pr and i<min_l:
        min_l = i
    elif not is_pr and i>max_l:
        max_l = i
print('Min: ', min_l)
print('Max: ', max_l)

#Дана последовательность целых чисел. Найти среднее арифметическое
#совершенных чисел и среднее геометрическое простых чисел.
l = [3, 5, 6, 9, 8, 1, 4, 7]
def is_prime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

def is_neutral(n):
     return n in [0, 1]

min_l = max(l) #10000000000
max_l = min(l) #-100000000000
for i in l:
    if is_neutral(i):
        continue
    is_pr = is_prime(i)
    if is_pr and i<min_l:
        min_l = i
    elif not is_pr and i>max_l:
        max_l = i
print('Min: ', min_l)
print('Max: ', max_l)

#Дана последовательность целых чисел. Найти среднее арифметическое
#совершенных чисел и среднее геометрическое простых чисел.
l = [1, 4, 7, 9, 4, 2, 6, 9, 4, 9]

def is_prime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

def is_neutral(n):
     return n in [0, 1]
def is_perfect(n):
    s = 0
    for i in range(1, n):
        if n%i == 0:
            s += i
    return n == s
def sr_geom(l):
    res = 1
    for i in l:
        res *= i
    res **= 1/len(l)
    return round(res, 2)

perfect_nums = []
prime_nums = []

for i in l:
    if is_neutral(i):
        continue
    if is_prime(i):
        prime_nums.append(i)
    elif is_perfect(i):
        perfect_nums.append(i)
sr_arifm = sum(perfect_nums)/len(perfect_nums)
sr_g = sr_geom(prime_nums)
print('medium arifm: ', sr_arifm)
print('Medium geometr: ', sr_g)

#Дана последовательность целых чисел. Для каждого числа последовательности найти количество его делителей.
k = [1, 4, 7, 9, 4, 2, 6, 9, 8, 9]

def count_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

for num in k:
    print(f"Number of divisors for {num}: {count_divisors(num)}")
#Дана последовательность целых чисел. Найти в каждом числе сумму четных цифр.
m = [123, 134, 567, 888, 900, 1111, 5673]

def sum_of_number(num):
    sum_even = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            sum_even += int(digit)
    return sum_even

for number in m:
    print(f"Сумма четных цифр в числе {number}: {sum_of_number(number)}")

#Дана последовательность целых чисел.
# Для каждого числа последовательности проверить, представляют ли его цифры строго возрастающую последовательность.
h = [123, 134, 567, 888, 900, 1111, 5673]
def rise_number(num):
    num_str = str(num)
    for i in range(len(h)):
        if int(num_str[i]) >= int(num_str[i + 1]):
            return False
        return True

for num in h:
    if rise_number(num):
        print(f"Число {num} имеет строго возрастающую последовательность цифр.")
    else:
        print(f"Число {num} не имеет строго возрастающую последовательность цифр.")

#Дан диапазон целых чисел от n1 до n2. Найти факториал каждого третьего простого числа в заданном диапазоне.
def find_simple(n):
    s = True
    for i in range(2, n):
        if n%i == 0:
            s = False
            break
    return s

def factorial(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

l = range(30, 70)
k = 0
for i in l:
    if find_simple(i) == True:
        k += 1
        if k % 3 == 0:
            print('Число:', i)
            print('Факториал числа:', factorial(i))

#Дано натуральное число N.
# Уменьшить число в 2 раза (деление нацело) и проверить,
# изменилось ли после уменьшения количество разрядов в числе.
def count_digits(number):
    return len(str(number))

N = 10

# Уменьшить число в 2 раза (деление нацело)
N_divided_by_2 = N // 2

# Посчитать количество цифр в исходном числе N
digits_N = count_digits(N)

#  Посчитать количество цифр в числе, полученном после деления на 2
digits_N_divided_by_2 = count_digits(N_divided_by_2)

#Сравнить количество цифр исходного числа с количеством цифр числа после деления
if digits_N != digits_N_divided_by_2:
    print("Количество разрядов изменилось после уменьшения в 2 раза.")
else:
    print("Количество разрядов не изменилось после уменьшения в 2 раза.")