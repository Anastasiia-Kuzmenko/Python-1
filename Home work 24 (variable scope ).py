"""
Написать функцию, принимающую в качестве своего параметра название игральной карты
(6, 7, 8, 9, 10, В, Д, К, Т) и проверяющую набрал ли игрок за текущий ход 21 очко.
Если набрано меньше, вывести на экран предложение вытянуть еще одну карту.
Если больше - сообщение о проигрыше. Если ровно 21 очко - сообщение о выигрыше.
Внутри данной функции определить еще одну функцию, которая будет возвращать числовой эквивалент вытянутой карты.
Решить задачу с использованием локальных, глобальных и нелокальных переменных.
"""

points = 0
def game(card, max_sum=21):
    def get_current_points():
        points = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'V': 2, 'D': 3, 'K': 4, 'T': 11}
        if card in points.keys():
            return points[card]
        return 0
    global points
    points += get_current_points()
    if points < max_sum:
        print('Try another card...')
    elif points > max_sum:
        print('You lose!')
    else:
        print('You win!')
game('T')
game('10')


# Написать функцию cylinder(), которая вычисляет площадь цилиндра.
# В теле cylinder() определить функцию circle(), вычисляющую площадь круга.
# В одном из передаваемых параметров в функцию cylinder() пользователь должен определять,
# нужно ли вычислить только площадь боковой поверхности цилиндра  или полную площадь цилиндра.
# Решить данную задачу, определяя площадь S как глобальную, локальную и нелокальную переменную.
# Определить значение Pi как константу.

PI = 3.14
def circle(R):
    return PI * R**2
s = 0
def cylinder(R, h, full_area=True):
    global s
    lateral_area = 2 * PI * R * h
    if full_area:
        s = circle(R) * 2 + lateral_area
    else:
        s = lateral_area
    return s


R = 9
h = 7
print("Lateral surface area:", cylinder(R, h, full_area=False))
print("Total area of the cylindre:", cylinder(R, h))