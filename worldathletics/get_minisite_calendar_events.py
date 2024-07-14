# Generated by ariadne-codegen on 2024-07-13 19:17
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetMinisiteCalendarEvents(BaseModel):
    get_minisite_calendar_events: Optional[
        "GetMinisiteCalendarEventsGetMinisiteCalendarEvents"
    ] = Field(alias="getMinisiteCalendarEvents")


class GetMinisiteCalendarEventsGetMinisiteCalendarEvents(BaseModel):
    hits: Optional[int]
    default_offset: Optional[int] = Field(alias="defaultOffset")
    pagination_page: Optional[int] = Field(alias="paginationPage")
    parameters: Optional["GetMinisiteCalendarEventsGetMinisiteCalendarEventsParameters"]
    results: Optional[
        List[Optional["GetMinisiteCalendarEventsGetMinisiteCalendarEventsResults"]]
    ]
    options: Optional["GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptions"]


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsParameters(BaseModel):
    start_date: Optional[str] = Field(alias="startDate")
    end_date: Optional[str] = Field(alias="endDate")
    query: Optional[str]
    region_type: Optional[str] = Field(alias="regionType")
    region_id: Optional[int] = Field(alias="regionId")
    discipline_id: Optional[int] = Field(alias="disciplineId")
    ranking_category_id: Optional[int] = Field(alias="rankingCategoryId")
    permit_level_id: Optional[int] = Field(alias="permitLevelId")
    competition_group_id: Optional[int] = Field(alias="competitionGroupId")
    competition_subgroup_id: Optional[int] = Field(alias="competitionSubgroupId")
    limit: Optional[int]
    offset: Optional[int]
    show_options_with_no_hits: Optional[bool] = Field(alias="showOptionsWithNoHits")
    hide_competitions_with_no_results: Optional[bool] = Field(
        alias="hideCompetitionsWithNoResults"
    )
    season: Optional[str]


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsResults(BaseModel):
    id: Optional[int]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    has_results: Optional[bool] = Field(alias="hasResults")
    has_api_results: Optional[bool] = Field(alias="hasApiResults")
    has_startlist: Optional[bool] = Field(alias="hasStartlist")
    name: Optional[str]
    venue: Optional[str]
    area: Optional[str]
    country: Optional[str]
    ranking_category: Optional[str] = Field(alias="rankingCategory")
    disciplines: Optional[str]
    competition_group: Optional[str] = Field(alias="competitionGroup")
    competition_subgroup: Optional[str] = Field(alias="competitionSubgroup")
    start_date: Optional[str] = Field(alias="startDate")
    end_date: Optional[str] = Field(alias="endDate")
    date_range: Optional[str] = Field(alias="dateRange")
    season: Optional[str]
    was_url: Optional[str] = Field(alias="wasUrl")
    has_competition_information: Optional[bool] = Field(
        alias="hasCompetitionInformation"
    )
    undetermined_competition_period: Optional[
        "GetMinisiteCalendarEventsGetMinisiteCalendarEventsResultsUndeterminedCompetitionPeriod"
    ] = Field(alias="undeterminedCompetitionPeriod")


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsResultsUndeterminedCompetitionPeriod(
    BaseModel
):
    status: Optional[str]
    label: Optional[str]
    remark: Optional[str]


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptions(BaseModel):
    regions: Optional[
        "GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRegions"
    ]
    seasons: Optional[
        List[
            Optional["GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsSeasons"]
        ]
    ]
    disciplines: Optional[
        List[
            Optional[
                "GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsDisciplines"
            ]
        ]
    ]
    ranking_categories: Optional[
        List[
            Optional[
                "GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRankingCategories"
            ]
        ]
    ] = Field(alias="rankingCategories")
    permit_levels: Optional[
        List[
            Optional[
                "GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsPermitLevels"
            ]
        ]
    ] = Field(alias="permitLevels")
    competition_groups: Optional[
        List[
            Optional[
                "GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsCompetitionGroups"
            ]
        ]
    ] = Field(alias="competitionGroups")
    competition_subgroups: Optional[
        List[
            Optional[
                "GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsCompetitionSubgroups"
            ]
        ]
    ] = Field(alias="competitionSubgroups")


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRegions(BaseModel):
    world: Optional[
        List[
            Optional[
                "GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRegionsWorld"
            ]
        ]
    ]
    area: Optional[
        List[
            Optional[
                "GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRegionsArea"
            ]
        ]
    ]
    country: Optional[
        List[
            Optional[
                "GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRegionsCountry"
            ]
        ]
    ]


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRegionsWorld(BaseModel):
    id: Optional[int]
    name: Optional[str]
    count: Optional[int]


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRegionsArea(BaseModel):
    id: Optional[int]
    name: Optional[str]
    count: Optional[int]


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRegionsCountry(
    BaseModel
):
    id: Optional[int]
    name: Optional[str]
    count: Optional[int]


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsSeasons(BaseModel):
    id: Optional[str]
    name: Optional[str]


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsDisciplines(BaseModel):
    id: Optional[int]
    name: Optional[str]
    count: Optional[int]


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRankingCategories(
    BaseModel
):
    id: Optional[int]
    name: Optional[str]
    count: Optional[int]


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsPermitLevels(BaseModel):
    id: Optional[int]
    name: Optional[str]
    count: Optional[int]


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsCompetitionGroups(
    BaseModel
):
    id: Optional[int]
    name: Optional[str]
    count: Optional[int]


class GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsCompetitionSubgroups(
    BaseModel
):
    id: Optional[int]
    name: Optional[str]
    count: Optional[int]


GetMinisiteCalendarEvents.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEvents.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsParameters.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsResults.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsResultsUndeterminedCompetitionPeriod.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptions.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRegions.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRegionsWorld.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRegionsArea.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRegionsCountry.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsSeasons.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsDisciplines.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsRankingCategories.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsPermitLevels.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsCompetitionGroups.update_forward_refs()
GetMinisiteCalendarEventsGetMinisiteCalendarEventsOptionsCompetitionSubgroups.update_forward_refs()
