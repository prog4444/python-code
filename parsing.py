# pip install beautifulSoup
from bs4 import BeautifulSoup


with open('C:/Users/Acer/Desktop/f.html') as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")

title = soup.title
print(title)
page = soup.find("h1") # метод find теги h1 ка мебурорад
print(page)

page = soup.find_all("h1") # метод find теги хамаи h1 ка мебурорад
print(page)











