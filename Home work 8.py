my_dict = {} #создаем пустой словарь
my_dict ["country"] = "Mexico"
print(my_dict)

#Дан словарь {0: 10, 1: 20}. Добавить в словарь ключ 2 со значением 30.
d = {0: 10, 1: 20}
d[2] = 30 # в [] ключ (добавляем значение ключа)
print(d)

#Дано три словаря: {1: 10, 2: 20}, {3: 30, 4: 40} и {5: 50, 6: 60}.
# Объединить данные словари в один.

d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
d3 = {5: 50, 6: 60}
d1.update(d2) #объеденяем словари
d1.update(d3)
print(d1)


#Дан словарь {'data1': 100, 'data2': -54, 'data3': 247}.
#Найти сумму значений словаря.

d4 = {'data1': 100, 'data2': -54, 'data3': 247}
values = d4.values()
print(values)
sum_v = sum(values)
print('Summa: ', sum_v)

#Дан словарь {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}.
# Найти 3 наибольших значения в нем.

d5 = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
values_d5 = d5.values()
print(values_d5)
sorted_v = sorted(values_d5, reverse=True)
print(sorted_v)
print('3 max elem: ', sorted_v[0:3])

#Дан словарь {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}.
# Создать новый словарь, который будет содержать только имя и зарплату сотрудника,
# а затем удалить эти значения из исходного словаря.

k = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
k_new = {'name': k.pop('name'), 'salary': k.pop('salary')}
print(k)
print(k_new)

#Дан словарь {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}.
#Переименовать ключ ‘city’ в ‘location’.

n = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
n['location'] = n.pop('city')
print(n)

#Дан словарь {'emp1': {'name': 'Jhon', 'salary': 7500},
#'emp2': {'name': 'Emma', 'salary': 8000},
#'emp3': {'name': 'Brad', 'salary': 6500}}.
#Измените значение зарплаты Брэда с 6500 до 8500

l = {'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}}
print(l['emp3'])
print(l['emp3'] ['salary'])
l['emp3'] ['salary'] = 8500
print(l)

#Дан словарь {‘v’: ‘s001’, ‘v1’: ‘s002’, ‘v2’: ‘s001’, ‘v3’: ‘s005’, ‘v4’: ‘s005’, ‘v5’: ‘s009’, ‘v6’: ‘s007’}.
# Выведите на экран все значения словаря таким образом, чтобы ни одно из них не повторялось.

m = {'v': 's001', 'v1': 's002', 'v2': 's001', 'v3': 's005', 'v4': 's005', 'v5': 's009', 'v6': 's007'}
m_v = m.values()
print(m_v)
sor = sorted(m_v)
print(sor)
print('vithout same values: ', sor[1:])


#Дан словарь {‘name’: ‘Alex’, ‘age’: 12, ‘class’: ‘v’, ‘roll_id’: ‘2’}.
# Проверить принадлежат ли следующие значения  словарю:
# ‘class’, ‘Alex’, ‘Michael’, ‘4’, 2, ‘2’, ‘age’, ‘address’, (‘name’, ‘Alex’), (‘class’, ‘x’)

p = {'name': 'Alex', 'age': 12, 'class': 'v', 'roll_id': '2'}
n = 'class' in p, 'Alex' in p, 'Michael' in p, '4' in p, '2' in p, '2' in p, 'age' in p, 'adress' in p
print(n)

# Дано два словаря: {‘Ten’: 10, ‘Twenty’: 20, ‘Thirty’: 30}
# и {‘Thirty’: 30, ‘Fourty’: 40, ‘Fifty’: 50}. Объедините эти словари в один

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

# Дан словарь {‘class’: {‘student’: {‘name’: ‘Mike’, ‘marks’: {‘physics’: 70, ‘history’: 80}}}}.
# Выведите на экран имя студента и его оценку по истории.

dict3 = {'class': {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}}
student_name = dict3['class']['student']['name']
marks = dict3['class']['student']['marks']['history']
print(student_name, marks)

# Дан словарь {‘gold’: 500, ‘pouch’: [‘flint’, ‘twine’, ‘gemstone’],
# ‘backpack’: [‘xylophone’, ‘dagger’, ‘bedroll’, ‘bread loaf’]}.
# Добавьте в словарь еще один элемент ‘pocket’, содержащий следующие значения:
# ‘seashell’, ‘strange berry’, ‘lint’.
# Отсортируйте значения, принадлежащие ключу ‘backpack’ и затем удалите из них значение ‘dagger’.
# Увеличьте  на 50 значение, принадлежащее ключу ‘gold’.

t = {'gold': 500, 'pouch': ['flint', 'twine', 'gemstone'],
     'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']}

t['pocket'] = ['seashell', 'strange berry', 'lint']
print(t)
print(t['gold'])
t['gold'] = 500*50
print(t)
sorted_backpack = sorted(t['backpack'])
print(sorted_backpack)
t['backpack'].remove('dagger')
print(t)