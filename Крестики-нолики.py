from tkinter import * 
from tkinter import messagebox

board = list(range(1, 10))
win_comb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def my_board():
    for i in range(3):
        print('|', board[0 + i*3], '|',
              board[1 + i*3], '|', board[2 + i*3], '|')


def take_input(player_symb):
    while True:
        print('Выберите позицию: ' + player_symb)
        value = input()
        if not value in '123456789':
            print('Введите заново: ')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Недопустимый ход')
            continue
        board[value-1] = player_symb
        break


def win():
    for each in win_comb:
        if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        my_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = win()
            if winner:
                my_board()
                print(winner, 'WIN')
                break
        counter += 1
        if counter > 8:
            my_board()
            print('None win')
            break

main()