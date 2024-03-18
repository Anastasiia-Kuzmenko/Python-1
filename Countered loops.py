# Вычислить факториал числа N
# N! = 1 * 2 * 3 * ... * N
N = 8
f = 1
for i in range(2, N + 1): # начинаем с 2 т.к. N присвоено 1
    f *= i
print(N, '!=', f)

#Дано натуральное число N. Определить количество делителей этого числа K, не равных ему самому.
#Например, для N = 12 такие делители: 1, 2, 3, 4, 6, а их количество K = 5.
#Тестовые данные:
#12 (1, 2, 3, 4, 6) = 5
#20 (1,2,4,5,10) = 5
#35 (1,5, 7) = 3

N = 12
K = 0 #кол-во делителей числа (изначально 0)
for i in range(1, N//2+1):
    if N%i == 0:
        K += 1
print(K)

#Дана последовательность из N вещаственных чисел.
# Определить наибольший элемент последовательности
l = [10.4, 46.6, 4.5, 6.8, 8.99]
max = l[0]
for i in range(1, len(l)):
    if l[i]>max:
        max = l[i]
print(max)

#Вычислить сумму натуральных четных чисел, не превышающих N.

n = 100
total_sum = 0
for i in range(2, n + 1, 2):
    total_sum += i
print(total_sum)

#Дано натуральное число N. Определить, является ли оно простым.
number = -1
prostoe = True

for i in range(2, number // 2 + 1):
    if number % i == 0:
        prostoe = False
        break
if prostoe and number > 1:
    print(f'Число {number} является простым.')
else:
    print(f'Число {number} не является простым.')

#Дана последовательность целых положительных чисел. Определить количество простых чисел в последовательности

k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_prime = 0

for num in k: #num каждое число из последовательности которое проверяем на простоту
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count_prime += 1

print('Количество простых чисел в последовательности:', count_prime)

#Дана последовательность целых чисел.
# Найти наименьшее число среди положительных элементов последовательности.
# Если присутствует несколько одинаковых наименьших элементов, то определить их количество.

m = [-11, 2, -3, 2, -5, -6, -7, -8, -9, -10]
min_positive = float('inf')  # Используем бесконечность для начального значения
count_min_positive = 0
sum_min_positive = 0
for i in m:
    if i > 0:
        if i < min_positive:
            min_positive = i
            count_min_positive = 1
            sum_min_positive = i
    elif i == min_positive:
            count_min_positive += 1
            sum_min_positive += i
if min_positive != float('inf'):
    print("Наименьшее положительное число:", min_positive)
    print("Количество таких чисел:", count_min_positive)
    print("Сумма таких чисел:", sum_min_positive)
else:
    print("В последовательности отсутствуют положительные числа.")
