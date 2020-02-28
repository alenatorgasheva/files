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
        print(lc.TXT_ERROR)
    return command


def runCommand(command):
    """
    Function for running command.
    :param command: command to run
    """
    if command == lc.TXT_ONE:
        print()
        startpath = os.getcwd()
        list_files(startpath)

    elif command == lc.TXT_TWO:
        moveUp()

    elif command == lc.TXT_THREE:
        print(lc.TXT_DIR)
        currentDir = input()
        moveDown(currentDir)

    elif command == lc.TXT_FOUR:
        print()
        path = os.path.split(os.getcwd())[-1]
        print(countFiles(path))

    elif command == lc.TXT_FIVE:
        path = os.getcwd()
        print()
        print(countBytes(path))

    elif command == lc.TXT_SIX:
        print(lc.TXT_NAME)
        target = input()
        print()
        path = os.getcwd()
        if not findFiles(target, path, False):
            print(lc.TXT_FILE)

    elif command == lc.TXT_SEVEN:
        pass

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        if dir != '.git':
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))
def moveUp():
    """
    Function for making the parent directory current.
    """
    os.chdir('..')


def moveDown(currentDir):
    """
    Function for making the required directory current.
    :param currentDir: a name of the subdirectory
    """
    if os.path.exists(currentDir):
        if os.path.isdir(os.path.abspath(currentDir)):
            os.chdir(os.path.abspath(currentDir))
        else:
            print()
            print(lc.TXT_ERROR_1)
    else:
        print()
        print(lc.TXT_ERROR_2)


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
    return lc.TXT_FILE_1 + str(len(files)) + \
           lc.TXT_DIR_1 + str(len(dirs)) + \
           lc.TXT_ALL + str(len(dirs) + len(files))


def countBytes(path):
    """
    Function for calculating the total volume (in bytes) of all files in the pass directory
    :param path: a directory name
    :return: volume (in bytes) of all files in the pass directory
    """
    size = 0
    for branch in os.listdir(path):
        if os.path.isfile(os.path.abspath(branch)) or os.path.isdir(os.path.abspath(branch)):
            size = os.path.getsize(path)
        else:
            countBytes(os.path.getsize(path))
    return size


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
    # Choosing the language
    language = input('Choose your language:\n1. English\n2. Russian\n').lower()
    while True:
        if language == 'english' or language == 'eng' or \
                language == 'e' or language == '1':
            import lc_eng as lc
            break
        elif language == 'russian' or language == 'rus' or \
                language == 'r' or language == '2':
            import lc_rus as lc
            break
        language = input('Please, choose language from proposed: ')

    MENU = '+' + '-' * 41 + '+' + '\n' + lc.TXT_MENU + '\n' + '+' + '-' * 41 + '+' + '\n' + lc.TXT_MENU_1

    while True:
        print()
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == lc.TXT_SEVEN:
            print()
            print(lc.TXT_END)
            break


main()
