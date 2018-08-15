#Alicja Piotrowska, L2
import random


def get_number_of_mines(size_board):
    num = int(input("Wybierz ile min chcesz umieścić na planszy: "))
    if size_board == 1:
        n = 7
    elif size_board == 2:
        n = 10
    else:
        n = 13

    if n*n <= num:
        print("Wybrales za duzo min")
        exit()
    elif num < n:
        print("Wybrales za malo min")
        exit()
    else:
        return num


def deploy_mines(num, size_board):
    if size_board == 1:
        n = 7
    elif size_board == 2:
        n = 10
    else:
        n = 13

    num = num+num

    coordinates = [None] * num

    for a in range(num):
        coordinates[a] = random.randint(0, n-1)

    return coordinates


def create_board(coordinates, size_board):

    if size_board == 1:
        length = 7
        board = [None] * 7
        for i in range(7):
            board[i] = [None] * 7
    if size_board == 2:
        length = 10
        board = [None] * 10
        for i in range(10):
            board[i] = [None] * 10
    if size_board == 3:
        length = 13
        board = [None] * 13
        for i in range(13):
            board[i] = [None] * 13
    a = 0
    z = 0
    while a < length:
        x = coordinates[z]
        y = coordinates[z + 1]
        if board[x][y] != 9:
            board[x][y] = 9
        else:
            board[random.randint(0, length-1)][random.randint(0, length-1)] = 9
        a = a+1
        z = z+2
    return board


def print_board(board):
    w = len(board)  # wiersze
    k = len(board[0])  # kolumny
    print("  ", end=" ")
    for m in range(k):
        if (m > 9):
            print(str(m), end=" ")
        else:
            print(str(m), end=" ")
    print("")
    for m in range(k):
        print("---", end="")
    print("")
    for i in range(w):
        print(chr(65 + i) + "|", end=" ")  # ASCII
        for j in range(k):
            if (j > 9):
                print(str(mapa[i][j]), end="  ")
            else:
                print(str(mapa[i][j]), end=" ")
        print("")


def number_of_neighboring_mines(row, col, board, size_board):
    row = row-1
    col = col-1
    c = 0
    x = row
    y = col
    if row > 0 and col>0:
        for x in range(row - 1, row + 2):
            for y in range(col - 1, col + 2):
                if board[x][y] == 9:
                    c = c + 1
    elif row == 0 and col == 0:
        for x in range(row, row + 2):
            for y in range(col, col + 2):
                if board[x][y] == 9:
                    c = c + 1
    elif row == size_board-1 and col == size_board-1:
        for x in range(row, row + 1):
            for y in range(col, col + 1):
                if board[x][y] == 9:
                    c = c + 1
    elif row == 0 and col > 0:
        for x in range(row, row + 2):
            for y in range(col - 1, col + 2):
                if board[x][y] == 9:
                    c = c + 1
    elif row > 0 and col ==0:
        for x in range(row - 1, row, row + 2):
            for y in range(col, col + 2):
                if board[x][y] == 9:
                    c = c + 1
    elif row > 0 and col == size_board - 1:
        for x in range(row - 1, row + 2):
            for y in range(col, col + 1):
                if board[x][y] == 9:
                    c = c + 1
    elif row == size_board - 1 and col > 0:
        for x in range(row, row + 1):
            for y in range(col - 1, col + 2):
                if board[x][y] == 9:
                    c = c + 1


    return c


def reveal_squears(board, size_board):
    if size_board == 1:
        n = 7
    elif size_board == 2:
        n = 10
    else:
        n = 13

    i = 0
    while i <= n*n:
        row = int(input("Numer wiersza: "))
        col = int(input("Numer kolumny: "))
        if (board[row-1][col-1] == 9):
            print("Bomba! Koniec gry!")
            exit()
        else:
            i = i + 1
            x = number_of_neighboring_mines(row, col, board, n)
            x = str(x)
            print("To miejsce otacza " + x + " bomb")
            print_board(board)

def sapper():
    print("Witaj w grze!")
    print("Wybierz rozmiar planszy: ")
    size_board = int(input("1-mała\n2-średnia\n3-duża\n"))
    if(size_board != 1 and size_board != 2 and size_board != 3):
        print("Nie ma takiej planszy")
        exit()
    num = get_number_of_mines(size_board)
    coordinates = deploy_mines(num, size_board)
    board = create_board(coordinates, size_board)
    #print(coordinates)
    print("Podaj współrzędne pola do odkrycia:")
    reveal_squears(board, num)

    number_of_neighboring_mines(coordinates, size_board)



sapper()


