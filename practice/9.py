# Создаём кортеж cardinal_numbers с порядковыми числительными
cardinal_numbers = ("first", "second", "third")

# Выводим второй элемент кортежа (индексация начинается с 0, значит [1] — это "second")
print(cardinal_numbers[1])

# Распаковываем кортеж cardinal_numbers в три переменные
position1, position2, position3 = cardinal_numbers

# Выводим значения переменных, каждое с новой строки (за счёт sep="\n")
print(position1, position2, position3, sep="\n")

# Создаём строку my_name с именем "Pavel"
my_name = "Pavel"

# Преобразуем строку в кортеж, где каждая буква — отдельный элемент
my_name = tuple(my_name)

# Проверяем, есть ли буква "x" в кортеже my_name, и выводим результат (True или False)
print("x" in my_name)

# Создаём новый кортеж my_name_two, исключая первую букву (берём срез с 1-го индекса до конца)
my_name_two = my_name[1:]

# Выводим новый кортеж my_name_two
print(my_name_two)
print()

# Создаём список food с элементами "rice" и "beans"
food = ["rice", "beans"]

# Добавляем в список food элемент "broccoli"
food.append("broccoli")

# Расширяем список food ещё двумя элементами: "bread" и "pizza"
food.extend(["bread", "pizza"])

# Выводим последний элемент списка food, начиная с последнего
# food[-1:] — срез, который берёт последний элемент
print(food[-1:])  # ['pizza']

# Создаём строку str, которая содержит продукты через запятую
str = "eggs,fruit,orangejuice"

# Разделяем строку str на элементы по запятой и сохраняем в список breakfast
breakfast = str.split(",")

# Выводим количество элементов в списке breakfast (количество продуктов)
print(len(breakfast))  # 3

# Генератор списка для вычисления длины каждой строки из списка breakfast
lengths = [len(item) for item in breakfast]

# Выводим новый список lengths, который содержит длины строк из breakfast
print(lengths)  # [4, 5, 12]
print()

