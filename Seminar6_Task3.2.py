# 3. Задача. Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ), применив лямбды, filter, map, zip, enumerate, списочные выражения.
# Seminar 1. Задача 1: Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list_1 = [1, 22, 3, 44, 553, 3, 33, 22, 63, 66, 23, 224, 6]

# sum_nechet = 0
# for i in range(len(list_1)):
#     if i % 2 != 0:
#         sum_nechet += list_1[i]

from functools import reduce
# sum_nechet = reduce(lambda x, y: x + y, filter(lambda c: ))

sum_nechet = reduce(lambda x, y: x + y, map(lambda x: x[0], filter(lambda x: x[1] % 2 != 0, zip(list_1, range(1, len(list_1)+1)))))
print(sum_nechet)