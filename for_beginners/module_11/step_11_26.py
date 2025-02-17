n = int(input())
array = []

for _ in range(n):
    s = int(input())
    array.append(s)

negative = []
zeros = []
positiv = []
for line in array:
    if line < 0:
        negative.append(line)
    elif line == 0:
        zeros.append(line)
    else:
        positiv.append(line)
print(*negative, *zeros, *positiv, sep="\n")


""" Negatives, Zeros and Positives
На вход программе подаются натуральное число 
n
n, а затем 
n
n целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число 
n
n, а затем 
n
n целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи. """
