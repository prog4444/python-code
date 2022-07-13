"""# Дни недели пронумерованы следующим образом: 1 — понедельник, 2 — вторник, …, 6 — суббота, 7 — воскресенье.
# Дано целое число K, лежащее в диапазоне 1–365.
# Определить номер дня недели для K-го дня года, если известно, что в этом году 1 января было субботой.
import random
week_days = {
    1: 'понеделник',
    2: 'вторник',
    3: 'среда',
    4: 'четверг',
    5: 'пятниса',
    6: 'суббота',
    7: 'воскресения'
}
k = random.randrange(1, 366)
k = 31
i = (1+4) % 7 + 1
print("1-e января: ", 1)
print("номер дня надели:", i)
print("день недели:", week_days[i])
i = (k + 4) % 7 + 1
print()
print("номер дня года: ", k)
print("номер дня надели:", i)
print("день недели:", week_days[i])"""

"""def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, -1))  # => None"""

"""# For7. Даны два целых числа A и B (A < B).
# Найти сумму всех целых чисел от A до B включительно.
a = 1
b = 20
s = 0
for i in range(1, 20):
    if i % 2 == 0:
        s += i
        print(i)
print(s)"""

# calculator

"""a = int(input("Ракамро дароред: "))
b = int(input("операторро дароред: "))
c = int(input("Ракамро дароред: "))"""

"""a = 6
b = 5

print( 'Addition:\t', a, '+', b, '=', a + b)
print( 'Subtraction:\t', a, '-', b, '=', a - b)
print('Multiplication:\t', a, 'x', b, '=', a * b)
print( 'Division:\t' , a, '÷', b, '=', a / b)
print( 'Floor Division:\t', a, '÷', b, '=', a // b)
print('Modulus:\t', a, '%', b, '=', a % b)
print( 'Exponent:\t ', a, '² = ', a ** b, sep = '')"""

"""# For8. Даны два целых числа A и B (A < B).
# Найти произведение всех целых чисел от A до B включительно.
a = int(input("a:"))
b = int(input("b:"))
s = 0
for i in range(a, b):
    if i % 2 == 0:
        s += i
        print(i)
print(s)"""

"""# For9. Даны два целых числа A и B (A < B).
# Найти сумму квадратов всех целых чисел от A до B включительно.
import math
a = int(input("a: "))
b = int(input("b: "))
s = 0
for i in range(a, b + 1):
    s = s + i**2
    print(i**2)"""

"""# For10. Дано целое число N (> 0).
# Найти сумму  1 + 1/2 + 1/3 + … + 1/N
n = int(input("n: "))
s = 1
for i in range(1, n):
    s = s + i
    print(i)
print(s)"""

"""print("_________________")      
print("_________________")
print("||")
print("||")
print("||")
print("||")
print("||")
print("||")
print("_________________")
print("_________________")"""

"""i = 0
for i in range(1, 100):
    if i % 5 == 0:
        print(i)
    elif i % 3 == 0:
        print(i)"""

"""a = [1, 3, 5, 7]
a.reverse()
print(a)"""

"""# 1 2 3 4 5 || 6 7 8 9

# i = 1
# while i < 6:
# print(i)
# i = i + 1

a = int(input())
b = int(input())
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)"""

"""# Begin22
a = 4
b = 9
print(a + 5)
print(b - 5)"""

"""# Begin - 15
d = 7
p = 3.14
L = p * d
print("Длину L:", L)
s = (p * (d * 2) / 4)
print("Площад круга S:", s)"""

"""# Boolean10°. Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное»
a = 8
b = 10
if a == b:
    print("true")
else:
    print("false")"""

"""# For6. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1.2, 1.4, …, 2 кг конфет.
g = 10
for i in range(10, 20):
    if i % 2 == 0:
        s = i / g
        print(s, "кг конфет", i, "сомони")"""

"""# For3. Даны два целых числа A и B (A < B).
# Вывести в порядке убывания все целые числа,
# расположенные между A и B (не включая числа A и B),
# а также количество N этих чисел.
a = 8
b = 20
for i in range(8, 20):
    if i % 2 == 1:
        print(i-20)"""

"""# Begin 20
import math
x1 = int(input("раками x1 дароред: "))
y1 = int(input("раками y1 дароред: "))
x2 = int(input("раками x2 дароред: "))
y2 = int(input("раками y2 дароред: "))
s = math.sqrt(x2 - x1) * 2 + (y2 - y1) * 2
print("расстояние между двумя точками с заданными координатами", s)"""


"""def button_press():
    print("кнопка нажата")
from tkinter import *
tk = Tk()
b1 = Button(tk, text="нажми меня!", command=button_press)
b1.pack()"""

"""# For33.
# Дано целое число N (> 1). Последовательность чисел Фибоначчи FK  (целого типа) определяется следующим образом:
a = 0
b = 1
n = int(input("enter no.of fibonacci to be generator :"))
if n <= 0:
    print("not possible")
elif n == 1:
    print(a)
elif n >= 2:
    print("{},{}".format(a, b), end='')
    for i in range(2, n):
        c = a + b
        print(",{}".format(c), end='')
        a = b
        b = c"""

"""# For4.
# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1,  2, …, 10 кг конфет.
nums = 10
for i in range(1, 10):
    f = i * 6
    print(i, "kg konfet", f, "somoni")"""

"""a = int(input("a:"))
b = int(input("b:"))
for i in range(a):
    if b > a:
        print(i)
    i = i + a
print(i)"""

"""a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for elem in a:
    if elem < 5:
        print(elem)


print([elem for elem in a if elem < 5])

print(list(filter(lambda elem: elem < 5, a)))"""

"""a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = [elem for elem in a if elem in b]"""

"""# Begin 21
import math
x1 = 4
y1 = 5
x2 = 5
y2 = 4
x3 = 3
y3 = 1
e = math.sqrt((x2 - y1) + (x2 - y2) + (x3 - y3))
print(e)
a = 5; b = 6; c = 6
p = (a + b + c) / 2
print(p)
p = 7
s = math.sqrt(p * (p - a) * (p - b) * (p * c))
print(s)"""

"""def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)
    print(fibb(10))

fibb(1)"""

"""# Integer4.
# Даны целые положительные числа A и B (A > B).
# На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений).
# Используя операцию деления нацело, найти количество отрезков B, размещенных на отрезке A.
a = (int(input()))
b = (int(input()))
if a > b:
    a = 2 % 3
    print(b)
else:
    print(a)"""

"""import math as m
m.sin(m.pi/3)
print(m)"""

"""# For2. Даны два целых числа A и B (A < B).
# Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B),
# а также количество N этих чисел.
n = 0
for i in range(20):
    if i % 2 == 0:
        n += 1
        print(i)
print(n)"""

"""# Begin 18 Абрамян
a = 4
b = 5
c = 9
d = a * c + b * c
print("Длина ", d)"""

"""my_list = [1, 5, 3, 2, 4]
if len(my_list) % 2 != 0:
    print(max(my_list)**2)
else:
    print(min(my_list)*3)"""

"""# For5°. Дано вещественное число — цена 1 кг конфет.
# Вывести стоимость 0.1, 0.2, …, 1 кг конфет
g = 10
for i in range(1, 10):
    s = i / g
    print(s, "kg konfet", i, "somoni")"""

"""i = 1
while i < 4:
    print('\nOuter Loop Iteration:', i)
    i += 1
    j = 1
    while j < 4:
        print('\tInner Loop Iteration:', j)
        j += 1"""

"""global_var = 1


def my_vars():
    print('Global Variable:', global_var)


local_var = 2
print('Local Variable:', local_var)

global inner_var
inner_var = 3

my_vars()
print('Coerced Global:', inner_var)"""

"""from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ['Name', 'Age', 'City']
table.add_row(["Alice", 20, "Adelaide"])
table.add_row(["Bob", 20, "Brisbane"])
table.add_row(["Chris", 20, "Cairns"])
table.add_row(["David", 20, "Sydney"])
table.add_row(["Ella", 20, "Melbourne"])
print(table)
table.align = 'r'
print(table)
table.sortby = "City"
print(table)"""

"""# Begin21
import math
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))
r = math.sqrt(x2 - x1) * 2 + (y2 - y1) * 2 + (x3 - y3) * 2
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("периметр: ", r)
print("p: ", p)
print("s: ", s)"""

"""# Begin12. Даны катеты прямоугольного треугольника
# a и b. Найти его гипотенузу c и периметр P:  c = (реша бардор)a^2 +b^2 , P = a + b + c.
import math
a = 5
b = 6
c = math.sqrt(a**a+b**b)
p = a + b + c
print("P:", p)"""

"""# Дано целое положительное число. Проверить истинность высказывания: «Данное число является нечетным трехзначным».
a = 7
b = 4
c = 9
if a > b < c:
    print("da")
else:
    print("net")"""
print(4)








