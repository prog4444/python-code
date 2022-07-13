from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
            host="localhost",
            user=input("username: "),
            password=(""),
            database="dars",
    ) as connection:
        print(connection)
except Error as e:
    print(e)
