import pydantic as pd

from src.players.model import Player


class PlayerInput(pd.BaseModel):
    """Expected request for a player input
    """
    movements: list[pd.constr(pattern="^[AWSDawsd]{0,5}$", to_upper=True)] = pd.Field(
        alias="movimientos"
    )
    attacks: list[pd.constr(pattern="^[PKpk]{0,1}$", to_upper=True)] = pd.Field(
        alias="golpes"
    )

    def to_player(self, player: Player) -> Player:
        """map the input to a specific implementation of a player

        Args:
            player (Player): implementation of a Player

        Returns:
            Player: instance of the player
        """
        return player(self.movements, self.attacks)


class FightRequest(pd.BaseModel):
    """Request expected for a Fight with validation
    """
    player1: PlayerInput
    player2: PlayerInput
