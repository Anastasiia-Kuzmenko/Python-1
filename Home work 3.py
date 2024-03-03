import math
a = 0
a_rad = math.radians(a)

y = math.cos(3/8 * math.pi - a_rad/4)**2 - math.cos(11/8*math.pi + a_rad/4)**2
print('y = ', y)

z = math.sqrt(2)/2 * math.sin(a_rad/2)
print('z = ', z)

x = 5
m = (math.pow(x, 2) + 2 * x - 3 + (x + 1) * math.sqrt(x**2 - 9)) / (math.pow(x, 2) + 2 * x - 3 + (x + 1) * math.sqrt(x**2 - 9))
print('m = ', m)

l = math.sqrt((x + 3) / (x - 3))
print('l = ', l)

k = (math.log2(8) + math.log2(18)) / (2 * math.log2(2) + math.log2(3))
print('k = ', k)

#Вычисление площади треугольника
a = 5
h = 4
S = 1/2 * a * h
print('S = ', S)
#Вычисление площади круга через радиус
r = 2
L = math.pi * r**2
print('L = ', L)

# Две сосны растут в 21 метре одна от другой.
# Высота одной сосны - 27 метров, другой - 7 метров.
# Найти расстояние между их верхушками
a = 21
b = 27
c = 7
d = math.sqrt(a**2 + b**2 + c**2)
print('d = ', d)