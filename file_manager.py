import sys
import os
import shutil
import platform

while True:
    print('1. Создать папку')
    print('2. Удалить файл/папку')
    print('3. Копировать файл/папку')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Просмотреть только папки')
    print('6. Просмотреть только файлы')
    print('7. Просмотреть информацию об ОС')
    print('8. Создатель программы')
    print('9. Смена рабочей дирректории*')
    print('10. Выход')

    choice = input('Выберите пункт меню: \n')
    if choice == '1':
        folder = input('Введите имя папки: ')
        if os.path.exists(f'{folder}'):
            print('Такая папка уже есть!\n')
        else:
            os.mkdir(f'{folder}')
            print('Папка создана!\n')
    elif choice == '2':
        del_folder = input('Введите имя папки: ')
        if os.path.exists(f'{del_folder}'):
            print(f'Папка {del_folder} удалена! ')
            os.rmdir(f'{del_folder}')
        else:
            print('Папка не найдена!')
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
        list_folders = []
        for i in os.listdir():
            if os.path.isdir(i):
                list_folders.append(i)
        print(list_folders)
    elif choice == '6':
        list_files = []
        for i in os.listdir():
            if os.path.isfile(i):
                list_files.append(i)
        print(list_files)
    elif choice == '7':
        print(sys.platform)
        print(os.name)
        print(platform.uname())
        print(platform.platform())
        print(platform.architecture())
        print(platform.system())
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
