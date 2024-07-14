# Generated by ariadne-codegen on 2024-07-13 19:16
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetAllTimeList(BaseModel):
    get_all_time_list: Optional["GetAllTimeListGetAllTimeList"] = Field(
        alias="getAllTimeList"
    )


class GetAllTimeListGetAllTimeList(BaseModel):
    page: Optional[int]
    pages: Optional[int]
    payload: Optional[List[Optional["GetAllTimeListGetAllTimeListPayload"]]]


class GetAllTimeListGetAllTimeListPayload(BaseModel):
    position: Optional[int]
    place: Optional[str]
    achiever_position: Optional[int] = Field(alias="achieverPosition")
    result: Optional[str]
    achiever: Optional[str]
    nationality: Optional[str]
    venue: Optional[str]
    date: Optional[str]
    result_score: Optional[int] = Field(alias="resultScore")


GetAllTimeList.update_forward_refs()
GetAllTimeListGetAllTimeList.update_forward_refs()
GetAllTimeListGetAllTimeListPayload.update_forward_refs()
