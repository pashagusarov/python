"""
1. Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2
"""

# my_arr = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
#
# for i in my_arr:
#     print(type(i))


"""
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку 
до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. 
Главное: дополнить числа до двух разрядов нулём!
*(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). 
Эта задача намного серьёзнее, чем может сначала показаться.
"""

# my_arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

"""
Решение № 1 (с новым списком)-------------------------------------------------------------------------------------------
"""

# new_arr = []
#
# for el in my_arr:
#     if el.isdigit() or el[1:].isdigit():
#         if el[0] == '+' or el[0] == '-':
#             new_arr.append(f'"{el[0]}{int(el[1:]):02}"')
#         else:
#             new_arr.append(f'"{int(el):02}"')
#     else:
#         new_arr.append(el)
#
# print(' '.join(new_arr))

"""
Решение № 2 (без создания нового списка)--------------------------------------------------------------------------------
"""

# i = 0
#
# while i < len(my_arr):
#     el = my_arr[i]
#     if el.isdigit() or el[1:].isdigit():
#         my_arr.remove(el)
#         if el[0] == '+' or el[0] == '-':
#             my_arr.insert(i, f'"{el[0]}{int(el[1:]):02}"')
#         else:
#             my_arr.insert(i, f'"{int(el):02}"')
#     i += 1
#
# print(' '.join(my_arr))


"""
4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 
'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. 
Можно ли при этом не создавать новый список?
"""

# my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
#            'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# for i in my_list:
#     name = i.split()
#     print(f'Hi {name[-1].capitalize()}')

"""
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]
"""

"""
A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп 
(например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, 
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
"""

# my_list = [57.40, 6.51, 97, 49.32, 29.3, 11.98, 77.10, 12, 65.22, 98.05]
# for i, price in enumerate(my_list):
#     rub = int(price) // 1
#     kop = (float(price) - rub) * 100
#     print(f"{rub} рублей {kop:02.0f} копеек", end='')
#     if i != len(my_list) - 1:
#         print(', ', end='')

"""
B. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки 
остался тот же).
"""

# print(my_list)  # показываю исходный список
# print(id(my_list))  # показываю ID исходного списка
# my_list.sort()
# print(my_list)  # показываю отсортированный список
# print(id(my_list))  # доказываю, что объект остался тот же

"""
C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
"""

# print(my_list)
# print(id(my_list))
#
# my_new_list = sorted(my_list, reverse=True)
#
# print(my_new_list)
# print(id(my_new_list))

"""
D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""

# print(sorted(my_list, reverse=True)[:5])
