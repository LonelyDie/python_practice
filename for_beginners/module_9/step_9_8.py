char = input()
n = 0
m = 0

for i in char:
    if i in "+":
        n += 1
    if i in "*":
        m += 1

print(f"Символ + встречается {n} раз")
print(f"Символ * встречается {m} раз")

""" Сколько раз?
На вход программе подаётся одна строка. Напишите программу, которая определяет, сколько раз в строке встречаются символы + и *, и выводит текст в следующем формате:

Символ + встречается <n> раз
Символ * встречается <m> раз
где <n>, <m> – количество вхождений символов + и * в строку соответственно.

Формат входных данных
На вход программе подаётся одна строка.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи. """