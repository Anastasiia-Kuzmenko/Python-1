i = 5
while i < 6:
    print(i)
    i += 1 # что бы не было зацикливания

#Вывести на экран значения функции
		#y = (e^sin(x)) * cos()

#на отрезке [0, П] с шагом 0.1.

from math import pi, e, sin, cos
x = 0
while x <= pi:
    y = e**sin(x) * cos(x)
    print(round(x, 2), round(y, 3))
    x += 0.1
#Найти наибольший общий делитель (НОД) натуральных чисел А и В

