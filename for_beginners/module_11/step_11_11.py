numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))     # 1. Вывод длины списка
print(numbers[-1])      # 2. Вывод последнего элемента списка
print(numbers[::-1])    # 3. Вывод списка в обратном порядке

# 4. Проверяем, содержатся ли **оба** числа 5 и 17
if (5 in numbers) and (17 in numbers):
    print("YES")
else:
    print("NO")

# 5. Удаляем первый и последний элементы
del numbers[0]  
del numbers[-1] 
print(numbers)          # 6. Вывод списка после удаления




""" Все сразу 1 🌶️
Дополните приведённый ниже код, чтобы он:

Вывел длину списка;
Вывел последний элемент списка;
Вывел список в обратном порядке (вспоминаем срезы);
Вывел «YES» (без кавычек), если список содержит числа 
5 и 17, или «NO» (без кавычек) в противном случае;
Вывел список с удалёнными первым и последним элементами.
Примечание. Каждый вывод осуществлять с новой строки. """