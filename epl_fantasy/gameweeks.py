from fantasy_cls import Fixture, Gameweek
from teams import Teams
from utils import ExtendedEnum


class Gameweeks(ExtendedEnum):
    GAMEWEEK_21 = Gameweek(
        number=21,
        fixtures=[
            Fixture(
                home_team=(Teams.VOLTA_CRIS.value, 19),
                away_team=(Teams.PAULINHO_FC.value, 47),
            ),
            Fixture(
                home_team=(Teams.DRAFT_V3.value, 23),
                away_team=(Teams.LIGA_SABSEG_FTW.value, 23),
            ),
            Fixture(
                home_team=(Teams.AL_NASSR.value, 23),
                away_team=(Teams.ZE_MAIA_GT_BINO.value, 28),
            ),
            Fixture(
                home_team=(Teams.GYO_GT_HAALAND.value, 40),
                away_team=(Teams.CHORA_BEBE.value, 46),
            ),
        ],
    )
