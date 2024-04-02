# Написать рекурсивную функцию возведения числа в целую степень
def pow(a, n): #а - число которое возводим в степень, n - степень в которую возводим
    if n == 0:
        return 1
    if n<0:
        return 1/pow(a, -n)
    return a*pow(a, n-1)
print(pow(3, 4))

#написать рекурсивную функцию для нахождения n-го числа Фибоначчи
# Тестовое значение 1 1 2 3 5 8 13 21 34 55 89

def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(3))

#Написать рекурсивную функцию подсчета суммы элементов списка чисел.

def sum_elem(lst):
    if len(lst) == 0:  # базовый случай: если список пустой, возвращаем 0
        return 0
    else:
        return lst[0] + sum_elem(lst[1:])  # добавляем первый элемент к сумме остальных элементов

my_list = [1, 2, 3, 4, 5]
print("Сумма элементов списка:", sum_elem(my_list))

#Написать рекурсивную функцию подсчета суммы цифр положительного целого числа.
def sum_digits(num):
    return num%10 + sum_digits(num//10) \
        if num > 9 \
        else num
print(sum_digits(18))

#Написать рекурсивную функцию подсчета суммы первых n  членов гармонического ряда:
def nth_harmonic_rec(n):
    if n == 1: #граничный случай
        return 1
    else: #рекурсивный случай
        return 1 / n + nth_harmonic_rec(n - 1)
print(round(nth_harmonic_rec(7)))