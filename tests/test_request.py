from pydantic import ValidationError

from src.request import FightRequest
from src.players.model import Player

class RequestMother():
    def get_players():
        player1 = {
            "movimientos": ["AWDSa", "a"],
            "golpes": ["K", "p"]
        }
        player2 = {
            "movimientos": ["s", "asdwS"],
            "golpes": ["k", "P"]
        }
        return (player1, player2)
    
    def get_players_with_empty_movements():
        player1 = {
            "movimientos": ["", ""],
            "golpes": ["K", "p"]
        }
        player2 = {
            "movimientos": ["", ""],
            "golpes": ["k", "P"]
        }
        return (player1, player2)

    def get_players_with_wrong_movements():
        player1 = {
            "movimientos": ["zc", "asddwa"],
            "golpes": ["K", "p"]
        }
        player2 = {
            "movimientos": ["bdN", "C15"],
            "golpes": ["k", "P"]
        }
        return (player1, player2)

    def get_players_with_wrong_attacks():
        player1 = {
            "movimientos": ["dwW", "ASD"],
            "golpes": ["x", "pP"]
        }
        player2 = {
            "movimientos": ["DS", "awdsa"],
            "golpes": ["N", "Pk"]
        }
        return (player1, player2)

    def get_players_with_no_structure():
        player1 = {
            "movimientos": "a",
            "golpes": "p"
        }
        player2 = {}
        return (player1, player2)


def test_input_ok():
    player1 ,player2 = RequestMother.get_players()
    FightRequest(player1=player1, player2=player2)
    assert True

def test_input_ok_with_empty_movements():
    player1 ,player2 = RequestMother.get_players_with_empty_movements()
    FightRequest(player1=player1, player2=player2)
    assert True

def test_create_model_ok():
    player1 ,player2 = RequestMother.get_players()
    request = FightRequest(player1=player1, player2=player2)
    class PlayerImpl(Player):
        pass
    player1_model = request.player1.to_player(PlayerImpl)
    assert type(player1_model) == PlayerImpl

def test_raise_with_one_player_only():
    player1 , _ = RequestMother.get_players()
    try:
        FightRequest(player1=player1, player2=None)
        assert False
    except ValidationError:
        assert True

def test_raise_with_no_structure():
    player1 , _ = RequestMother.get_players_with_no_structure()
    try:
        FightRequest(player1=player1, player2=None)
        assert False
    except ValidationError:
        assert True

def test_raise_with_wrong_movement():
    player1 ,player2 = RequestMother.get_players_with_wrong_movements()
    try:
        FightRequest(player1=player1, player2=player2)
        assert False
    except ValidationError:
        assert True

def test_raise_with_wrong_attacks():
    player1 ,player2 = RequestMother.get_players_with_wrong_attacks()
    try:
        FightRequest(player1=player1, player2=player2)
        assert False
    except ValidationError:
        assert True

def test_strings_to_uppercase():
    player1 ,player2 = RequestMother.get_players()
    request = FightRequest(player1=player1, player2=player2)
    for movement in request.player1.movements:
        assert movement.isupper()
    for attack in request.player1.attacks:
        assert attack.isupper()
