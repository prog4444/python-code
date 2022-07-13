def say_hello(name="Tom"):
    print("Hello,", name)


say_hello()
say_hello("Bob")


def display_info(name, age):
    print("Name:", name, "\t", "Age:", age)


display_info(age=22, name="tom")


def sum(*params):
    result = 0
    for n in params:
        result += n
    return result


sumOfNumbers1 = sum(1, 2, 3, 4, 5)
sumOfNumbers2 = sum(3, 4, 5)
print(sumOfNumbers1)
print(sumOfNumbers2)


def exchange(usd_rate, money):
    result = round(money / usd_rate, 2)
    return result


result1 = exchange(60, 30000)
print(result1)
result2 = exchange(56, 300000)
print(result2)
result3 = exchange(65, 30000)
print(result3)


def create_default_user():
    name = "Tom"
    age = 33
    return name, age


user_name, user_age = create_default_user()
print("Name:", user_name, "\t Age:", user_age)


def main():
    say_hello("Tom")
    usd_rate = 56
    money = 30000
    result = exchange(usd_rate, money)
    print("К выдаче", result, "долларов")


def say_hello(name):
    print("Hello", name)


def exchange(usd_rate, money):
    result = round(money / usd_rate, 2)
    return result


main()


def m(number):
    print(number ** 2)


m(2)

name = "sardor"


def say_bye():
    print("Good bye", name)


say_bye()
