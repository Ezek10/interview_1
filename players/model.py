import abc

from app import logger
from utils import MyList


class Player(abc.ABC):
    name: str
    super_attack: str
    special_attack: str
    super_attack_name: str
    special_attack_name: str
    _energy = 6

    def __init__(self, movements: MyList[str], attacks: MyList[str]) -> None:
        self._movements = MyList(movements)
        self._attacks = MyList(attacks)

    def get_energy(self) -> int:
        return self._energy

    def get_number_of_actions(self) -> int:
        number_of_actions = 0
        for ii in range(len(self._movements)):
            number_of_actions += len(self._movements[ii]) + len(self._attacks[ii])
        return number_of_actions

    def get_number_of_movements(self) -> int:
        number_of_movements = 0
        for movement in self._movements:
            number_of_movements += len(movement)
        return number_of_movements

    def get_number_of_attacks(self) -> int:
        number_of_attacks = 0
        for attack in self._attacks:
            number_of_attacks += len(attack)
        return number_of_attacks

    def is_dead(self) -> bool:
        return self._energy <= 0

    def recieve_damage(self, energy: int) -> None:
        self._energy -= energy

    def get_amount_of_turns(self) -> int:
        return len(self._movements)

    def _is_super_attack(self, action: str) -> bool:
        return self.super_attack in action

    def _is_special_attack(self, action: str) -> bool:
        return self.special_attack in action

    def _is_kick_attack(self, attack: str) -> bool:
        return attack == "K"

    def _is_punch_attack(self, attack: str) -> bool:
        return attack == "P"

    def attack(self) -> int:
        movement = self._movements.pop_with_default(0, "")
        attack = self._attacks.pop_with_default(0, "")
        if self._is_super_attack(movement + attack):
            logger.log(f"{self.name} lo revento con un {self.super_attack_name}")
            return 3
        elif self._is_special_attack(movement + attack):
            logger.log(f"{self.name} conecto un {self.special_attack_name}")
            return 2
        elif self._is_kick_attack(attack):
            logger.log(f"{self.name} dio una gran patada")
            return 1
        elif self._is_punch_attack(attack):
            logger.log(f"{self.name} dio un puñetazo")
            return 1
        else:
            logger.log(
                f"{self.name} se olvido que esta \
                peleando a muerte y se mueve sin atacar"
            )
            return 0
