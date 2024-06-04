# Generated by ariadne-codegen on 2024-06-04 12:20
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetRankingGroups(BaseModel):
    get_ranking_groups: Optional[List[Optional["GetRankingGroupsGetRankingGroups"]]] = (
        Field(alias="getRankingGroups")
    )


class GetRankingGroupsGetRankingGroups(BaseModel):
    event_group: Optional[str] = Field(alias="eventGroup")
    events: Optional[List[Optional["GetRankingGroupsGetRankingGroupsEvents"]]]


class GetRankingGroupsGetRankingGroupsEvents(BaseModel):
    name: Optional[str]
    display_name: Optional[str] = Field(alias="displayName")
    gender: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")


GetRankingGroups.update_forward_refs()
GetRankingGroupsGetRankingGroups.update_forward_refs()
GetRankingGroupsGetRankingGroupsEvents.update_forward_refs()
