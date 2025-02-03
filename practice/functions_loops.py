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

def doubles(num):
    total = 0
    for i in range(num):
        total += num
    return total


num3 = int(input())
doubles(num3)

