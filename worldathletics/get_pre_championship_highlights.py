# Generated by ariadne-codegen on 2024-07-13 19:17
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetPreChampionshipHighlights(BaseModel):
    get_pre_championship_highlights: Optional[
        "GetPreChampionshipHighlightsGetPreChampionshipHighlights"
    ] = Field(alias="getPreChampionshipHighlights")


class GetPreChampionshipHighlightsGetPreChampionshipHighlights(BaseModel):
    events: Optional[
        List[Optional["GetPreChampionshipHighlightsGetPreChampionshipHighlightsEvents"]]
    ]


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEvents(BaseModel):
    discipline: Optional[str]
    ranking_leaders: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeaders"
            ]
        ]
    ] = Field(alias="rankingLeaders")
    reigning_champions: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampions"
            ]
        ]
    ] = Field(alias="reigningChampions")
    sex: Optional[str]
    world_leaders: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeaders"
            ]
        ]
    ] = Field(alias="worldLeaders")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeaders(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembersTeamMembersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembersTeamMembersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampions(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembersTeamMembersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembersTeamMembersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeaders(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembersTeamMembersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembersTeamMembersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


GetPreChampionshipHighlights.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlights.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEvents.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeaders.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembers.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembersTeamMembers.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembersTeamMembersTeamMembers.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampions.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembers.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembersTeamMembers.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembersTeamMembersTeamMembers.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeaders.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembers.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembersTeamMembers.update_forward_refs()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembersTeamMembersTeamMembers.update_forward_refs()
