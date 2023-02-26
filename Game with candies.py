# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

player_1 = input('Игрок №1, введите имя: ')
player_2 = input('Игрок №2, введите имя: ')

candies = int(input('Введите колчество конфет: '))

rand = random.randint(1, 2)

print(rand)

if rand == 1:
    print('Первый ход делает ' + player_1)
if rand == 2:
    print('Первый ход делает ' + player_2)


while candies > 0:
    if rand == 1:
        print(player_1 + ', введите количество конфет до 28: ')
        player_1_choice = int(input())
        candies = candies - player_1_choice
        if player_1_choice > 28:
            print('Неверное количество, введите снова: ')
            player_1_choice = int(input())
        if player_1_choice > candies:
            print('Неверное количество, введите снова: ')
            player_1_choice = int(input())
        if candies <= 0:
            print('Победил игрок 1')
            break
        print(f'Осталось {candies}')
        print(player_2 + ', введите количество конфет до 28: ')
        player_2_choice = int(input())
        candies = candies - player_2_choice
        if player_2_choice > 28:
            print('Неверное количество, введите снова: ')
            player_2_choice = int(input())
        if player_2_choice > candies:
            print('Неверное количество, введите снова: ')
            player_2_choice = int(input())
        if candies <= 0:
            print('Победил игрок 2')
            break
        print(f'Осталось {candies}')
    if rand == 2:
        print(player_2 + ', введите количество конфет до 28: ')
        player_2_choice = int(input())
        candies = candies - player_2_choice
        if player_2_choice > 28:
            print('Неверное количество, введите снова: ')
            player_2_choice = int(input())
        if player_2_choice > candies:
            print('Неверное количество, введите снова: ')
            player_2_choice = int(input())
        if candies <= 0:
            print('Победил игрок 2')
            break
        print(f'Осталось {candies}')
        print(player_1 + ', введите количество конфет до 28: ')
        player_1_choice = int(input())
        candies = candies - player_1_choice
        if player_1_choice > 28:
            print('Неверное количество, введите снова: ')
            player_1_choice = int(input())
        if player_1_choice > candies:
            print('Неверное количество, введите снова: ')
            player_1_choice = int(input())
        if candies <= 0:
            print('Победил игрок 1')
            break
        print(f'Осталось {candies}')