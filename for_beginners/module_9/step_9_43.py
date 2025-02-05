# Считываем первое слово
word1 = input()
weight1 = sum(ord(ch) for ch in word1)  # Считаем сумму кодов символов
heaviest_word = word1
heaviest_weight = weight1

# Считываем второе слово
word2 = input()
weight2 = sum(ord(ch) for ch in word2)
if weight2 > heaviest_weight:  # Если слово тяжелее текущего, обновляем
    heaviest_word = word2
    heaviest_weight = weight2

# Считываем третье слово
word3 = input()
weight3 = sum(ord(ch) for ch in word3)
if weight3 > heaviest_weight:
    heaviest_word = word3
    heaviest_weight = weight3

# Считываем четвёртое слово
word4 = input()
weight4 = sum(ord(ch) for ch in word4)
if weight4 > heaviest_weight:
    heaviest_word = word4
    heaviest_weight = weight4

# Выводим самое тяжёлое слово
print(heaviest_word)


""" Самое тяжёлое слово 🗿
Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode всех символов этого слова. Напишите программу, которая принимает 
4 слова и находит среди них самое тяжёлое слово. Если самых тяжёлых слов будет несколько, то программа должна вывести первое из них.

Формат входных данных
На вход программе подаются 
4 слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое тяжёлое слово в строке. """
