
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

win_combination = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


def step_maps(step, symbol):
    place = maps.index(step)
    maps[place] = symbol


def get_result():
    winner = ""

    for i in win_combination:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            winner = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            winner = "O"

    return winner
game_over = False
player1 = True

while game_over == False:
    print_maps()

    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))

    step_maps(step, symbol)
    winner = get_result()
    if winner != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

print_maps()
print("Победил", winner)







