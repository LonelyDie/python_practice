n = int(input())
while n > 1000:
    a = n % 10
    n //= 10
print(n % 10)


""" Третья цифра 3️⃣
Дано натуральное число 

n(n>99). Напишите программу, которая определяет его третью (с начала) цифру.

Формат входных данных 
На вход программе подаётся одно натуральное число, состоящее как минимум из трёх цифр.

Формат выходных данных
Программа должна вывести его третью (с начала) цифру. """
