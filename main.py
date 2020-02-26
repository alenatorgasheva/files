# Case - study #7
# This program shows information about filing system.

# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

# Tasks:
#  - локализация, комментарии, код ревью, тестирование

# Ready tasks:
#  - выход

import os


def acceptCommand():
    # ввод команды и одобрение ее
    pass


def runCommand(command):
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