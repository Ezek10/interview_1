import pydantic as pd

from src.players.model import Player


class Movimiento(pd.BaseModel):
    mov: str = pd.Field(pattern="^[AWSDawsd]{0,5}$")


class Golpe(pd.BaseModel):
    golpe: str = pd.Field(pattern="^[PKpk]{0,1}$")


class PlayerInput(pd.BaseModel):
    movimientos: list[str]
    golpes: list[str]

    def to_player(self, player: Player) -> Player:
        return player(self.movimientos, self.golpes)


class FightRequest(pd.BaseModel):
    player1: PlayerInput
    player2: PlayerInput
