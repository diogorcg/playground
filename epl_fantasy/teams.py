from fantasy_cls import FirstRoundInfo, Team
from utils import ExtendedEnum


class FirstRoundInfoTeams(ExtendedEnum):
    AL_NASSR = FirstRoundInfo(
        wins=10,
        draws=0,
        losses=7,
        points_scored=606,
    )
    CHORA_BEBE = FirstRoundInfo(
        wins=6,
        draws=1,
        losses=10,
        points_scored=710,
    )
    DRAFT_V3 = FirstRoundInfo(
        wins=13,
        draws=1,
        losses=3,
        points_scored=881,
    )
    GYO_GT_HAALAND = FirstRoundInfo(
        wins=9,
        draws=0,
        losses=8,
        points_scored=616,
    )
    LIGA_SABSEG_FTW = FirstRoundInfo(
        wins=7,
        draws=1,
        losses=9,
        points_scored=669,
    )
    PAULINHO_FC = FirstRoundInfo(
        wins=4,
        draws=0,
        losses=13,
        points_scored=684,
    )
    VOLTA_CRIS = FirstRoundInfo(
        wins=8,
        draws=1,
        losses=8,
        points_scored=643,
    )
    ZE_MAIA_GT_BINO = FirstRoundInfo(
        wins=9,
        draws=0,
        losses=8,
        points_scored=770,
    )


class Teams(ExtendedEnum):
    AL_NASSR = Team(
        player_name="João Meneses",
        team_name="Al-Nassr",
        first_round_info=FirstRoundInfoTeams.AL_NASSR.value,
    )
    CHORA_BEBE = Team(
        player_name="Miguel Meneses",
        team_name="Chora Bebé",
        first_round_info=FirstRoundInfoTeams.CHORA_BEBE.value,
    )
    DRAFT_V3 = Team(
        player_name="Pedro Ribeiro",
        team_name="Draft v3",
        first_round_info=FirstRoundInfoTeams.DRAFT_V3.value,
    )
    GYO_GT_HAALAND = Team(
        player_name="Nuno Ribeiro",
        team_name="Gyo>haaland",
        first_round_info=FirstRoundInfoTeams.GYO_GT_HAALAND.value,
    )
    LIGA_SABSEG_FTW = Team(
        player_name="José Alves",
        team_name="Liga SabSeg FTW",
        first_round_info=FirstRoundInfoTeams.LIGA_SABSEG_FTW.value,
    )
    PAULINHO_FC = Team(
        player_name="Pedro Gonçalves",
        team_name="Paulinho FC",
        first_round_info=FirstRoundInfoTeams.PAULINHO_FC.value,
    )
    VOLTA_CRIS = Team(
        player_name="Diogo Gonçalves",
        team_name="Volta Cris",
        first_round_info=FirstRoundInfoTeams.VOLTA_CRIS.value,
    )
    ZE_MAIA_GT_BINO = Team(
        player_name="José Maia",
        team_name="Zé Maia > Bino",
        first_round_info=FirstRoundInfoTeams.ZE_MAIA_GT_BINO.value,
    )
