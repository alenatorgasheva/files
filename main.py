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
        print('Где искать?')
        path = input()
        print(countFiles(path))

    elif command == '5':
        print('Где искать?')
        path = input()
        print(countBytes(path))

    elif command == '6':
        print('Введите имя файла.')
        target = input()
        print('Где искать?')
        path = input()
        print(findFiles(target, path))

    elif command == '7':
        pass


def moveUp():
    r_catalog = os.getcwd()[:os.getcwd().rfind('\\')]
    os.chdir(r_catalog)


def moveDown(currentDir):
    if os.path.exists(currentDir):
        os.chdir(os.path.abspath(currentDir))
    else:
        print('error')


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
    MENU = '-' * 43 + '\n' + '''|  1. Просмотр каталога                   |
|  2. На уровень вверх                    |
|  3. На уровень вниз                     |
|  4. Количество файлов и каталогов       |  
|  5. Размер текущего каталога (в байтах) |
|  6. Поиск файла                         |
|  7. Выход из программы                  |''' + '\n' + '-' * 43 + '\n' + 'Выберите пункт меню: '
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print('Работа программы завершена.')
            break
