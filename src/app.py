from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.fight import Fight
from src.logger import logger
from src.players.arnaldor_shuatseneguer import ArnaldorShuatseneguer
from src.players.tonyn_stallone import TonynStallone
from src.request import FightRequest

app = FastAPI()


@app.post("/fight")
async def talana_jrpg(request: FightRequest) -> list[str]:
    player1 = request.player1.to_player(TonynStallone)
    player2 = request.player2.to_player(ArnaldorShuatseneguer)
    fight = Fight(player1, player2)
    fight.start()
    content = logger.get_all_logs()
    logger.clean()
    return JSONResponse(status_code=200, content=content)
