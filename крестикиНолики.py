# игра КРЕСТИКИ НОЛИКИ
# инструкция
def instruction():
    print(
    '''
    Добро пожаловать. В схватке сойдутся челевек и комп за доской игры Крестики
    Нолики. Чтобы сделать ход введи число от 0 до 8
    Числа соответствуют полям доски как показано ниже:
    0 | 1 | 2 |
    3 | 4 | 5 |
    6 | 7 | 8 |
    Начнем сражение!
        '''
    )
    input('Нажмите Еnter чтобы выйти')

# глобальные константы
X = 'x'
O = 'o'
EMPTY = ' '
TIE = 'ничья'
NUM_SQUARES = 9

def ask_yes_or_no(question):  # задает вопрос с ответом ДА или НЕТ
    response = None
    while response not in('y', 'n'):
        response = input(question).lower()
    return response

def ask_number(question, low, high):  # прости ввести число из диапазона
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def choice():
    go_first = ask_yes_or_no('Хочешь оставить за собой певый ход? (Y/N): ')
    if go_first == 'y':
        print('начинать и играть  крестиками будет человек.')
        human = X
        computer = O
    else:
        print("начинать и играть крестиками будет компьютер.")
        computer = X
        human = O
    return computer, human
# создаем новую игровую доску

def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

# печатаем доску на экране

def display_board(board):
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t', '__________')
    print('\t', board[3], '|', board[4], '|', board[5])
    print('\t', '__________')
    print('\t', board[6], '|', board[7], '|', board[8])

# создаем список доступных ходов

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    WAY_TO_WIN = ((0, 1, 2),
                  (3, 4, 5),
                  (6, 7, 8),
                  (0, 3, 6),
                  (1, 4, 7),
                  (2, 5, 8),
                  (0, 4, 8),
                  (2, 4, 6))
    for row in WAY_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner




