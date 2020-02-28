# Case - study #7
# This program shows information about filing system.

# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

import os


def acceptCommand():
    """
    Function for input check.
    :return: correct command
    """
    correctCommands = ['1', '2', '3', '4', '5', '6', '7']
    while True:
        command = input()
        if command in correctCommands:
            break
        print('Ошибка. Введите действие из списка.')
    return command


def runCommand(command):
    """
    Function for running command.
    :param command: command to run
    """
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
        if not findFiles(target, path, False):
            print('Файл не найден.')

    elif command == '7':
        pass


def moveUp():
    """
    Function for making the parent directory current.
    :return: None
    """
    root = os.getcwd()[:os.getcwd().rfind('\\')]
    os.chdir(root)


def moveDown(currentDir):
    """
    Function for making the required directory current.
    :param currentDir: a name of the subdirectory
    :return: None
    """
    if os.path.exists(currentDir):
        if os.path.isdir(os.path.abspath(currentDir)):
            os.chdir(os.path.abspath(currentDir))
        else:
            print('error')
    else:
        print('error')


def countFiles(path):
    """
    Wrapper function.
    :param path: a directory name
    :return: number files and subdirectories
    """
    moveUp()
    return files_list(path, [], [])


def files_list(path, dirs, files):
    """
    Recursive function calculating the number of files and subdirectories in the required directory.
    :param path: a directory name
    :param dirs: list of all subdirectories in the current directory
    :param files: list of all files in the current directory
    :return: number files and subdirectories
    """
    for file in os.listdir(path):
        path_1 = os.path.join(path, file)
        if os.path.isfile(path_1):
            files.append(path_1)
        else:
            if path_1 not in dirs:
                dirs.append(path_1)
            files_list(path_1, dirs, files)
    return 'Количество файлов: ' + str(len(files)) + \
           '\nКоличество подкаталогов: ' + str(len(dirs)) + \
           '\nВсего: ' + str(len(dirs) + len(files))


def countBytes(path):
    pass


def findFiles(target, path, search):
    """
    Function for searching file.
    :param target: file name
    :param path: current path
    :param search: whether a file is found
    :return: whether a file is found
    """
    for name in os.listdir(path):
        if os.path.isfile(os.path.abspath(name)):
            if name == target:
                print(os.path.abspath(name))
                search = True

        elif os.path.isdir(os.path.abspath(name)):
            moveDown(name)
            search = findFiles(target, os.getcwd(), search)
            moveUp()
    return search


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
