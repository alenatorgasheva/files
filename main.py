# Case - study #7
# This program shows information about filing system.

# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

# Tasks:
#  - локализация, комментарии, код ревью, тестирование - Настя
#  - accept, run - Алёна
#  - up, down - Алина

# Ready tasks:
#  - выход

import os


def acceptCommand():
    correctCommands = ['1', '2', '3', '4', '5', '6', '7']
    while True:
        command = input()
        if command in correctCommands:
            break
        print('Ошибка. Введите действие из списка.')
    return command


def runCommand(command):
    if command == '1':
        pass
    elif command == '2':
        moveUp()
    elif command == '3':
        print('Введите каталог.')
        currentDir = input()
        moveDown(currentDir)
    elif command == '4':
        print(countFiles('????????????????????????????????????'))
    elif command == '5':
        print(countBytes('????????????????????????????????????'))
    elif command == '6':
        print('Введите имя файла.')
        target = input()
        print(findFiles(target, '?????????????????????????????'))
    elif command == '7':
        pass


def moveUp():
    pass


def moveDown(currentDir):
    pass


# TODO (Алина)
def countFiles(path):
    pass


# TODO (Настя)
def countBytes(path):
    pass


# TODO (Алёна)
def findFiles(target, path):
    pass


def main():
    MENU = ''
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print('Работа программы завершена.')
            break