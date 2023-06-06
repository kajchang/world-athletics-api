# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetFlashInterviews(BaseModel):
    get_flash_interviews: Optional[
        List[Optional[List[Optional["GetFlashInterviewsGetFlashInterviews"]]]]
    ] = Field(alias="getFlashInterviews")


class GetFlashInterviewsGetFlashInterviews(BaseModel):
    discipline_name: Optional[str] = Field(alias="disciplineName")
    discipline_sex_name: Optional[str] = Field(alias="disciplineSexName")
    unit_type_name: Optional[str] = Field(alias="unitTypeName")
    unit_name: Optional[str] = Field(alias="unitName")
    phase_name: Optional[str] = Field(alias="phaseName")
    phase_id: Optional[int] = Field(alias="phaseId")
    unit_id: Optional[int] = Field(alias="unitId")
    interviews: Optional[
        List[Optional["GetFlashInterviewsGetFlashInterviewsInterviews"]]
    ]


class GetFlashInterviewsGetFlashInterviewsInterviews(BaseModel):
    id: Optional[int]
    phase_id: Optional[int] = Field(alias="phaseId")
    phase_date: Optional[Any] = Field(alias="phaseDate")
    phase_name: Optional[str] = Field(alias="phaseName")
    unit_id: Optional[int] = Field(alias="unitId")
    unit_code: Optional[int] = Field(alias="unitCode")
    unit_type_name: Optional[str] = Field(alias="unitTypeName")
    unit_name: Optional[str] = Field(alias="unitName")
    title: Optional[str]
    body: Optional[str]
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_team_name: Optional[str] = Field(alias="competitorTeamName")
    competitor_forename: Optional[str] = Field(alias="competitorForename")
    competitor_surname: Optional[str] = Field(alias="competitorSurname")
    competitor_country_code: Optional[str] = Field(alias="competitorCountryCode")
    competitor_sex: Optional[str] = Field(alias="competitorSex")
    competitor_type: Optional[str] = Field(alias="competitorType")
    updated_on: Optional[Any] = Field(alias="updatedOn")
    event_id: Optional[int] = Field(alias="eventId")
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name: Optional[str] = Field(alias="disciplineName")
    discipline_sex_name: Optional[str] = Field(alias="disciplineSexName")
    flash_interview_order: Optional[int] = Field(alias="flashInterviewOrder")
    flash_interview_date: Optional[Any] = Field(alias="flashInterviewDate")
    flash_interview_has_time: Optional[bool] = Field(alias="flashInterviewHasTime")
    event_store_id: Optional[str] = Field(alias="eventStoreId")
    is_approved: Optional[bool] = Field(alias="isApproved")


GetFlashInterviews.update_forward_refs()
GetFlashInterviewsGetFlashInterviews.update_forward_refs()
GetFlashInterviewsGetFlashInterviewsInterviews.update_forward_refs()