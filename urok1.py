'''import math

print(math.pow(10, 2))'''

'''s = "sar\ndor"
s1 = "sar\rdor"
s2 = "sar\tdor"
s3 = "sar\vdor"
s4 = "sar\ador"
s5 = "sar\bdor"
s6 = "sar\fdor"
s7 = "sar\0dor"
s8 = "sar\"dor"
s9 = "sar\'dor"
print(s, s1, s2, s3, s4, s5, s6, s7, s8, s9)'''

'''number = 23
running = True

while running:
    guuss = int(input('Введите целое число : '))

    if guuss == number:
        print('поздравляю вы угадали ')
        running = False # это останавливаеть цикл while
    elif guuss < number:
        print('Нет, загаданное число немного больше этого')
    else:
        print('Нет, загаданное число немного менше этого')
else:
    print('Цикл while закончен.')'''

'''while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    print('Длина строки: ', len(s))
print('Завершение')'''
'''while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введённая строка достаточной длины')'''

'''def sayhello():
    print("Thanky say have a you ")


sayhello()
sayhello()


def pilus(b, m):
    a = b + m
    print(a)


pilus(5, 6)'''

'''def fo(a, b):
    while a > b:
        print("Hello world")
        break
    if a < b:
        print("Sardor a mayda budas")


fo(5, 4)'''

'''x = 50
def func():
    global x
    
    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)
    
    
    
    
func()
print('Значение x составляет', x)'''

'''def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('Локальное x сменилось на', x)


func_outer()'''

'''def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count


print(total(10, 1, 2, 3, vegetables=50, fruits=100))'''

'''*a, b, c = 1, 2, 3, 4, 5, 8, 9
print(a, b, c) # operator * для происвоение на один обект несколко значение'''

'''s = [4, 10]
print(list(range(1, 5)))
print(list(range(*s)))'''

'''def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Число равны'
    else:
        return y
print(maximum(3, 2))'''

# def printMax(x, y):
# '''#Выводит максимальное из двух чисел.

# Оба значения должны быть целыми числами.'''
# '''x = int(x) # конвертируем в целые, если возможно
# y = int(y)

# if x > y:
# print(x, 'наибольшее')
# else:
# print(y, 'наибольшее')
# printMax(3, 5)
# print(printMax.__doc__)


"""import sys

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)
print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')"""

'''import calendar

c = calendar.TextCalendar()
print(c.formatyear(2020))'''

'''import  sys
r = dir('str')
print(r)


a = help(eval)'''

# Это мое список

"""shoplist = ['def', 'sardor', 'sador']
print('Я должен сделать ', len(shoplist), 'покупок')
print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')
print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)
print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)
print('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)"""

"""zoo = ('питон', 'слон', 'пингвин') # помните, что скобки не обязательны
print('Количество животных в зоопарке -', len(zoo))
new_zoo = 'обезьяна', 'верблюд', zoo
print('Количество клеток в зоопарке -', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Животные, привезённые из старого зоопарка:', new_zoo[2])
print('Последнее животное, привезённое из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(new_zoo)-1+len(new_zoo[2]))"""

"""list = ["sardor", "madina", "aziza", "lola"]
new_list = list
list[0] = "lola"
list[2] = "pop"
print(list, "\n", new_list)

t = [1, 2, 3, 4]
t[0] = 2
print(t)"""

"""list = [1, 5, 6, 8, 7, 10, 4, 3, 2]
print(list)
for i in range(len(list)):
    for j in range(len(list)-i-1): 
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)"""

"""ab = {
    'Swaroop': 'swaroop@gmail.com',
    'Larry': 'Larry@wall.org',
    'Matsumoto':'lang.org'
}
print("adress swaroop'a:", ab['Swaroop'])
print("adress swaroop'a:", ab['Larry'])
print("adress swaroop'a:", ab['Matsumoto'])
# Удаление пары ключ-значение
del ab['Larry']
print('\nВ адресной книге {0} контактов\n'.format(len(ab)))
for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))
# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])"""
"""a = help(dict)
print(a)"""

"""shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'
# Операция индексирования
print('Элемент 0 -', shoplist[0])
print('Элемент 1 -', shoplist[1])
print('Элемент 2 -', shoplist[2])
print('Элемент 3 -', shoplist[3])
print('Элемент -1 -', shoplist[-1])
print('Элемент -2 -', shoplist[-2])
print('Символ 0 -', name[0])

# Вырезка из списка

print('Элементы с 1 по 3:', shoplist[1:3])
print('Элементы с 2 до конца:', shoplist[2:])
print('Элементы с 1 по -1:', shoplist[1:-1])
print('Элементы от начала до конца:', shoplist[:])

# Вырезка из строки

print('Символы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 до -1:', name[1:-1])
print('Символы от начала до конца:', name[:])"""

# d = help(str)
# print(d)

"""name = 'Swaroop' # Это объект строки
if name.startswith('Swa'):
    print('Да, строка начинается на "Swa"')
if 'a' in name:
    print('Да, она содержит строку "a"')
if name.find('war') != -1:
    print('Да, она содержит строку "war"')
delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))"""

"""import os
import time

source = ["C:\\My Documents"]

target_dir = 'E:\\Backup'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + ".zip"
zip_command = "zip -gr {0}".format(target, ' '.join(source))
print(zip_command)
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')"""

"""class Person:
    def sayHi(self):
        print('Hi, Have a you')


p = Person()
p.sayHi()"""

'''class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Hi My name is Sardor', self.name)

p = Person('Swaroop')
p.sayHi()'''

"""class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        Robot.population += 1

    def __del__(self):
        print('{0} уничтожается!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))

    def sayHi(self):
        '''Приветствие робота.
        Да, они это могут.'''
        print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))

    def howMany():
        print('У нас {0:d} роботов.'.format(Robot.population))

    howMany = staticmethod(howMany)


droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()
print("\nЗдесь роботы могут проделать какую-то работу.\n")
print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2
Robot.howMany()"""

"""class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Ser:
    def ret(self):
        print("sardor")


p = Ser
p.name = "Sardor"
p.age = 45
print(p.name, "\\", p.age)
p.ret()"""

"""class Classl: # Базовый класс

    def funcl(self):
        print("Meтoд funcl() класса Classl")

    def func2 (self) :
        print("Meтoд func2() класса Classl")


class Class2(Classl):  # Класс Class2 наследует класс Classl
    def funcЗ(self) :
        print("Meтoд funcЗ() класса Class2")


с = Class2()  # Создаем экземпляр класса Class2
с. funcl()  # Выведет: Метод funcl () класса Classl
с. func2()  # Выведет: Метод func2 () класса Classl
с. funcЗ()"""

"""class Classl: # Базовь� класс для класса Class2
    def funcl ( self) :
        print("Meтoд funcl() класса Classl")
class Class2(Classl): # К.пасс Class2 наследует класс Classl
    def func2(self):
        print("Meтoд func2() кпасса Class2")
class ClassЗ(Classl): # Класс ClassЗ наследует класс Classl
    def funcl ( self):
        print ( "метод func1() kласса ClassЗ")
    def func2(self):
        print("Meтoд func2{) класса ClassЗ")
    def funcЗ(self):
        print("Meтoд funcЗ() класса ClassЗ")
    def func4(self):
        print("Meтoд func4() класса ClassЗ")
class Class4(Class2, ClassЗ): # Множественное наследование
    def func4(self):
        print("Meтoд func4() класса Class4")
        
        
с = Class4()  # Создаем экземпляр класса Class4
с. funcl()   # Выведет: Метод funcl () класса ClassЗ
с. func2()  # Выведет: Метод func2 () класса Class2
с. funcЗ() # Выведет: Метод funcЗ () класса ClassЗ
с. func4() # Выведет: Метод func4 () класса Class4"""

"""class Myclass:
    def __init__(self, m):
        self.msg = m
    def __call__(self):
        print(self.msg)

c = Myclass("Znacheniy1")
c1 = Myclass("Znacheniy2")
c()
c1()"""

"""class MyClass:
    def __init__(self):
        self.i = 20

    def __getattr__(self, attr):
        print("Вызван метод __getattr__()")
        return 0


c = MyClass()
print(c.i)
print(c.s)"""

"""class MyClass:
    def __init__(self):
        self.i = 20

    def __getattribute__(self, attr):
        print("Вызван метод _getattribute_()")
        return object.__getattribute__(self, attr)


a = MyClass()
print(a.i)"""

"""class MyClass:
    def __setattr__ (self, attr, value):
        print("Вызван метод setattr ()")
        self.__dict__[attr] = value # Только так!!!


a = MyClass()
a.i = 10  # Выведет: Вызван метод setattr ()
print(a.i)  # Выведет: 10"""

"""class MyClass:

    def __init__(self, y):
        self.x = y

    def __add__(self, y):
        print("Экземпляр слева")
        return self.x + y

    def __radd__(self, y):
        print("Экзумпляр справо")
        return self.x + y

    def __iadd__(self, y):
        print("Сложение с присваиванием")
        self.x += y
        return self


c = MyClass(50)
print(c + 10)
print(20+c)
c += 30
print(c.x)"""

"""class MyClass:
    @staticmethod
    def func1(x, y):
        return x + y
    def func2(self, x, y):
        return x + y
    def func3(self, x, y):
        return MyClass.func1(x, y)


print(MyClass.func1(10, 20))
c =MyClass()
print(c.func2(15, 6))
print(c.func1(50, 12))
print(c.func3(23, 5))"""

"""class MyClass:
    @classmethod
    def func(cls, x):
        print(cls, x)
MyClass.func(10)
c = MyClass()
c.func(50)"""

"""class Class1:
    def func(self, x):
        raise NotImplementedError("Необходимо переопределить метод")
class Class2(Class1):
    def func(self, x):
        print(x)
class Class3(Class1):
    pass

c2 = Class2()
c2.func(50)
c3 = Class3()
try:
    c3.func(50)
except NotImplementedError as msg:
    print(msg)"""

"""from abc import ABCMeta, abstractmethod
class Class1 (metaclass=ABCMeta):
    @abstractmethod
    def func(self, x):
        pass

class Class2(Class1):
    def func(self, x):
        print(x)

class Class3(Class1):
    pass

c2 = Class2()
c2.func(50)
try:
    c3 =Class3()
    c3.func(50)
except TypeError as msg:
    print(msg)"""

"""class MyClass:
    def __init__(self, x):
        self.__privateVar = x

    def set_var(self, x):
        self.__privateVar = x
    def get_var(self):
        return self.__privateVar


c = MyClass(10)
print(c.get_var())
c.set_var(20)
print(c.get_var())
try:
    print(c.__privateVar)
except AttributeError as msg:
    print(msg)

c._MYCLASS__privatevar = 50

print(c.get_var())"""

"""class MyClass:
    def __init__(self, value):
        self.__var = value
    def get_var(self):
        return self.__var
    def set_var(self, value):
        self.__var = value
    def del_var(self):
        del self.__var
    v = property(get_var, set_var, del_var, "Строка документасия")

c = MyClass(5)
c.v = 35
print(c.v)
del c.v"""

"""low = 0
high = len(list) - 1
mid = (low + high) / 5
guess = list[mid]
if guess < item:
    low = mid + 1"""

"""def binary_search(list, item):
    low = 0
    high = len(list) - 1  # 1 2, 3, 4, 5, 6 8 9 1 0 1 11213141516171819202122 -1=21

    while low <= high:  # 0 <= 21 True
        mid = (low + high)  # 0 1 2 3 4 5 6
        guess = list[mid]  # 3 5 7 9 21 22 6 22
        if guess == item:  # 3 5 7 9 21 22 6 22 == -1
            return mid  # 0 1 2 3 4 5 6
        if guess > item:  # 3 5 7 9 21 22 6 22 > -1
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9, 21, 22]

print(binary_search(my_list, 9))
print(binary_search(my_list, -1))"""

"""def benary_search(list, item):
    low = 0  # в переменных low и high списка чойгир шудааст
    high = len(list) - 1

    while low <= high:   # то хамин часташ якто кам......
        mid = (low + high)  # ....намешад проверка кадан мегирем
        guess = list[mid]
        if guess == item:  # значения ёфт шад
            return mid  # чоп мекунем mid-ро
        if guess > item:  # Много
            high = mid - 1
        else:          # мало
            low = mid + 1
    return None # значения нест гуфтос


my_list = [1, 2, 3, 4, 6]

print(benary_search(my_list, 2))  # 1 чоп мекунад
print(benary_search(my_list, -1))  # None чоп мекунад значения ёфт нашуд мегуд"""

"""def sart(list, item):
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


my_list = [1, 2, 3, 4, 5, 6, 7]

print(sart(my_list, 2))
print(sart(my_list, 10))"""

"""def sort(list, item):
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

my_list = [1, 2, 3, 4, 5, 6]

print(sort(my_list, 5))
print(sort(my_list, 5))"""

# Функсия для поиска наименьшего элемента массива:
import math


"""def findSmallest(arr):
    smallest = arr[0]  # 1, 3, 3, 4, 6, 6
    smallest_index = 0  # 0
    for i in range(1, len(arr)):  # 1, 2, 3, 4, 5
        if arr[i] < smallest:  # 1, 2, 3, 4, 5 < 1, 3, 3, 4, 6, 6
            smallest = arr[i]  # 2, 5
            smallest_index = i  # 1, 1
    return smallest_index  # 1, 1


def selectionSort(arr):
    newArr = []  # []
    for i in range(len(arr)):  # 0, 1 2 3 4 5
        smallest = findSmallest(arr) # 0 1 0 0 1 0
        newArr.append(arr.pop(smallest))
        # [1]
        # [1, 2]
        # [1, 2, 3]
        # [1, 2, 3, 4]
        # [1, 2, 3, 4, 5]
        # [1, 2, 3, 4, 5, 6]
    return newArr


print(selectionSort([1, 3, 2, 4, 6, 5]))"""


























