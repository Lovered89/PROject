
__author__ = 'Галай Денис Максимович'

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

# TODO: код пишем тут...
# import math
# # name = str(input("Введите имя!: "))
# # age = int(input("Введите возраст!: "))
# # if age==18:
# #     print(name,"18 лет")
# # else:
# #     age = age - 18
# #     last = abs(age) % 10
# #     print(name,"на", abs(age),end=" ")
# #     if (abs(age) <= 14 and abs(age) >= 11 or last >=5 and last <=9):
# #         print("лет",end=" ")
# #     else:
# #         if (last==1):
# #             print("год",end=" ")
# #         else:
# #             if (last==2 or last==3 or last==4):
# #                 print("года",end=" ")
# # if (age !=18 and age> 0):
# #     print("старше 18")
# # else:
# #     if (age != 18):
# #         print("младше 18")

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# TODO: код пишем тут...
# a = int (input("Введите первую переменную: "))
# b = int (input("Введите вторую переменную: "))
# c = int
# c = b
# b = a
# a = c
# print ("Новые значения!", a, b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# TODO: код пишем тут...
# import math
# a = int (input("Введите переменную A: "))
# b = int (input("Введите переменную B: "))
# c = int (input("Введите переменную C: "))
# x = int
# x1 = int
# x2 = int
# d = int
# d = b**2 - 4 * a * c
# if d>0:
#     d = (math.sqrt(d))
#     x1 = (-b + d)/ (2 * a)
#     x2 = (-b - d)/ (2 * a)
#     print("Уранение имеет два корня!: ", x1, x2)
# elif d==0:
#     x = - b / 2 * a
#     print("Уравние имеет один корень! ", x)
# else:
#     print("Не имеет корней!")

