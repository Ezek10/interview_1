import abc

from src.language.es import KICK, NO_MOVING, PUNCH, SPECIAL_ATTACK, SUPER_ATTACK
from src.logger import logger
from src.utils import MyList


class Player(abc.ABC):
    """Abstract class to model a player in a fight
    """
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
        """returns the energy of the player
        """
        return self._energy

    def get_number_of_actions(self) -> int:
        """returns amount of actions plus attacks

        Returns:
            int: amount of (attacks + movements)
        """
        number_of_actions = 0
        for ii in range(len(self._movements)):
            number_of_actions += len(self._movements[ii]) + len(self._attacks[ii])
        return number_of_actions

    def get_number_of_movements(self) -> int:
        """returns amount of movements plus attacks

        Returns:
            int: amount of movements
        """
        number_of_movements = 0
        for movement in self._movements:
            number_of_movements += len(movement)
        return number_of_movements

    def is_dead(self) -> bool:
        """returns if the player has energy <= 0
        """
        return self._energy <= 0

    def recieve_damage(self, energy: int) -> None:
        """reduce energy by an amount

        Args:
            energy (int): amount to reduce
        """
        self._energy -= energy

    def get_amount_of_turns(self) -> int:
        """returns the total amount of turns based on movements (it should be the same of the attacks)
        """
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
        """realice the attack using the next movements and attacks set in the player

        Returns:
            int: energy that will reduce from the enemy
        """
        movement = self._movements.pop_with_default(0, "")
        attack = self._attacks.pop_with_default(0, "")
        if self._is_super_attack(movement + attack):
            logger.log(SUPER_ATTACK.format(self.name, self.super_attack_name))
            return 3
        elif self._is_special_attack(movement + attack):
            logger.log(SPECIAL_ATTACK.format(self.name, self.special_attack_name))
            return 2
        elif self._is_kick_attack(attack):
            logger.log(KICK.format(self.name))
            return 1
        elif self._is_punch_attack(attack):
            logger.log(PUNCH.format(self.name))
            return 1
        else:
            logger.log(NO_MOVING.format(self.name))
            return 0
