# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
def create_folders():
    import os
    for i in range(1,10):
        dir_path = os.path.join(os.getcwd(), 'folder_'+ str(i))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
                print('Такая директория уже существует')
    # И второй скрипт, удаляющий эти папки.
def remove_folders():
    import os
    confirm = input("Действительно хотите удалить созданные папки? Y/N")
    if confirm == "Y" or "y":
        for i in range(1,10):
            dir_del = os.path.join(os.getcwd(),'folder_'+ str(i))
            if os.path.exists(dir_del):
                try:
                    os.rmdir(dir_del)
                    print("Все папки были удалены")
                except FileExistsError:
                    print("Здесь таких папок нет!")
    else:
        print("Операция отменена")
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_folders():
    import os
    currentDir = os.getcwd()
    folders =  [i for i in os.listdir(currentDir) \
    if os.path.isdir(os.path.join(currentDir, i))]
    print (folders)
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_me():
    import shutil
    file_name = os.path.basename(__file__)
    shutil.copy(file_name, file_name+'.dupl')
