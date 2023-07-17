from app import logger
from players.model import Player


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
        logger.log(f"El combate comenzo! {self.first.name} dara el primer golpe")
        turn = 1
        while turn <= total_turns:
            self.second.recieve_damage(self.first.attack())
            if self.second.is_dead():
                logger.log(f"{self.second.name} murio, sus familiares quizas lo lloren")
                logger.log(
                    f"{self.first.name} gano, y le sobro \
                    {self.first.get_energy()} de energia"
                )
                return self.first
            else:
                self.first.recieve_damage(self.second.attack())
                if self.first.is_dead():
                    logger.log(
                        f"{self.first.name} murio, sus familiares van \
                        a llorarlo toda su vida"
                    )
                    logger.log(
                        f"{self.second.name} sobrevivio, y \
                        le quedo {self.second.get_energy()} energia"
                    )
                    return self.second
            turn += 1
