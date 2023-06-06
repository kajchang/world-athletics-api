# Generated by ariadne-codegen on 2023-06-06 10:50
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetResultInfo(BaseModel):
    get_result_info: Optional[List[Optional["GetResultInfoGetResultInfo"]]] = Field(
        alias="getResultInfo"
    )


class GetResultInfoGetResultInfo(BaseModel):
    id: Optional[str]
    title: Optional[str]
    file_name: Optional[str] = Field(alias="fileName")
    info_type: Optional[int] = Field(alias="infoType")
    event_id: Optional[int] = Field(alias="eventId")
    competition_id: Optional[str] = Field(alias="competitionId")


GetResultInfo.update_forward_refs()
GetResultInfoGetResultInfo.update_forward_refs()