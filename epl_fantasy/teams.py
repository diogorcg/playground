from fantasy_cls import FirstRoundInfo, Team
from utils import ExtendedEnum


class FirstRoundInfoTeams(ExtendedEnum):
    AL_NASSR = FirstRoundInfo(
        matches_won=11,
        matches_drawn=0,
        matches_lost=7,
        points_for=661,
        total=33,
        points_against=663,
    )
    CHORA_BEBE = FirstRoundInfo(
        matches_won=7,
        matches_drawn=1,
        matches_lost=10,
        points_for=779,
        points_against=784,
        total=22,
    )
    DRAFT_V3 = FirstRoundInfo(
        matches_won=13,
        matches_drawn=1,
        matches_lost=4,
        points_for=909,
        points_against=632,
        total=40,
    )
    GYO_GT_HAALAND = FirstRoundInfo(
        matches_won=9,
        matches_drawn=0,
        matches_lost=9,
        points_for=667,
        total=27,
        points_against=689,
    )
    LIGA_SABSEG_FTW = FirstRoundInfo(
        matches_won=8,
        matches_drawn=1,
        matches_lost=9,
        points_for=699,
        points_against=762,
        total=25,
    )
    PAULINHO_FC = FirstRoundInfo(
        matches_won=5,
        matches_drawn=0,
        matches_lost=13,
        points_for=755,
        points_against=898,
        total=15,
    )
    VOLTA_CRIS = FirstRoundInfo(
        matches_won=8,
        matches_drawn=1,
        matches_lost=9,
        points_for=699,
        points_against=763,
        total=25,
    )
    ZE_MAIA_GT_BINO = FirstRoundInfo(
        matches_won=9,
        matches_drawn=0,
        matches_lost=9,
        points_for=807,
        total=27,
        points_against=785,
    )


class Teams(ExtendedEnum):
    AL_NASSR = Team(
        manager_name="João Meneses",
        team_name="Al-Nassr",
        first_round_info=FirstRoundInfoTeams.AL_NASSR.value,
    )
    CHORA_BEBE = Team(
        manager_name="Miguel Meneses",
        team_name="Chora Bebé",
        first_round_info=FirstRoundInfoTeams.CHORA_BEBE.value,
    )
    DRAFT_V3 = Team(
        manager_name="Pedro Ribeiro",
        team_name="Draft v3",
        first_round_info=FirstRoundInfoTeams.DRAFT_V3.value,
    )
    GYO_GT_HAALAND = Team(
        manager_name="Nuno Ribeiro",
        team_name="Gyo>haaland",
        first_round_info=FirstRoundInfoTeams.GYO_GT_HAALAND.value,
    )
    LIGA_SABSEG_FTW = Team(
        manager_name="José Alves",
        team_name="Liga SabSeg FTW",
        first_round_info=FirstRoundInfoTeams.LIGA_SABSEG_FTW.value,
    )
    PAULINHO_FC = Team(
        manager_name="Pedro Gonçalves",
        team_name="Paulinho FC",
        first_round_info=FirstRoundInfoTeams.PAULINHO_FC.value,
    )
    VOLTA_CRIS = Team(
        manager_name="Diogo Gonçalves",
        team_name="Volta Cris",
        first_round_info=FirstRoundInfoTeams.VOLTA_CRIS.value,
    )
    ZE_MAIA_GT_BINO = Team(
        manager_name="José Maia",
        team_name="Zé Maia > Bino",
        first_round_info=FirstRoundInfoTeams.ZE_MAIA_GT_BINO.value,
    )
