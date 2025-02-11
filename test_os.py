import os
import time


directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.abspath(file)
        filetime = os.path.getmtime(os.listdir()[0])
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(os.listdir()[0])
        parent_dir = os.path.dirname(os.path.abspath(file))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: '
              f'{formatted_time}, \nРодительская директория: {parent_dir}')