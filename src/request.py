import pydantic as pd

from src.players.model import Player


class PlayerInput(pd.BaseModel):
    movements: list[pd.constr(pattern="^[AWSDawsd]{0,5}$", to_upper=True)] = pd.Field(alias = "movimientos")
    attacks: list[pd.constr(pattern="^[PKpk]{0,1}$", to_upper=True)] = pd.Field(alias = "golpes")

    def to_player(self, player: Player) -> Player:
        return player(self.movements, self.attacks)


class FightRequest(pd.BaseModel):
    player1: PlayerInput
    player2: PlayerInput
