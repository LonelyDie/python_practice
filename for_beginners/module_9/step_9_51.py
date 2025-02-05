n = int(input())
for _ in range(n):
    class_name = input()
    if (
        len(class_name) == 2
        and '0' <= class_name[0] <= '9'
        and 'А' <= class_name[1] <= 'П'
    ):
        print('YES')
    else:
        print('NO')

""" Название класса 👩‍🏫🌶️
В школе BEEGEEK названия учебных классов необычные. Они имеют следующий формат:

<номер класса><буква класса>
где <номер класса> должен находиться в диапазоне от 
0
0 (как и все у программистов) до 
9
9 включительно, а буквой класса могут быть все буквы в диапазоне от «А» до «П» включительно.

Напишите программу, которая принимает натуральное число 
n
n, а далее 
n
n названий классов, каждое на новой строке. Для каждого названия класса ваша программа должна выводить на отдельной строке «YES» (без кавычек), если название класса корректное, или «NO» (без кавычек) в противном случае.

Формат входных данных
На вход программе подаются натуральное число 
n
n, а затем 
n
n названий классов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести на отдельной строке для каждого названия класса «YES» (без кавычек) или «NO» (без кавычек) в соответствии с условием задачи.

Примечание. Будем считать, что буквы Ё нет в русском алфавите, а значит, класс с такой буквой также будет считаться некорректным. 😢 """