from src.players.arnaldor_shuatseneguer import ArnaldorShuatseneguer

def test_player_starts_with_6_energy():
    player = ArnaldorShuatseneguer(
        movements = [""],
        attacks = [""]
    )
    assert player.get_energy() == 6

def test_number_of_actions():
    player = ArnaldorShuatseneguer(
        movements = ["AWDSA", "", "", ""],
        attacks = ["K", "P", "", "P"]
    )
    assert player.get_number_of_actions() == 8

def test_number_of_movements():
    player = ArnaldorShuatseneguer(
        movements = ["AWDSA", "", "", ""],
        attacks = ["K", "P", "", "P"]
    )
    assert player.get_number_of_movements() == 5

def test_recieve_damage():
    player = ArnaldorShuatseneguer(
        movements = ["AWDSA", "", "", ""],
        attacks = ["K", "P", "", "P"]
    )
    player.recieve_damage(5)
    assert player._energy == 1

def test_is_dead():
    player = ArnaldorShuatseneguer(
        movements = ["AWDSA", "", "", ""],
        attacks = ["K", "P", "", "P"]
    )
    player.recieve_damage(6)
    assert player.is_dead() == True

def test_amount_of_turns():
    player = ArnaldorShuatseneguer(
        movements = ["AWDSA", "", "", ""],
        attacks = ["K", "P", "", "P"]
    )
    assert player.get_amount_of_turns() == 4

def test_attack_with_supper_attack():
    player = ArnaldorShuatseneguer(
        movements = ["ASSA"],
        attacks = ["K"]
    )
    assert player.attack() == 3

def test_attack_with_special_attack():
    player = ArnaldorShuatseneguer(
        movements = ["WASA"],
        attacks = ["P"]
    )
    assert player.attack() == 2

def test_attack_with_kick():
    player = ArnaldorShuatseneguer(
        movements = ["SAA"],
        attacks = ["K"]
    )
    assert player.attack() == 1

def test_attack_with_punch():
    player = ArnaldorShuatseneguer(
        movements = ["ASSA"],
        attacks = ["P"]
    )
    assert player.attack() == 1

def test_no_attack():
    player = ArnaldorShuatseneguer(
        movements = ["ASSA"],
        attacks = [""]
    )
    assert player.attack() == 0
