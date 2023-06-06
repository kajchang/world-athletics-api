# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetEventTeamStandingDetails(BaseModel):
    get_event_team_standing_details: Optional[
        List[Optional["GetEventTeamStandingDetailsGetEventTeamStandingDetails"]]
    ] = Field(alias="getEventTeamStandingDetails")


class GetEventTeamStandingDetailsGetEventTeamStandingDetails(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    team_standings_id: Optional[int] = Field(alias="teamStandingsId")
    team_standing_detail_order: Optional[int] = Field(alias="teamStandingDetailOrder")
    event_id: Optional[int] = Field(alias="eventId")
    sex_code: Optional[str] = Field(alias="sexCode")
    sex_name: Optional[str] = Field(alias="sexName")
    rank: Optional[int]
    result_rank: Optional[int] = Field(alias="resultRank")
    result_mark: Optional[str] = Field(alias="resultMark")
    record: Optional[str]
    standing_points: Optional[int] = Field(alias="standingPoints")
    team_id: Optional[int] = Field(alias="teamId")
    team_name: Optional[str] = Field(alias="teamName")
    team_country_code: Optional[str] = Field(alias="teamCountryCode")
    standing_mark: Optional[int] = Field(alias="standingMark")
    competitor_id__w_a: Optional[int] = Field(alias="competitorId_WA")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    team_id__w_a: Optional[int] = Field(alias="teamId_WA")
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor: Optional[
        "GetEventTeamStandingDetailsGetEventTeamStandingDetailsCompetitor"
    ]
    discipline: Optional[
        "GetEventTeamStandingDetailsGetEventTeamStandingDetailsDiscipline"
    ]


class GetEventTeamStandingDetailsGetEventTeamStandingDetailsCompetitor(BaseModel):
    id: Optional[int] = Field(alias="_id")
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    type_code: Optional[str] = Field(alias="typeCode")
    first_name: Optional[str] = Field(alias="firstName")
    last_name: Optional[str] = Field(alias="lastName")
    information: Optional[str]
    sex_code: Optional[str] = Field(alias="sexCode")
    sex_name: Optional[str] = Field(alias="sexName")
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    birth_date: Optional[Any] = Field(alias="birthDate")
    birth_date_str: Optional[str] = Field(alias="birthDateStr")
    url_slug: Optional[str] = Field(alias="urlSlug")
    representative_type_code: Optional[str] = Field(alias="representativeTypeCode")
    representative_id: Optional[int] = Field(alias="representativeId")
    competitor_id__w_a: Optional[int] = Field(alias="competitorId_WA")
    name: Optional[str]
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")
    sex_name_url_slug: Optional[str] = Field(alias="sexNameUrlSlug")
    friendly_name: Optional[str] = Field(alias="friendlyName")
    friendly_name_letter: Optional[str] = Field(alias="friendlyNameLetter")
    friendly_name_first3_letter: Optional[str] = Field(alias="friendlyNameFirst3Letter")


class GetEventTeamStandingDetailsGetEventTeamStandingDetailsDiscipline(BaseModel):
    id: Optional[str] = Field(alias="_id")
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    name: Optional[str]
    type_code: Optional[str] = Field(alias="typeCode")
    type_name: Optional[str] = Field(alias="typeName")
    type_order: Optional[int] = Field(alias="typeOrder")
    order: Optional[int]
    is_track: Optional[bool] = Field(alias="isTrack")
    is_field: Optional[bool] = Field(alias="isField")
    is_road: Optional[bool] = Field(alias="isRoad")
    is_combined: Optional[bool] = Field(alias="isCombined")
    is_walk: Optional[bool] = Field(alias="isWalk")
    is_indoor: Optional[bool] = Field(alias="isIndoor")
    is_reaction: Optional[bool] = Field(alias="isReaction")
    is_outdoor: Optional[bool] = Field(alias="isOutdoor")
    is_wind: Optional[bool] = Field(alias="isWind")
    is_relay: Optional[bool] = Field(alias="isRelay")
    is_valid_i_a_a_f: Optional[bool] = Field(alias="isValidIAAF")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")


GetEventTeamStandingDetails.update_forward_refs()
GetEventTeamStandingDetailsGetEventTeamStandingDetails.update_forward_refs()
GetEventTeamStandingDetailsGetEventTeamStandingDetailsCompetitor.update_forward_refs()
GetEventTeamStandingDetailsGetEventTeamStandingDetailsDiscipline.update_forward_refs()