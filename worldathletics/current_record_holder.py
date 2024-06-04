# Generated by ariadne-codegen on 2024-06-04 12:20
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class CurrentRecordHolder(BaseModel):
    current_record_holder: Optional[
        List[Optional["CurrentRecordHolderCurrentRecordHolder"]]
    ] = Field(alias="currentRecordHolder")


class CurrentRecordHolderCurrentRecordHolder(BaseModel):
    progression_list_id: Optional[int] = Field(alias="progressionListId")
    category: Optional[str]
    performance: Optional[str]
    equal: Optional[bool]
    pending: Optional[bool]
    set_indoor: Optional[bool] = Field(alias="setIndoor")
    women_only: Optional[bool] = Field(alias="womenOnly")
    mixed: Optional[bool]
    yard: Optional[bool]
    wind: Optional[str]
    competitor: Optional["CurrentRecordHolderCurrentRecordHolderCompetitor"]
    country: Optional[str]
    venue: Optional[str]
    date: Optional[str]
    legend: Optional[str]
    discipline: Optional[str]
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")


class CurrentRecordHolderCurrentRecordHolderCompetitor(BaseModel):
    name: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    url_slug: Optional[str] = Field(alias="urlSlug")
    birth_date: Optional[str] = Field(alias="birthDate")


CurrentRecordHolder.update_forward_refs()
CurrentRecordHolderCurrentRecordHolder.update_forward_refs()
CurrentRecordHolderCurrentRecordHolderCompetitor.update_forward_refs()
