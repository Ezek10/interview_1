from src.fight import Fight
from src.players.tonyn_stallone import TonynStallone


def test_order_of_combat_by_actions():
    player_1 = TonynStallone(
        movements=["D"],
        attacks=["K"]
    )
    player_2 = TonynStallone(
        movements=["SA"],
        attacks=["K"]
    )
    fight = Fight(player_1, player_2)
    assert fight.first == player_1
    assert fight.second == player_2

def test_order_of_combat_by_movements():
    player_1 = TonynStallone(
        movements=["D", ""],
        attacks=["K", "P"]
    )
    player_2 = TonynStallone(
        movements=["SA", ""],
        attacks=["K", ""]
    )
    fight = Fight(player_1, player_2)
    assert fight.first == player_1
    assert fight.second == player_2

def test_order_of_combat_by_player_1():
    player_1 = TonynStallone(
        movements=["AS"],
        attacks=["K"]
    )
    player_2 = TonynStallone(
        movements=["AS"],
        attacks=["K"]
    )
    fight = Fight(player_1, player_2)
    assert fight.first == player_1
    assert fight.second == player_2

def test_fight_draw():
    player_1 = TonynStallone(
        movements=["AS"],
        attacks=["K"]
    )
    player_2 = TonynStallone(
        movements=["AS"],
        attacks=["K"]
    )
    fight = Fight(player_1, player_2)
    winner = fight.start()
    assert winner is None

def test_fight_end_immediately():
    player_1 = TonynStallone(
        movements=["DSD", "DSD"],
        attacks=["P", "P"]
    )
    player_2 = TonynStallone(
        movements=["DSD", "DSD"],
        attacks=["P", "P"]
    )
    fight = Fight(player_1, player_2)
    winner = fight.start()
    assert winner is player_1

def test_fight_win_player_2():
    player_1 = TonynStallone(
        movements=["DSD", "DSD"],
        attacks=["P", "K"]
    )
    player_2 = TonynStallone(
        movements=["DSD", "DSD"],
        attacks=["P", "P"]
    )
    fight = Fight(player_1, player_2)
    winner = fight.start()
    assert winner is player_2
