# Integer 27 
import random

str = {
    0: "Yakshanbe",
    1: "Dushanbe",
    2: "seshanbe",
    3: "chorshanbe",
    4: "Panshanbe",
    5: "Juma",
    6: "Sanbe"
}
K = random.randrange(1, 366)
N = random.randrange(1, 8)
print(N)
print("K = ", K, "; N = ", N)
K = 29
i = N % 7 + 4
print("1-е января: ", 1)
print("Номер хафта: ", i)
print("рузи хафта:", str[i])

# if 15
#
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if a > b and a > c:
#     f = b + c
# print(f)

# for 1
# k = int(input("k: "))
# n = int(input("n: "))
# for i in range(n):
#     print(k)

# for 2
