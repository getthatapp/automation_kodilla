import pytest
from os import unlink, close
from tempfile import mkstemp
from sqlalchemy import create_engine
from itertools import count
import Mock

from tic_tac_toe.database import metadata, history, winner


@pytest.fixture
def create_games(database_connection):

    def game_creator(*games):
        move_id = count(1)
        for game_id, moves in enumerate(games, 1):
            database_connection.execute(history.insert(), [
                {
                    'game_id': game_id,
                    'move_id': next(move_id),
                    'position': int(position),
                    'symbol': symbol
                } for position, symbol in zip(moves[::2], moves[1::2])
            ])

    return game_creator


@pytest.fixture
def database_connection():
    fd, name = mkstemp(prefix='test_winner_', suffix='.sqlite')
    engine = create_engine(f'sqlite:///{name}')
    metadata.create_all(engine)
    with engine.connect() as connection:
        yield connection
    close(fd)
    unlink(name)


@pytest.fixture
def connection_mock():
    return lambda moves: Mock(
        execute=Mock(
            return_value=[
                (int(position), symbol)
                for position, symbol
                in zip(moves[::2], moves[1::2])
            ]
        )
    )


def test_3x_in_a_column(database_connection, create_games):
    assert winner(connection_mock('4X105X302X608X'), None) == 'X'


def test_create_board_from_moves(connection_mock, monkeypatch):
    monkeypatch.setattr(
        'tic_tac_toe.database.tic_tac_toe_winner',
        lambda board: board
    )
    assert winner(connection_mock('4X105X302X608X'), None) == ' OXOXXO X'

