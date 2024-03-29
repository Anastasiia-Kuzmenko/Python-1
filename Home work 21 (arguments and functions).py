"""
Написать функцию, принимающую некоторое целое число и вычисляющую по умолчанию
сумму его четных цифр. Предусмотреть возможность изменения поведения функции таким образом,
чтобы она также могла вычислять сумму нечетных цифр.

-------------
Тестовые значения:
N = 9874023, even_sum=14, odd_sum = 19
N = 38271, even_sum=10, odd_sum = 11
N = 123456789, even_sum=20, odd_sum = 25
"""
def digit_sum(N, even=True):
    s = 0 #сумма цифр и значально =0
    while N>0:
        cur_digit = N%10
        if even and cur_digit%2 == 0:
            s += cur_digit
        elif not even and cur_digit%2 != 0:
            s += cur_digit
        N //= 10
    return s
print(digit_sum(9874023))
print(digit_sum(38271))
print(digit_sum(123456789))

print(digit_sum(9874023, even=False))
print(digit_sum(38271, even=False))
print(digit_sum(123456789, even=False))

#Написать функцию, приримающую произвольное количество
#целых чисел и возвращающую наибольшее положительное из них кратное 13

def find_numb(*args):
    max = -1
    for i in args:
        if i>0 and i%13 == 0 and i>max:
            max = i
    if max != -1:
        return max
    return 'no such numbers'
print(find_numb(2, 7, 0, 3, 1, 5, -13))

"""
Написать функцию, принимающую некоторую информацию о геометрической фигуре и
рассчитывающую площадь данной фигуры.


- Ромб с диагоналями d1 и d2 (s = (d1*d2) / 2)
- Квадрат со стороной c (s=c2)
- Трапеция с основаниями a,b и высотой h (s = ½ *(a+b)*h)
- Круг с радиусом r (s=Pi*r2)

------------------
Тестовые значения:
figure_type = 'rhombus', d1=10, d2=8        -> S = 40
figure_type = 'square', a=5                 -> S = 25
figure_type = 'trapezoid', a=12, b=3, h=6   -> S = 45
figure_type = 'circle', r=18                -> S = 1017
figure_type = 'unknown', a=1, b=2, c=3      -> invalid data
"""
from  math import pi
def square(figure_type, **kwargs):
    if figure_type == 'rhombs':
        return kwargs['d1'] * kwargs['d2']/2
    if figure_type == 'square':
        return kwargs['a']**2
    if figure_type == 'trapezoid':
        return 1/2*(kwargs['a']+kwargs['b'])*kwargs['h']
    if figure_type == 'circle':
        return pi*kwargs['r']**2
    if figure_type == 'unknown':
        return 'invalid data'


print(square(figure_type = 'rhombs', d1 = 10, d2 = 8))
print(square(figure_type = 'square', a = 5))
print(square(figure_type = 'trapezoid', a = 12, b = 3, h = 6))
print(square(figure_type = 'circle', r=18))
print(square(figure_type = 'unknown', a=1, b=2, c=3))

#Напишите программу, осуществляющую проверку логина и пароля для входа в систему.
# Проверка введенных пользователем данных должна осуществляться в отдельной функции,
# принимающей следующие параметры: имя пользователя, пароль, количество попыток входа
# в систему (по умолчанию 3), сообщение, выводимое пользователю  в случае, если все
# попытки входа в систему исчерпаны (по умолчанию: “Система заблокирована. Повторите попытку через 5 мин.”)
"""""
def check(login, password, max_attempt=3, failured_message='Система заблокирована. Повторите попытку через 5 мин.'):
    attempts = max_attempt
    while attempts > 0:
        if login == 'admin' and password == 'password123':
            print('Вход выполнен успешно!')
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f'Неверный логин или пароль. Осталось попыток: {attempts}')
                login = input('Введите имя пользователя: ')
                password = input('Введите пароль: ')
            else:
                print(failured_message)
                return False

def main():
    login = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')

    check(login, password)

if __name__ == "__main__":
    main()
"""""

#Напишите функцию, принимающую сведения об авторе
# (в виде произвольного списка именованных аргументов)  и выводящая их на экран в указанном формате:
#И. О. Фамилия (дата рождения - дата смерти) - краткая информация
#Например: А. С. Пушкин (6.06.1799 - 10.02.1837) - русский поэт,
# драматург и прозаик. И. Соболь (24.08.1939) - израильский драматург, писатель и режиссер.
def autor(name, birth_date, death_date=None, **kwargs):
    # Создаем строку для имени автора
    initials = ''.join([x[0].upper() + '.' for x in name.split()])
    # Создаем строку для дат
    date_string = f' ({birth_date}'
    if death_date:
        date_string += f' - {death_date}'
    date_string += ')'

    # Составляем информацию об авторе
    info = kwargs.get('info', '')

    # Выводим информацию об авторе
    print(f'{initials} {date_string} - {info}')
autor('Александр Сергеевич Пушкин', '6.06.1799', '10.02.1837', info='русский поэт, драматург и прозаик')
autor('Исаак', '24.08.1939', info='израильский драматург, писатель и режиссер')


#Напишите функцию, которая может принимать произвольное количество аргументов (целых чисел),
# и определять, сколько среди них двузначных и трёхзначных чисел. Определение количества
# разрядов в числе также оформить в виде отдельной функции.
def count_digits(number):
    return len(str(number))

def number(*args):
    two_digit_count = 0
    three_digit_count = 0

    for num in args:
        num_digits = count_digits(num)
        if num_digits == 2:
            two_digit_count += 1
        elif num_digits == 3:
            three_digit_count += 1

    return two_digit_count, three_digit_count

# Пример использования функции
two_digit, three_digit = number(10, 99, 100, 101, 999, 1000)
print(f'Количество двузначных чисел: {two_digit}')
print(f'Количество трехзначных чисел: {three_digit}')
