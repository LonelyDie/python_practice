# Вывод длины строки
str1, str2 = "Animals", "Badger"
print(len(str1))

# Объединение строк и добавление пробела
str3 = str1 + " " + str2
print(str3)

# Объединение строк
str1 += str2
print(str1)

# Вывод строки zing
str4 = "bazinga"
print(str4[2:6])

# Преобразование строк к верхнему и нижнему регистру
str5, str6, str7, str8 = "Animals", "Badger", "HoneyBee", "HoneyBadger"
print(str5.lower(), str6.lower(), str7.lower(), str8.lower(), sep="\n") # Нижний регистр
print(str5.upper(), str6.upper(), str7.upper(), str8.upper(), sep="\n") # Верхний регистр

# Удаление пропусков
str9, str10, str11 = "    Filet Mignon", "Brisket    ", "  Cheeseburger   "
print(str9.lstrip(), str10.rstrip(), str11.strip(), sep='\n')

# Проверка наличия символов
str11, str12, str13, str14 = "Becomes", "becomes", "BEAR", "bEautiful"
print(str11.startswith("be"), str12.startswith("be"), str13.startswith("be"), str14.startswith("be"), sep="\n") # startswith() поиск по началу

# Проверка наличия символов и возвращение True для всех строк
str15, str16, str17, str18 = "Becomes", "becomes", "BEAR", "bEautiful"
str15 = "b" + str15[1] # Замена первого элемента 
str17 = "be" + str17[1:2] # Замена первых двух элементов
str18 = str18[0] + "e" + str18[2] # Объединение первого элемента и замена второго элемента
print(str15.startswith("be"), str16.startswith("be"), str17.startswith("be"), str18.startswith("be"), sep="\n") # startswith() поиск по началу

# Ввод от пользователя и вывод
say = input("Введите ")
print("Вы ввели " + say)

# Ввод от пользователя и вывод в нижнем регистре
say1 = input("Введите ")
print("Вы ввели " + say1.lower())

# Ввод от пользователя и вывод количество символов
say2 = input("Введите ")
print("Количество символов:", len(say2))

# Запрос у пользователя ввод первую букву, преобразование ее к верхнему регистру и выводит ее.
say3 = input("Скажи мне свой пароль: ")
say3 = say3[0:1] # Выбор первого симвала из слова
print("Первая буква, которую вы ввели, была:", say3.upper()) # Вывод верхнего регистра

# Преобразование строки в целое число вызовом int()
str19 = "2"
str20 = int(str19) * 2
print(str20)

# Преобразование строки в целое число вызовом float()
str21 = "2.0"
str22 = float(str21) * 2
print(str22)

# Создание строки и целого числа с выводом
str23 = "2"
print("Слово " + str(str20))

# Дважды вызыв input(), перемножение чисел и вывод результата
number_1 = input()
number_2 = input()
number_3 = int(number_1) * int(number_2)
print("The product of " + str(number_1) + " and " + str(number_2) + " is " + str(float(number_3)) + ".")