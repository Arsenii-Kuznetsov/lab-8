import os

path = input('Введите путь до файла: ')
try:
    if not os.path.isfile(path):
        exit('Путь не является файлом')
except PermissionError:
    exit('Ошибка доступа')
if os.path.splitext(path)[1] != '.txt':
    exit('Файл должен иметь расширение txt')
with open(path) as file:
    weather = dict()
    for line in file:
        date, temperature = line.split(';')
        month = date.split('-')[1]
        if month in weather.keys():
            weather[month] += [float(temperature)]
        else:
            weather[month] = [float(temperature)]
for month in weather:
    temperature_list = weather[month]
    weather[month] = (sum(temperature_list) / len(temperature_list), max(temperature_list), min(temperature_list))
months = (
    'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
for month in weather:
    print(
        f'{months[int(month) - 1]}: средняя температура: {weather[month][0]}, максимальная температура: {weather[month][1]}, минимальная температура: {weather[month][2]}')
