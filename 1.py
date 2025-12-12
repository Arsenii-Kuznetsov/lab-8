import os
import re

path = input('Введите путь до директории: ')
try:
    if not os.path.isdir(path):
        exit('Путь не является директорией')
    list_txt_files_directories = [os.path.join(path, x) for x in os.listdir(path) if x.endswith('.txt')]
    if len(list_txt_files_directories) == 0:
        exit('В директории нет файлов txt')
except PermissionError:
    exit('Ошибка доступа')
result = open('result.txt', 'w', encoding='utf-8')
frequently_encountered_words = dict()
for file_txt in list_txt_files_directories:
    try:
        with open(file_txt, encoding='utf-8') as file:
            text = []
            for line in file:
                line = line.lower()
                text += [re.sub(r'[^a-zа-яё\s]', '', line)]
    except PermissionError:
        print(f'Ошибка доступа к файлу {os.path.split(file_txt)[1]}')
        continue
    file_frequently_encountered_words = dict()
    for line in text:
        words = line.split()
        for word in words:
            if word in file_frequently_encountered_words.keys():
                file_frequently_encountered_words[word] += 1
            else:
                file_frequently_encountered_words[word] = 1
    file_frequently_encountered_words_10 = dict(
        sorted(file_frequently_encountered_words.items(), key=lambda x: x[1], reverse=True)[:10])
    file_frequently_encountered_words_10_sorted = dict(sorted(file_frequently_encountered_words_10.items()))
    result.write(
        f'Название файла: {os.path.split(file_txt)[1]}, словарь: {file_frequently_encountered_words_10_sorted}\n')
    for word in file_frequently_encountered_words:
        if word in frequently_encountered_words.keys():
            frequently_encountered_words[word] += file_frequently_encountered_words[word]
        else:
            frequently_encountered_words[word] = file_frequently_encountered_words[word]
frequently_encountered_words_10 = dict(
    sorted(frequently_encountered_words.items(), key=lambda x: x[1], reverse=True)[:10])
frequently_encountered_words_10_sorted = dict(sorted(frequently_encountered_words_10.items()))
result.write(f'Словарь для всех файлов: {frequently_encountered_words_10_sorted}')
result.close()
