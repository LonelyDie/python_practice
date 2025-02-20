array = []
n = int(input())
for i in range(n):
    array.append(int(input()))

array.remove(min(array))
array.remove(max(array))
print(*array, sep="\n")


""" Remove outliers
При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.

На вход программе подаются натуральное число 
n, а затем 
n различных натуральных чисел. Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

Формат входных данных
На вход программе подаются натуральное число 
n, а затем 
n различных натуральных чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи. """
