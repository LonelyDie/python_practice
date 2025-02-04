# Возведение в 3-ю степень
def cube(x):
    product = pow(x, 3)
    return product


a = int(input())
num = cube(a)
print(num)


# Вывод имени
def greet(name):
    print(f"Hello, {name}!")


b = input()
greet(b)


# Температура по шкале Фаренгейта
def convert_far_to_cel(F):
    C = (F - 32) * 5 / 9
    print(f"{F} degrees F = {C:.2f} degrees F")
    return F


F = int(input("Enter a temperature in degrees F: "))
convert_far_to_cel(F)


# Температура по шкале Цельсия
def convert_cel_to_far(C):
    F = C * 9 / 5 + 32
    print(f"{C} degrees C = {F:.2f} degrees F")
    return F


C = int(input("Enter a temperature in degrees C: "))
convert_cel_to_far(C)


# Целые числа от 2 до 10
for i in range(2, 11):
    print(i)

# Целые числа от 2 до 10
n = 1
while n < 10:
    n += 1
    print(n)


# Функция doubles(), которая получает число и увеличивает его вдвое
def doubles(num):
    return num3 * 2


num3 = int(input())
for _ in range(3):  # Трижды увеличиваем число
    num3 = doubles(num3)
    print(num3)


# Функция для расчета и вывода прибыли по вкладу
def invest(principal, rate, year):
    # Проходим по каждому году
    for year in range(1, (year + 1)):
        # Рассчитываем сумму с учетом годового процента
        principal = principal * (1 + rate)
        # Выводим результат, округленный до двух знаков после запятой
        print(f" year {year}: ${principal:.2f}")


# Запрашиваем данные у пользователя
principal = float(input("Введите основную сумму вклада: "))  # Основная сумма
annual_rate = (
    float(input("Введите процент вклада: ")) / 100
)  # Процент в виде десятичной дроби
num_years = int(input("На сколько лет: "))  # Количество лет

# Вызываем функцию invest с введенными данными
invest(principal, annual_rate, num_years)
