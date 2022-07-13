''' arr =[1, 2, 3, 4]
abd = enumerate(arr, start=2)
next(abd) '''

'''i =1
while i < 101:
    print(i)
    i -= 1'''

'''arr = [1, 2, 3]
i, count = 0, len(arr)
while i < count:
    arr[i] *= 2
    i += 1
print(arr)'''
'''for i in range(1, 101):
    if 4 < i < 11:
        continue
    print(i)'''
'''i = 1
while True:
    if i > 100: break
    print(i)
    i += 1'''
'''print("ведите слово 'stop' ля получения результата")
summa = 0
while True:
    x = input("Введите число: ")
    if x == "stop":
        break       # Вход из сикла
    x = int(x)      # Преобразуем строку в число
    summa += x
print("сумма чисел равно:", summa)
input()'''
# while True: print(eval(input("a= ")))

# For1. Даны целые числа K и N (N > 0). Вывести N раз число K.
"""k = int(input(" k: "))
n = int(input(" n: "))
for i in range(n):
    if n > 0:
        print(k)"""

# For2. Даны два целых числа A и B (A < B). Вывести в порядке возрастания все
# целые числа, расположенные между A и B (включая сами числа A и B), а
# также количество N этих чисел.
"""a = int(input(" a: "))
b = int(input(" b: "))
for i in range(a, b + 1):
    print(i)"""
# For3. Даны два целых числа A и B (A < B). Вывести в порядке убывания все
# целые числа, расположенные между A и B (не включая числа A и B), а
# также количество N этих чисел.
"""a = int(input())
b = int(input())
for i in range(b - 1, a, -1):
    print(i)"""
# For4. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1,
# 2, . . . , 10 кг конфет.
"""a = float(input())
print(*[f'{i}кг - цена: {round(i * a, 2)}' for i in range(1, 11)], sep='\n')"""

























































