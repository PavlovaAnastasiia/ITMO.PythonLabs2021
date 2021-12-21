#import – позволяет клиентам (импортерам) получать модуль целиком.
#from – позволяет клиентам получать определенные имена из модуля.
import math
import statistics

help(math)
help(statistics)

#Напишите программу, в которой создайте список из десяти целых чисел.
import random

list = []
for i in (range(0,10)):
    list.append(random.randint(0,100))
print(list)

#подсчет суммы чисел списка, среднего значения,
#медианы (median) и стандартного отклонения (stdev)

print("Сумма - ",sum(list))
print("Мода - ",statistics.mode(list))
print("Среднее значение - ", sum(list)/10)
print("Медиана - ", statistics.median(list))
print("Стандартное отклонение - ", statistics.stdev(list))

#Реализуйте программу, в которой генерируется случайное число на интервале от 1 до 100.
#генерации числа используйте функцию randint модуля random.

a = random.randint(1,100)
print("Случайное число - ", a)