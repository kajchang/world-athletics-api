# Generated by ariadne-codegen on 2024-07-13 19:17
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetRandomWorldRankingDiscipline(BaseModel):
    get_random_world_ranking_discipline: Optional[
        List[Optional["GetRandomWorldRankingDisciplineGetRandomWorldRankingDiscipline"]]
    ] = Field(alias="getRandomWorldRankingDiscipline")


class GetRandomWorldRankingDisciplineGetRandomWorldRankingDiscipline(BaseModel):
    name: Optional[str]
    display_name: Optional[str] = Field(alias="displayName")
    gender: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")
    rankings: Optional[
        List[
            Optional[
                "GetRandomWorldRankingDisciplineGetRandomWorldRankingDisciplineRankings"
            ]
        ]
    ]
    query: Optional[
        "GetRandomWorldRankingDisciplineGetRandomWorldRankingDisciplineQuery"
    ]


class GetRandomWorldRankingDisciplineGetRandomWorldRankingDisciplineRankings(BaseModel):
    id: int
    place: Optional[int]
    competitor_name: Optional[str] = Field(alias="competitorName")
    competitor_country_url_slug: Optional[str] = Field(alias="competitorCountryUrlSlug")
    competitor_url_slug: Optional[str] = Field(alias="competitorUrlSlug")
    competitor_birth_date: Optional[Any] = Field(alias="competitorBirthDate")
    country_code: Optional[str] = Field(alias="countryCode")
    ranking_score: Optional[int] = Field(alias="rankingScore")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")
    country_place: Optional[int] = Field(alias="countryPlace")
    previous_id: Optional[int] = Field(alias="previousId")
    previous_place: Optional[int] = Field(alias="previousPlace")
    previous_ranking_score: Optional[int] = Field(alias="previousRankingScore")


class GetRandomWorldRankingDisciplineGetRandomWorldRankingDisciplineQuery(BaseModel):
    limit: Optional[int]
    gender: Optional[str]
    event_group: Optional[str] = Field(alias="eventGroup")


GetRandomWorldRankingDiscipline.update_forward_refs()
GetRandomWorldRankingDisciplineGetRandomWorldRankingDiscipline.update_forward_refs()
GetRandomWorldRankingDisciplineGetRandomWorldRankingDisciplineRankings.update_forward_refs()
GetRandomWorldRankingDisciplineGetRandomWorldRankingDisciplineQuery.update_forward_refs()
