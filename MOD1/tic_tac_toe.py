def tic_tac_toe_winner(board):
    board = list(board)

    #sprawdzenie poprawnosci wejscia
    if len(board) !=9 or abs(board.count('X') - board.count('O')) > 1:
        raise ValueError('Nieprawidłowe wejście')

    combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for combination in combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] and board[combination[0]] != " ":
            return board[combination[0]]

    return None


test_cases = {
    'XXXO O O ': 'X',  # Wygrana X poziomo w pierwszym rzędzie
    'O O XXXOO': 'X',  # Wygrana X poziomo w trzecim rzędzie
    ' OOXOXOX ': 'X',  # Wygrana X poziomo w drugim rzędzie
    'XOXOX X O': 'X',  # Wygrana X pionowo w pierwszej kolumnie
    'OXO X OX ': 'X',  # Wygrana X pionowo w drugiej kolumnie
    'OOXXO OX ': 'X',  # Wygrana X pionowo w trzeciej kolumnie
    'X OXO X O': 'X',  # Wygrana X na przekątnej od lewego górnego rogu do prawego dolnego
    'O XOXO X ': 'X',  # Wygrana X na przekątnej od lewego dolnego rogu do prawego górnego
    'OOOXX X X': 'O',  # Wygrana O poziomo w pierwszym rzędzie
    'X XXOOOO ': 'O',  # Wygrana O poziomo w trzecim rzędzie
    'XOOX OX O': 'O',  # Wygrana O poziomo w drugim rzędzie
    'OXXO OXXO': 'O',  # Wygrana O pionowo w pierwszej kolumnie
    'XOXOXO  X': 'O',  # Wygrana O pionowo w drugiej kolumnie
    'XXOOO XOX': 'O',  # Wygrana O pionowo w trzeciej kolumnie
    'O XXOO XO': 'O',  # Wygrana O na przekątnej od lewego górnego rogu do prawego dolnego
    'X OXO OX ': 'O',  # Wygrana O na przekątnej od lewego dolnego rogu do prawego górnego
    'XXOOXXXOO': None,  # Remis
    'XOXOXO  O': None,  # Gra niezakończona
}

for board, expectation in test_cases.items():
    response  = tic_tac_toe_winner(board)
    assert response == expectation, \
        f'Expected {expectation!r} for {board!r} got {response!r}'



test_cases = {
    'XO  X O X': 'X',
    'OX  O X O': 'O',
    'XXOOXXXOO': None,
    'XXXXXXXXX': ValueError,  # Nieprawidłowe wejście - za dużo X
    '  OOOOOOO': ValueError,  # Nieprawidłowe wejście - za dużo O
    'OXO  OXOX': ValueError,  # Nieprawidłowe wejście - gracze nie wykonują ruchów na zmianę
    'XXXXXOOOOO': ValueError,  # Nieprawidłowe wejście - zbyt długi ciąg
}

for board, expectation in test_cases.items():
    if isinstance(expectation, Exception):
        try:
            response = tic_tac_toe_winner(board)
            print(f'Expected {expectation!r} for {board!r} got {response!r}')
        except expectation:
            pass
    else:
        response = tic_tac_toe_winner(board)
        assert response == expectation, \
            f'Expected {expectation!r} for {board!r} got {response!r}'