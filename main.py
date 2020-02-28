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
        def list_files(startpath):
            for root, dirs, files in os.walk(startpath):
                if dir != '.git':
                    level = root.replace(startpath, '').count(os.sep)
                    indent = ' ' * 4 * (level)
                    print('{}{}/'.format(indent, os.path.basename(root)))
                    subindent = ' ' * 4 * (level + 1)
                    for f in files:
                        print('{}{}'.format(subindent, f))

        startpath = os.getcwd()
        list_files(startpath)
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
        path = os.getcwd()
        findFiles(target, path)

    elif command == '7':
        pass


def moveUp():
    r_catalog = os.getcwd()[:os.getcwd().rfind('\\')]
    os.chdir(r_catalog)


def moveDown(currentDir):
    if os.path.exists(currentDir):
        if os.path.isdir(os.path.abspath(currentDir)):
            os.chdir(os.path.abspath(currentDir))
        else:
            print('error')
    else:
        print('error')


# TODO (Алина)
def countFiles(path):
  moveUp()
  return files_list(path, [], [])
def files_list(path, lst, lst_files):
  for file in os.listdir(path):
    path_1 = os.path.join(path, file)
    if os.path.isfile(path_1):
        lst_files.append(path_1)
    else:
      if path_1 not in lst:
        lst.append(path_1)
      files_list(path_1, lst, lst_files)
  return 'Количество файлов: '+str(len(lst_files))+ '\nКоличество подкаталогов: '+str(len(lst)) +\
         '\nВсего: '+str(len(lst)+len(lst_files))


# TODO (Настя)
def countBytes(path):
    pass


# TODO (Алёна)
def findFiles(target, path):
    for brunch in os.listdir(path):
        if os.path.isfile(os.path.abspath(brunch)):
            if brunch == target:
                print(os.path.abspath(brunch))

        elif os.path.isdir(os.path.abspath(brunch)):
            moveDown(brunch)
            findFiles(target, os.getcwd())
            moveUp()


def main():
    MENU = '+' + '-' * 41 + '+' + '\n' + '''|  1. Просмотр каталога                   |
    |  2. На уровень вверх                    |
    |  3. На уровень вниз                     |
    |  4. Количество файлов и каталогов       |  
    |  5. Размер текущего каталога (в байтах) |
    |  6. Поиск файла                         |
    |  7. Выход из программы                  |''' + '\n' + '+' + '-' * 41 + '+' + '\n' + 'Выберите пункт меню: '

    while True:
        print()
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == '7':
            print()
            print('Работа программы завершена.')
            break


main()
