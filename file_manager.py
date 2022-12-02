import sys
import os
import shutil
import platform


def dec_test(func):
    def inner(*args, **kwargs):
        print('*' * 200)
        result = func(*args, **kwargs)
        return result

    return inner


@dec_test
def who_create():
    name = {
        f'{sys.platform} {os.name} {platform.uname()} {platform.platform()} {platform.architecture()} {platform.system()}'}
    return name


@dec_test
def menu():
    result = f'1. Создать папку\n2. Удалить файл/папку\n3. Копировать файл/папку\n4. Просмотр содержимого рабочей директории\n5. Просмотреть только папки\n6. Просмотреть только файлы\n7. Просмотреть информацию об ОС\n8. Создатель программы\n9. Смена рабочей дирректории*\n10. Выход'
    return result


while True:
    print(menu())

    choice = input('Выберите пункт меню: \n')
    if choice == '1':
        folder = input('Введите имя папки: ')
        print('Такая папка уже есть') if os.path.exists(f'{folder}') else (os.mkdir(folder))
    elif choice == '2':
        del_folder = input('Введите имя папки: ')
        print('Папка удалена'), os.rmdir(f'{del_folder}') if os.path.exists(f'{del_folder}') else print(
            'Папка не найдена!')
    elif choice == '3':
        copy_folder = input('Введите целевой папки: ')
        if os.path.exists(f'{copy_folder}'):
            print(f'Папка {copy_folder} скопирована, введите новое имя папки:')
            new_folder = input()
            shutil.copytree(f'{copy_folder}', f'{new_folder}')
            print('Копия создана!\n')
        else:
            print('Папка не найдена!\n')
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':
        list_folders = [i for i in os.listdir() if os.path.isdir(i)]
        print(list_folders)
    elif choice == '6':
        list_files = [i for i in os.listdir() if os.path.isfile(i)]
        print(list_files)
    elif choice == '7':
        print(who_create())
    elif choice == '8':
        print(f'Автор программы: {os.getlogin()}')
    elif choice == '9':
        print(f'Текущий катлог: {os.getcwd()}')
        link = input('Введите новый путь: ')
        os.chdir(link)
        print(f'Текущий катлог: {os.getcwd()}')
    elif choice == '10':
        break
    else:
        print('Неверный пункт меню')
