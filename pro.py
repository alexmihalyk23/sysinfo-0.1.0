# coding : utf-8
import os, sys
import psutil
line = "--------------------------------------"
do = 0

def systemInfo():
    print("Вот что я знаю о компьютере: ")
    print("Количество логических ЦП: ", psutil.cpu_count())
    print("Платформа: ", sys.platform)
    print("Кодировка файловой системы: ", sys.getfilesystemencoding())
    print("Текущая директория: ", os.getcwd(), "\n")

while do != 9:
    print(line)
    print("[1] - Показать директорию")
    print("[2] - Информация о Компьютере")
    print("[3] - Количество логических ЦП")
    print("[9] - Выход ")
    print(line)
    do = int(input("Выберите действие: "))
    print(line)
    if do == 1:
        print(os.listdir(), "\n")
    elif do == 2:
        systemInfo()
        #print("Текущий пользователь: ", os.getlogin())
    elif do == 3:
        print("Количество логических ЦП: ", psutil.cpu_count())
    elif do == 4:
        print("Количество логических ЦП: ", psutil.cpu_count())
    else:
        pass
