# Вывод числа с разделителям-подчеркиванием и без
num1 = 25000000 
num2 = 25_000_000
print(num1, num2, sep='\n') 

# Литерал с плавающей точкой
num = 1.75e5
print(num)

# Вывод минимальной степени бесконечности 
num = 2e309
print(num)

# Возведения первого числа в степень, заданную вторым числом
num1 = float(input("Enter a base: "))
num2 = int(input("Enter an exponent: "))
num3 = num1**num2
print(f"{num1} to the power of {num2} = {num3}")

# Абсолютное значение этого числа
num1 = float(input("Enter a number: "))
num2 = abs(num1)
print(f"The absolute value of {num1} is {num2}")

# Является ли разность двух чисел целым числом и разность которых не является целым числом
num1 = float(input("Enter a base: "))
num2 = float(input("Enter another number: "))
num3 = num1 - num2
num4 = num3.is_integer()
print(f"The difference between {num1} and {num2} is an integer? {num4}!")

# Округление до 2-х цифр
num1 = float(input("Enter a base: "))
num2 = round(num1, 2)
print(f"{num1} rounded to 2 decimal places is {num2}")

# Вывод фиксированной точки с тремя знаками в дробной части
num = 3**0.125
print(f"{num:.3f}")

# Вывод с двумя знаками в дробной части
num = 150000 
print(f"{num:,.2f}")

 # Вывод в % без дробной части
num = 2/10
print(f"{num:.0%}") 