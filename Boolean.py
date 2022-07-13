import random
# Boolean1◦
# . Дано целое число A. Проверить истинность высказывания: «Число A является положительным».
'''a = int(input("a = "))
f = a > 0
print(f)'''
# Boolean2◦
# . Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
'''a = float(input("a = "))
s = a % 2 == 1
print(s)'''
# Boolean3◦
# Дано целое число A. Проверить истинность высказывания: «Число A является четным».
'''a = float(input("a: "))
s = a % 2 == 0
print(s)'''

# Boolean4◦
# . Даны два целых числа: A, B. Проверить истинность высказывания:
# «Справедливы неравенства A > 2 и B ≤ 3».
'''a = int(input("a: "))
b = int(input("b: "))
f = a > 2 and b <= 3
print(f)'''

# Boolean5◦
# . Даны два целых числа: A, B. Проверить истинность высказывания:
# «Справедливы неравенства A ≥ 0 или B < −2».
'''a = random.randrange(-10, 10)
b = random.randrange(-10, 10)
d = (a > 0) or (b < -2)
print(d)'''
# Boolean6◦
# Даны три целых числа: A, B, C. Проверить истинность высказывания: «Справедливо двойное неравенство A < B < C».
'''a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
s = a < b < c
print(s)'''
'''A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
print("A = ", A)
print("B = ", B)
print("C = ", C)
x = (A<B) and (B<C)
print("A<B: ", (A<B))
print("B<C: ", (B<C))
print("A<B<C: ", x)'''













