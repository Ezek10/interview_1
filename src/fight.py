from src.app import logger
from src.players.model import Player
from src.language.es import (
    FIRST_HIT,
    SECOND_PLAYER_DIE,
    FIRST_PLAYER_DIE,
    SECOND_PLAYER_WIN,
    FIRST_PLAYER_WIN,
)


class Fight:
    def __init__(self, player1, player2) -> None:
        self.first, self.second = self._get_order_of_combat(player1, player2)

    def _get_order_of_combat(
        self, player1: Player, player2: Player
    ) -> tuple[Player, Player]:
        actions_1 = player1.get_number_of_actions()
        actions_2 = player2.get_number_of_actions()
        if actions_1 < actions_2:
            first = player1
            second = player2
        elif actions_1 > actions_2:
            first = player2
            second = player1
        else:
            movements_1 = player1.get_number_of_movements()
            movements_2 = player2.get_number_of_movements()
            if movements_1 < movements_2:
                first = player1
                second = player2
            elif movements_1 > movements_2:
                first = player2
                second = player1
            else:
                attacks_1 = player1.get_number_of_attacks()
                attacks_2 = player2.get_number_of_attacks()
                if attacks_1 < attacks_2:
                    first = player1
                    second = player2
                elif attacks_1 > attacks_2:
                    first = player2
                    second = player1
                else:
                    first = player1
                    second = player2

        return first, second

    def start(self):
        total_turns = max(
            self.first.get_amount_of_turns(), self.second.get_amount_of_turns()
        )
        logger.log(FIRST_HIT.format(self.first.name))
        turn = 1
        while turn <= total_turns:
            self.second.recieve_damage(self.first.attack())
            if self.second.is_dead():
                logger.log(SECOND_PLAYER_DIE.format(self.second.name))
                logger.log(
                    FIRST_PLAYER_WIN.format(self.first.name, self.first.get_energy())
                )
                return self.first
            else:
                self.first.recieve_damage(self.second.attack())
                if self.first.is_dead():
                    logger.log(FIRST_PLAYER_DIE.format(self.first.name))
                    logger.log(
                        SECOND_PLAYER_WIN.format(
                            self.second.name, self.second.get_energy()
                        )
                    )
                    return self.second
            turn += 1
