import pytest


def test_tic_tac_toe_winner():
    try:
        assert callable(tic_tac_toe_winner), "tic_tac_toe not callable"
    except ImportError as e:
        assert False, e


def test_empty_board():
    assert tic_tac_toe_winner(' ' * 9) is None


def test_3x_in_a_row():
    winner = tic_tac_toe_winner('XXX      ')
    assert winner == 'X', f"expected X, got {winner}"


def test_illegal_board_symbols():
    try:
        tic_tac_toe_winner('Ala ma kota')
        assert False, "ValueError expected"
    except ValueError:
        pass


def test_illegal_board_size():
    try:
        tic_tac_toe_winner('XXX')
        assert False, "ValueError expected"
    except ValueError:
        pass


def test_3X_diagonally():
    assert tic_tac_toe_winner('XO OX   X') == 'X'


def test_too_large_board():
    with pytest.raises(ValueError):
        tic_tac_toe_winner('XOOOXXXXOX')


if __name__ == '__main__':
    for test in (
        test_tic_tac_toe_winner,
    ):
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)




