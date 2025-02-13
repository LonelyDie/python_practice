from math import log

n = int(input())
num = 0
for i in range(1, n):
    num = num + (1 / (i + 1))

print((1 + num) - log(n))

""" Асимптотическое приближение 📉
На вход программе подаётся натуральное число 
n. Напишите программу, которая вычисляет значение выражения
Формат входных данных
На вход программе подаётся натуральное число 
n.

Формат выходных данных
Программа должна вывести единственное число в соответствии с условием задачи.

Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math. """
