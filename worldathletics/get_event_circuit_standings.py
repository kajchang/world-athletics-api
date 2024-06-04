# Generated by ariadne-codegen on 2024-06-04 12:21
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetEventCircuitStandings(BaseModel):
    get_event_circuit_standings: Optional[
        "GetEventCircuitStandingsGetEventCircuitStandings"
    ] = Field(alias="getEventCircuitStandings")


class GetEventCircuitStandingsGetEventCircuitStandings(BaseModel):
    circuit_name: Optional[str] = Field(alias="circuitName")
    parameters: Optional["GetEventCircuitStandingsGetEventCircuitStandingsParameters"]
    seasons: Optional[List[Optional[str]]]
    standings: Optional[
        List[Optional["GetEventCircuitStandingsGetEventCircuitStandingsStandings"]]
    ]


class GetEventCircuitStandingsGetEventCircuitStandingsParameters(BaseModel):
    gender: Optional[str]
    season: Optional[str]


class GetEventCircuitStandingsGetEventCircuitStandingsStandings(BaseModel):
    disciplines: Optional[str]
    entries: Optional[
        List[
            Optional["GetEventCircuitStandingsGetEventCircuitStandingsStandingsEntries"]
        ]
    ]


class GetEventCircuitStandingsGetEventCircuitStandingsStandingsEntries(BaseModel):
    athlete_id: Optional[int] = Field(alias="athleteId")
    athlete: Optional[str]
    country: Optional[str]
    rank: Optional[int]
    points: Optional[str]
    results: Optional[
        List[
            Optional[
                "GetEventCircuitStandingsGetEventCircuitStandingsStandingsEntriesResults"
            ]
        ]
    ]


class GetEventCircuitStandingsGetEventCircuitStandingsStandingsEntriesResults(
    BaseModel
):
    discipline: Optional[str]
    points: Optional[str]
    result: Optional[str]
    venue: Optional[str]
    place: Optional[int]
    date: Optional[str]
    details: Optional[str]


GetEventCircuitStandings.update_forward_refs()
GetEventCircuitStandingsGetEventCircuitStandings.update_forward_refs()
GetEventCircuitStandingsGetEventCircuitStandingsParameters.update_forward_refs()
GetEventCircuitStandingsGetEventCircuitStandingsStandings.update_forward_refs()
GetEventCircuitStandingsGetEventCircuitStandingsStandingsEntries.update_forward_refs()
GetEventCircuitStandingsGetEventCircuitStandingsStandingsEntriesResults.update_forward_refs()
