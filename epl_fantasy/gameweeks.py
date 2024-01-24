from fantasy_cls import Fixture, Gameweek
from teams import Teams
from utils import ExtendedEnum


class Gameweeks(ExtendedEnum):
    GAMEWEEK_21 = Gameweek(
        number=21,
        fixtures=[
            Fixture(
                home_team=(Teams.VOLTA_CRIS.value, 56),
                away_team=(Teams.PAULINHO_FC.value, 71),
            ),
            Fixture(
                home_team=(Teams.DRAFT_V3.value, 28),
                away_team=(Teams.LIGA_SABSEG_FTW.value, 30),
            ),
            Fixture(
                home_team=(Teams.AL_NASSR.value, 55),
                away_team=(Teams.ZE_MAIA_GT_BINO.value, 37),
            ),
            Fixture(
                home_team=(Teams.GYO_GT_HAALAND.value, 51),
                away_team=(Teams.CHORA_BEBE.value, 69),
            ),
        ],
    )
