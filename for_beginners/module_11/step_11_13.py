alphabet = []
for i in range(26):
    alphabet.append(chr(ord("a") + i) * (i + 1))

print(alphabet)

""" Алфавит
Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
Формат выходных данных
Программа должна вывести указанный список.

Примечание. Последний элемент списка должен состоять из 26 символов z. """
