"""import random
import time
def displayIntro():
    print('''Вы находитесь в землях, заселенных драконами. 
    6. Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон, 
    7. который готов поделиться с вами своими сокровищами. 
    Во второй — 8. жадный и голодный дракон, который мигом вас съест.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
        cave = input()


    return cave

def checkCave(chosenCave):
     print('Вы приближаетесь к пещере...')
     time.sleep(2)
     print('Ее темнота заставляет вас дрожать от страха...')
     time.sleep(2)
     print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
     print()
     time.sleep(2)

     friendlyCave = random.randint(1, 2)

     if chosenCave == str(friendlyCave):
         print('...делится с вами своими сокровищами!')
     else:
         print('...моментально вас съедает!')

playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Попытаете удачу еще раз? (да или нет)')
    playAgain = input()"""

import random
t = 0
print('привет Как тубя зовут')
myName = input()

number = random.randint(1, 20)
print('что x,' + myName + 'я загадываю число от 1 and 20')

for guessesTaken in range(6):
    print('Попробуй угадать.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Твое число слишком маленькое.')
    if guess > number:
        print('Твое число слишком большое.')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Отлично, ' + myName + '! Ты справился за ' + guessesTaken + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Я загадала число ' + number + '.')




