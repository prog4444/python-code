import math

""" Begin 23
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
Te = a
a = b
b = c
c = a
print(a)
print(b)
print(c)"""

""" Begin 24
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
pop = a
a = c
c = b
b = a
print(a)
print(b)
print(c)"""

"""# Begin 25
x = int(input("x:"))
y = (3 * x ** 6) - (6 * x ** 2 - 7)
print(y)"""

"""# Begin 26
x = int(input("x:"))
y = 4 * (x - 3) ** 6 - 7 * (x - 3) ** 3 + 2
print(y)"""

"""# Begin 27
a = int(input("a:"))
a2 = a ** 2
a4 = a ** 4
a8 = a ** 8
print('Значение A в степени 2 равно: ', a2)
print('Значение A в степени 4 равно: ', a4)
print('Значение A в степени 8 равно: ', a8)"""

"""# Begin 28

a = int(input("a:"))

a1 = a ** 2
a2 = a ** 3
a3 = a ** 5
a4 = a ** 10
a5 = a ** 15
print('Значение A в степени 2 равно: ', a1)
print('Значение A в степени 3 равно: ', a2)
print('Значение A в степени 5 равно: ', a3)
print('Значение A в степени 10 равно: ', a4)
print('Значение A в степени 15 равно: ', a5)"""

"""# Begin 29

a = int(input("a: "))
s = a * 180 / 3.14
print(s)

# Begin 30

a = float(input("a: "))
d = a * 3.14 / 180
print(d)"""

"""# Begin 31

Tf = int(input("Tf: "))
Tc = (Tf - 32) * 5 / 9
print(Tc)"""

"""# Begin 32

Tf = int(input("Tf: "))
Tc = 9 / 5 * Tc + 32
print(Tc)

# Begin 33

import random

X, Y = [random.randrange(1, 10) for i in range(2)]  # 7 7
A = random.randrange(1000, 10000)  # 4094
price = A / X
cost_Y = price * Y
print(X, "kg = ", A, " rubles")
print("1 kg = {0:.2f} rubles".format(price))
print("{0} kg = {1:.2f} rubles".format(Y, cost_Y))"""

"""# Begin 34

x=int(input('Вес шоколадных конфет:'))
a=int(input('Стоимость шоколадных конфет:'))
y=int(input('Вес ирисок:'))
b=int(input('Стоимость ирисок:'))
sx=a/x
sy=b/y
print('Цена 1 кг шоколадных конфет: ',sx)
print('Цена 1 кг ирисок: ',sy)
print('Шоколадные конфеты дороже в ',sx/sy," раз" )"""

""" Begin 35 Скорость лодки в стоячей воде V км/ч, скорость течения реки U км/ч (U < V). 
Время движения лодки по озеру T1 ча по реке (против течения) — T2 ч. Определить путь S, 
пройденный лодкой (путь = время · скорость). Учесть,
что при движении против течения скорость лодки уменьшается на величину скорости течения

V = int(input("Скорость лодки в стоячей воде: "))
U = int(input("Скорость течения реки: "))
T1 = int(input("Время движения лодки по озеру: "))
T2 = int(input("а по реке против течения: "))
s = V * T1 + (V - U) * T2
print("Путь пройденный лодка = ", s, "часов")"""

""" Begin 36 Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние между ними S км. 
Определить расстояние между ними через T часов,
если автомобили удаляются друг от друга.
Данное расстояние равно сумме начального расстояния и общего пути,
проделанного автомобилями; общий путь = время · суммарная скорость.

v1 = int(input("Скорость первого автомобиля: "))
v2 = int(input("Скорость второго автомобиля: "))
t = int(input("t ч: "))
s = int(input("расстояние между ними: "))
k = s + v1 * t + v2 * t
print("Между автомобилями", k, "km")"""

"""Begin 37 Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние между ними S км.
Определить расстояние между ними через T часов, если автомобили первоначально движутся навстречу друг другу.
Данное расстояние равно модулю разности начального расстояния и общего пути, проделанного автомобилями;
общий путь = время · суммарная скорость.

v1 = int(input("Скорость первого автомобиля: "))
v2 = int(input("Скорость второго автомобиля: "))
s = int(input("ростаяни между ними: "))
t = int(input("t часов: "))
u = abs(s - (v1 * t + v2 * t))
print("Данное расстояние равно: ", u)"""

"""# Begin 38  Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
a = int(input("a: "))
b = int(input("b: "))
s = (-1) * b/a
print(s)"""

"""Begin 39  Найти корни квадратного уравнения A·x2 + B·x + C = 0, 
заданного своими коэффициентами A, B, C (коэффициент A не равен 0), 
если известно, что дискриминант уравнения положителен. Вывести вначале меньший, а затем больший из найденных корней.
Корни квадратного уравнения находятся по формуле x1,2 = () /B D−± (2·A), где D — дискриминант, равный B2 – 4·A·C.

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = b * 2 - 4 * a * c
print("Корни квадратного уравнения равно: ", d)
x1 = (-2 + 4) / 2
x2 = (-2 - 4) / 2
if x2 < x1:
    print('Меньший корень равен : ', x1)
    print('Больший корень равен : ', x2)
else:
    print('Меньший корень равен : ', x2)
    print('Больший корень равен : ', x1)"""

""" Begin 40 Найти решение системы линейных уравнений вида
A1·x + B1·y = C1,
A2·x + B2·y = C2,
заданной своими коэффициентами A1, B1, C1, A2, B2, C2,
если известно, что данная система имеет единственное решение.
Воспользоваться формулами
x = (C1·B2 – C2·B1)/D,
y = (A1·C2 – A2·C1)/D,
где D = A1·B2 – A2·B1.

a1 = int(input("a1: "))
b1 = int(input("b1: "))
c1 = int(input("c1: "))
a2 = int(input("a2: "))
b2 = int(input("b2: "))
c2 = int(input("c2: "))
d = a1 * b2 - a2 * b1
x = (c1 * b2 - c2 * b1) / d
y = (a1 * c2 - a2 * b1) / d
print("x = ", x)
print("y: ", y)"""

# integer

""" Integer1. Дано расстояние L в сантиметрах. Используя операцию деления нацело,
найти количество полных метров в нем (1 метр = 100 см).

l = int(input("l: "))
d = l / 100
print(l, "метр", d, "см")"""

""" Integer2. Дана масса M в килограммах. Используя операцию деления нацело,
найти количество полных тонн в ней (1 тонна = 1000 кг).

m = int(input("m: "))
d1 = m / 1000
print(m, "тонна", d1, "кг")"""

"""# Integer3°. Дан размер файла в байтах. Используя операцию деления нацело,
# найти количество полных килобайтов, которые занимает данный файл (1 килобайт = 1024 байта).

n = int(input("n: "))
d1 = n * 1024
print(n, "килобайт", d1, "байта")"""

"""# Integer4. Даны целые положительные числа A и B (A > B).
# На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений).
# Используя операцию деления нацело, найти количество отрезков B, размещенных на отрезке A.

a = int(input("Введите длину отрезка a: "))
b = int(input("Введите длину отрезка b: "))
s = a // b
print('В отрезке a содержится ', s, ' полных отрезков b.')"""

"""# Integer5. Даны целые положительные числа A и B (A > B).
# На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений).
# Используя операцию взятия остатка от деления нацело, найти длину незанятой части отрезка A.

a = int(input("Введите длину отрезка a: "))
b = int(input("Введите длину отрезка b: "))
d4 = a % b
print(d4)"""

"""# Integer6. Дано двузначное число. Вывести вначале его левую цифру (десятки),
# а затем — его правую цифру (единицы).
# Для нахождения десятков использовать операцию деления нацело,
# для нахождения единиц — операцию взятия остатка от деления.

a = int(input("Введите двузначное число: "))
s = a // 10
f = a % 10
print(s)
print(f)"""

"""# Integer7. Дано двузначное число. Найти сумму и произведение его цифр.

a = int(input("Введите двузначное число: "))
s = a // 10
f = a % 10
v = s + f
b = s * f
print("сумма двузначние число =", v)
print("произведение двузначние число =", b)"""

"""# Integer8°. Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа

A = int(input("Введите двузначное число: "))
Res = (A // 10) + (A % 10) * 10
print('При перестановке цифр исходного числа получится: ', Res)"""

"""# Integer9. Дано трехзначное число. Используя одну операцию деления нацело, вывести первую цифру данного числа (сотни).
s = int(input("Введите трехзначное число: "))
d = s // 100
print(d)"""

"""# Integer10. Дано трехзначное число. Вывести вначале его последнюю цифру (единицы),
# а затем — его среднюю цифру (десятки).
s = int(input("Введите трехзначное число: "))
d = s % 10
f = s % 100 // 10
print("его последнюю цифр:", d)
print("среднюю цифру", f)"""

"""# Integer11°. Дано трехзначное число. Найти сумму и произведение его цифр.
s = int(input("Введите трехзначное число: "))
d = s // 100
f = s % 100 // 10
c = s % 10
r7 = d + f + c
r8 = d * f * c
print("сумму трехзначное число:", r7)
print("произведение трехзначное число:", r8)"""

"""# Integer12. Дано трехзначное число. Вывести число, полученное при прочтении исходного числа справа налево
s = int(input("Введите трехзначное число: "))
c = (s % 10) * 100 + ((s % 100) // 10) * 10 + (s // 100)
print("Выводим число на оборот:", c)"""

"""# Integer13. Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали ее справа.
# Вывести полученное число.

s = int(input("Введите трехзначное число: "))
b = (s % 100) * 10 + (s // 100)
print(b)                 # 584"""

"""# Integer14. Дано трехзначное число. В нем зачеркнули первую справа цифру и приписали ее слева.
# Вывести полученное число
s = int(input("Введите трехзначное число: "))
b = (s % 10) * 100 + (s // 10)
print(b) 845 """

"""# Integer15. Дано трехзначное число. Вывести число,
# полученное при перестановке цифр сотен и десятков исходного числа (например, 123 перейдет в 213)
s = int(input("Введите трехзначное число: "))
b = (s % 10) + ((s % 100) // 10) * 100 + (s // 100) * 10
print(b)"""

"""# Integer16. Дано трехзначное число. Вывести число, полученное при
# перестановке цифр десятков и единиц исходного числа (например, 123 перейдет в 132).
s = int(input("Введите трехзначное число: "))
b = (s % 10) + ((s % 100) // 10) * 100 + (s // 100) * 10
print(b)"""

'''# Integer17. Дано целое число, большее 999.
# Используя одну операцию деления нацело и одну
# операцию взятия остатка от деления, найти цифру,
# соответствующую разряду сотен в записи этого числа

f = int(input("f = "))
d = (f // 100) % 10
print(d)'''

'''# Integer18. Дано целое число, большее 999.
# Используя одну операцию деления нацело и одну
# операцию взятия остатка от деления, найти цифру,
# соответствующую разряду тысяч в записи этого числа

f = int(input("f = "))
g = f // 1000
print(g)'''

"""s = int((input("a: ")))
a = (s % 10) + ((s % 100) // 10) * 100 + (s // 100) * 10
print(a)

dop = "http://google.com"
gop = "https://wikipedia.com"
print(gop)"""

"""name = "Bro Code sardor"

print(len(name))
print(name.find("0"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o", "a"))
print(name*3)"""

"""x = 1 #int
y = 2.0  #float
z = "3" #str

print(("x is" + x))
print(("y is" + y))
print(z*3)

x = float(x)
y = float(y)
z = float(z)"""

# сартировка пузрком

"""nums = [1, 4, 8, 9, 3, 4, 7]

print(nums)

for i in range(len(nums)):
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)"""
# Integer 19 С начала суток прошло N секунд (N — целое). Найти количество
# полных минут, прошедших с начала суток
'''n = int(input("Введите каличество секунд: "))
s = int(n // 60)
print("каличество полных минут: ", s)'''
# Integer20◦
# . С начала суток прошло N секунд (N — целое). Найти количество
# полных часов, прошедших с начала суток.
'''n = int(input("Введите каличество секунд: "))
s = n // (60*60)
print("каличество полных часов: ", s)'''

# Integer21◦
# . С начала суток прошло N секунд (N — целое). Найти количество
# секунд, прошедших с начала последней минуты
'''c = int(input("Введите каличество секунд: "))
s = c // 60
print("каличество секунд прошедших с последние минуты:", s)'''
# Integer22◦ С начала суток прошло N секунд (N — целое). Найти количество
# секунд, прошедших с начала последнего часа.
'''c = int(input(" c: "))
d = c % 3600
print(d, 'секунд')'''
# Integer23◦
# . С начала суток прошло N секунд (N — целое). Найти количество
# полных минут, прошедших с начала последнего часа
'''d = int(input("d: "))
f = d % 60
print(f, "minut")'''
# Integer24◦
# . Дни недели пронумерованы следующим образом: 0 — воскресенье,
# 1 — понедельник, 2 — вторник, . . . , 6 — суббота. Дано целое число K,
# лежащее в диапазоне 1–365. Определить номер дня недели для K-го дня
# года, если известно, что в этом году 1 января было понедельником.

"""import random
week_days = {
    0: 'воскресенье',
    1: 'понедельник',
    2: 'вторник',
    3: 'среда',
    4: 'четверг',
    5: 'пятница',
    6: 'суббота'
}
K = random.randrange(1,366)
K = 31
i = (1 + 1) % 7
print("1-е января: ", 1)
print("Номер дня недели: ", i)
print("День недели:", week_days[i])
i = K % 7
print()
print("Номер дня года: ", K)
print("Номер дня недели: ", i)
print("День недели:",week_days[i])"""

"""import turtle
turtle.bgcolor("black")
turtle.speed(0)
turtle.pensize(1)

for i in range(6):
    for colors in ["red", "yellow", "magenta" ]:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(5)
turtle.hideturtle"""

# Integer25◦
# . Дни недели пронумерованы следующим образом: 0 — воскресенье,
# 1 — понедельник, 2 — вторник, . . . , 6 — суббота. Дано целое число K,
# лежащее в диапазоне 1–365. Определить номер дня недели для K-го дня
# года, если известно, что в этом году 1 января было четвергом

'''import random

week = {
    0: "воскресеные",
    1: 'понеделник',
    2: 'vtornic',
    3: 'sreda',
    4: 'chetverg',
    5: 'pyatnisa',
    6: 'subbota',
    7: 'voskreseniya'
}
k = random.randrange(1,366)
k = 31
i = (1 + 4) % 7
print("1-е января: ", 1)
print("Номер дня недели: ", i)
print("День недели:", week[i])
i = k % 7
print()
print("Номер дня года: ", k)
print("Номер дня недели: ", i)
print("День недели:",week[i])'''

# Integer26◦ . Дни недели пронумерованы следующим образом: 1 — понедельник, 2 — вторник, . . . , 6 — суббота,
# 7 — воскресенье. Дано целое число K, лежащее в диапазоне 1–365. Определить номер дня недели для K-го дня года,
# если известно, что в этом году 1 января было вторником.

import random

'''week = {
    1: 'ponedelnik',
    2: 'vtornic',
    3: 'sreda',
    4: 'chetverg',
    5: 'pyatnisa',
    6: 'subbota',
    7: 'voskresiniya'
}
k = random.randrange(1, 366)
k = 31
i = (1 + 1) % 7
print("1-е января: ", 1)
print("Номер дня недели: ", i)
print("День недели:", week[i])
i = k % 7
print()
print("Номер дня года: ", k)
print("Номер дня недели: ", i)
print("День недели:",week[i])'''

# Integer27◦ . Дни недели пронумерованы следующим образом: 1 — понедельник, 2 — вторник, . . . , 6 — суббота,
# 7 — воскресенье. Дано целое число K, лежащее в диапазоне 1–365. Определить номер дня недели для K-го дня года,
# если известно, что в этом году 1 января было субботой.
# ....................

# Integer28◦ . Дни недели пронумерованы следующим образом: 1 — понедельник, 2 — вторник, . . . , 6 — суббота,
# 7 — воскресенье. Дано целое число K, лежащее в диапазоне 1–365, и целое число N, лежащее в диапазоне 1–7.
# Определить номер дня недели для K-го дня года, если известно, что в этом году 1 января было днем недели с номером N.

'''import random
week_days = {
    1: 'понедельник',
    2: 'вторник',
    3: 'среда',
    4: 'четверг',
    5: 'пятница',
    6: 'суббота',
    7: 'воскресенье'
}
K = random.randrange(1, 366)
print(K)
N = random.randrange(1, 8)
print(N)
print("K = ", K, "; N = ", N)
K = 29
i = (1+N-1) % 7 + 1
print("1-е января: ", 1)
print("Номер дня недели: ", i)
print("День недели:", week_days[i])
i = (K+N-1)%7 + 1
print()
print("Номер дня года: ", K)
print("Номер дня недели: ", i)
print("День недели:", week_days[i])'''

# Integer29◦ . Даны целые положительные числа A, B, C. На прямоугольнике размера A × B размещено максимально
# возможное количество квадратов со стороной C (без наложений). Найти количество квадратов, размещенных на
# прямоугольнике, а также площадь незанятой части прямоугольника.
'''import math
a = int(input(" a = "))
b = int(input(" b = "))
c = int(input(" c = "))

Num =(a // c) * (b // c)
print('На прямоугольнике можно разместить ', Num, ' квадратов')

S = a * b - Num * math.sqrt(c)
print('Не занятая площадь прямоугольника равна ', S)'''

# Integer30◦ . Дан номер некоторого года (целое положительное число). Определить соответствующий ему номер столетия,
# учитывая, что, к примеру, началом 20 столетия был 1901 год.

'''v = int(input(" v: "))
c = (v // 100) + 1
print(c)'''

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if a > b and a > c:
#     f = b + c
# print(f)
# ///////////////////////////////////////////////////////////////////////////////

# Begin 1

# a = int(input("a = "))
# p = 4 * a
# print(p)
# Begin 2
# a = int(input("a = "))
# s = a ** 2
# print(s)
# Begin 3
# a = int(input("a = "))
# b = int(input("b = "))
# s = a * b
# p = 2 * (a + b)
# print("s = ", s)
# print("p = ", p)
# Begin 4
# a = int(input("a = "))
# p = 4 * a
# print(p)
# Begin 5
# a = int(input("a= "))
# v = a **3
# print("v = ", v)
# s = 6 * a ** 2
# print("s = ", s)
# Begin 6
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# v = a * b * c
# print(v)
# s = 2 * (a * b + b *c + a *c)
# print(s)
# # Begin 7
# p = 3.14
# r = int(input("r = "))
# l = 2 * p *r
# print(l)
# s = p * r ** 2
# print(s)
# Begin 8
# a = int(input())
# b = int(input())
# s = (a + b) / 2
# print(s)

# x = int(input("x = "))
# if(x % 2) == 0:
#     print("Чотние")
# else:
#     print("Нечетное")
# if x > 99:
#     print("трёхзначние")
# if (99 >= x) and (x > 9):
#     print("двухзначние")
# if x <= 9:
#     print("однозначние")
# print("\U0001F917")
# print("\U0001F637")

import math


# Begin 9
# a = int(input("Ракам дароред: "))
# b = int(input("Ракам дароред: "))
# c = a * b
# print("Хосили зарби ду ракам: ", c)
# print("Решаи хосили зарб: ", abs(d))
# d = math.sqrt(c)
# Begin 10
# a = int(input("Ракм дароред: "))
# b = int(input("Ракм дароред: "))
# s = a + b
# print("Суммаи ду ракам", s)
# d = a - b
# print("Минуси ду ракам", d)
# zarb = a * b
# print("Зарби ду ракам", zarb)
# e1 = r1 ** 2
# e2 = r2 ** 2
# chast = e1 / e2 # Часное их квадратов
# print("Квадрат ду ракам", chast)
# Begin 11
# a = int(input("Ракам дароред: "))
# b = int(input("Ракам дароред: "))
# print("Сумма: ", a + b)
# print("Минус: ", a - b)
# print("Зарб: ", a * b)
# print("Частное из модулей: ", abs(a) + abs(b)) # функсия abs() знак модуль
# Begin 12
# a = int(input("a="))
# b = int(input("b="))
# c = math.sqrt(a**2 + b**2)
# print("Гипотенуза ёфт шуд", c)
# p = a + b + c
# print("Периметр ёфт шуд", p)
# Begin 13
# r1 = int(input("r1="))
# r2 = int(input("r2="))
# p = 3.14
# s1 = p * r1 ** 2
# print("Кольца, внешний радиус которого равен", s1)
# s2 = p * r2 ** 2
# print("Кольца, вутренний радиус которого равен", s2)
# s3 = s1 - s2
# print("Площадь", s3)
# Begin 14
# r = int(input("r="))
# p = 3.14
# l = 2 + p * r
# print("Радиус ", l)
# s = p * r ** 2
# print("лошад круга ", s)
# Begin 15
# r = int(input("r = "))
# p = 3.14
# l = 2 * p * r
# print("Длина окружности", l)
# s = p * r ** 2
# print("Плошад груга", s)
# d = 2 * r
# print("Диаметр", d)
# Begin 16
# x1 = int(input("x1 = "))
# x2 = int(input("x2 = "))
# d = abs(x2 - x1)
# print("Расстоаяние между двумя x1.....x2 = ", d)
# Begin 17
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# d = abs(a - c)
# print("Расстояние отрезка AC равно: ", d)
# g = abs(b - c)
# print("Расстояние отрезка BC равно: ", g)
# sum = d + g
# print("Summa отрезков AC и BC равно", sum)
# Begin 18
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
# ac = abs(c - a)
# print(ac)
# cb = abs(b - c)
# print(cb)
# df = ac * cb
# print("произведени равно", df)
# Begin 19
# x1 = int(input("x1 = "))
# y1 = int(input("y1 = "))
# x2 = int(input("x2 = "))
# y2 = int(input("y2 = "))
# t = (x1 + y2) * 2
# print("Периметр равно ", t)
# t1 = x1 * y2
# print("Плошад равно", t1)
# Begin 20
# x1 = int(input("x1="))
# y1 = int(input("y1="))
# x2 = int(input("x2="))
# y2 = int(input("y2="))
# r1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# print("Расстояние между двумя точками равно", r1)
# begin 21
# x1 = int(input("x1 = "))
# y1 = int(input("y1 = "))
# x2 = int(input("x2 = "))
# y2 = int(input("y2 = "))
# x3 = int(input("x3 = "))
# y3 = int(input("y3 = "))
# d = math.sqrt((x3 - x2)**2 + (y3 - y2)**2 + (x2 - x1)**2 + (y2 - y1)**2)
# print("Координаты трех вершин треугольника: ", d)
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# p = a + b + c
# print("Периметр треуголника равен = ", p)
# pp = (a + b + c) / 2
# s = math.sqrt(pp + (pp - a) * (pp - b) * (pp - c))
# print("Площади треугольника со сторонами a, b, c = ", s)
# begin 22
# a = int(input("a: "))
# b = int(input("b: "))
# a = b + a
# b = a - b
# a = a - b
# print("a = ", a, "  ", "b = ", b)
# Begin 23
# import random
#
# A, B, C = sorted(random.sample(range(-10, 10), 3))
# print("A = {0}, B = {1}, C = {2}".format(A, B, C))
# A, B = B, A
# A, C = C, A
# print("A = {0}, B = {1}, C = {2}".format(A, B, C))
# # Begin 24

# Codewars zadacha
# def sum_array(a):
#     total = 0
#     for number in a:
#         total += number
#     return total
#
#
# print(sum_array([1, 2, 3]))  # 6
# def sum_array(a):
#     return sum(a);
# print(sum_array([1, 2, 3]))