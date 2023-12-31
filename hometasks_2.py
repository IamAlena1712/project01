# -*- coding: utf-8 -*-
"""Hometasks_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uUcbse7TLYvAt5IaHPPKgF3sXPg_yFUs
"""

#Домашнее задание 2

# Lvl 1 Задача 1
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

splitted_line = my_favorite_songs.split(',')
print((splitted_line)[0], (splitted_line)[4], (splitted_line)[1], (splitted_line)[3])

# Lvl 1 Задача 2


# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]



import random

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

print("Время звучания трех случайных песен - ", random.choice(my_favorite_songs)[1] + random.choice(my_favorite_songs)[1] + random.choice(my_favorite_songs)[1], "минут" )



# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
import random

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
    }


print(random.choice(list(my_favorite_songs_dict.values()))+ random.choice(list(my_favorite_songs_dict.values())) + random.choice(list(my_favorite_songs_dict.values())))



# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца,
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

month =int(input("Введите номер месяца "))

#print(month)

year = (["Январь", 31], ["Февраль", 28], ["Март", 31], ["Апрель", 30], ["Май", 31], ["Июнь", 30], ["Июль", 31], ["Август", 31], ["Сентябрь", 30], ["Октябрь", 31], ["Ноябрь", 30], ["Декабрь", 31])

if month == 1:
  print("Вы ввели '{}'. {} дней".format(year [0][0], year[0][1]))

elif month == 2:
  print("Вы ввели '{}'. {} дней".format(year [1][0], year[1][1]))

elif month == 3:
  print("Вы ввели '{}'. {} дней".format(year [2][0], year[2][1]))

elif month == 4:
  print("Вы ввели '{}'. {} дней".format(year [3][0], year[3][1]))

elif month == 5:
  print("Вы ввели '{}'. {} дней".format(year [4][0], year[4][1]))

elif month == 6:
  print("Вы ввели '{}'. {} дней".format(year [5][0], year[5][1]))

elif month == 7:
  print("Вы ввели '{}'. {} дней".format(year [6][0], year[6][1]))

elif month == 8:
  print("Вы ввели '{}'. {} дней".format(year [7][0], year[7][1]))

elif month == 9:
  print("Вы ввели '{}'. {} дней".format(year [8][0], year[8][1]))

elif month == 10:
  print("Вы ввели '{}'. {} дней".format(year [9][0], year[9][1]))

elif month == 11:
  print("Вы ввели '{}'. {} дней".format(year [10][0], year[10][1]))

elif month == 12:
  print("Вы ввели '{}'. {} дней".format(year [11][0], year[11][1]))

elif month > 12:
  print("Такого месяца нет!")

from re import X
# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.


# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

for title, code in titles.items():
    total_quantity = 0
    total_cost = 0
    for titles in store[code]:
        total_quantity += titles['quantity']
        total_cost += titles['price']
    print(title, " - ",total_quantity," шт, ",total_cost * total_quantity," руб")

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"