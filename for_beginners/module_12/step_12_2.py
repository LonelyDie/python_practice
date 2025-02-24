# Считывание первой строки и преобразование её в список целых чисел L
L = list(map(int, input().split()))

# Считывание второй строки и преобразование её в список целых чисел M
M = list(map(int, input().split()))

# Создание третьего списка, где каждый элемент - сумма соответствующих элементов L и M
result = [L[i] + M[i] for i in range(len(L))]

# Вывод элементов списка result в одну строку через пробел
print(" ".join(map(str, result)))


""" Сумма двух списков
На вход программе подаются две строки текста, содержащие целые числа. Из данных строк формируются списки чисел L и M. Напишите программу, которая создаёт третий список, элементами которого являются суммы соответствующих элементов списков L и M. Далее программа должна вывести каждый элемент полученного списка на одной строке через 
1 пробел.

Формат входных данных
На вход программе подаются две строки текста, содержащие целые числа, разделённые символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Количество чисел в обеих строках одинаковое. """
