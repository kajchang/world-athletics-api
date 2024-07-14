# Generated by ariadne-codegen on 2024-07-13 19:16
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetEvent(BaseModel):
    get_event: Optional["GetEventGetEvent"] = Field(alias="getEvent")


class GetEventGetEvent(BaseModel):
    id: Optional[str]
    media_ids: Optional[List[Optional[int]]] = Field(alias="mediaIds")
    related_media: Optional[List[Optional["GetEventGetEventRelatedMedia"]]] = Field(
        alias="relatedMedia"
    )
    timezone: Optional[str]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    name: Optional[str]
    start_date: Optional[Any] = Field(alias="startDate")
    end_date: Optional[Any] = Field(alias="endDate")
    venue: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    area_code: Optional[str] = Field(alias="areaCode")
    area_name: Optional[str] = Field(alias="areaName")
    age_code: Optional[str] = Field(alias="ageCode")
    indoor_outdoor: Optional[str] = Field(alias="indoorOutdoor")
    category_code: Optional[str] = Field(alias="categoryCode")
    category_name: Optional[str] = Field(alias="categoryName")
    category_order: Optional[int] = Field(alias="categoryOrder")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")
    sub_category_name: Optional[str] = Field(alias="subCategoryName")
    sub_category_order: Optional[int] = Field(alias="subCategoryOrder")
    show_web_live_banner: Optional[bool] = Field(alias="showWebLiveBanner")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    class_code: Optional[str] = Field(alias="classCode")
    class_name: Optional[str] = Field(alias="className")
    class_order: Optional[int] = Field(alias="classOrder")
    is_published: Optional[bool] = Field(alias="isPublished")
    has_comp_doc_results: Optional[bool] = Field(alias="hasCompDocResults")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    start_date_year: Optional[int] = Field(alias="startDateYear")
    circuits: Optional[List[Optional["GetEventGetEventCircuits"]]]
    area_name_url_slug: Optional[str] = Field(alias="areaNameUrlSlug")
    category_name_url_slug: Optional[str] = Field(alias="categoryNameUrlSlug")
    sub_category_name_url_slug: Optional[str] = Field(alias="subCategoryNameUrlSlug")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")


class GetEventGetEventRelatedMedia(BaseModel):
    id: Optional[str]
    media_type: Optional[str] = Field(alias="mediaType")
    title: Optional[str]
    copyright: Optional[str]
    file_name: Optional[str] = Field(alias="fileName")
    related_athletes: Optional[List[Optional[int]]] = Field(alias="relatedAthletes")
    related_disciplines: Optional[List[Optional[str]]] = Field(
        alias="relatedDisciplines"
    )
    related_competitions: Optional[List[Optional[str]]] = Field(
        alias="relatedCompetitions"
    )
    related_events: Optional[List[Optional[int]]] = Field(alias="relatedEvents")
    is_deleted: Optional[bool] = Field(alias="isDeleted")
    live_from: Optional[Any] = Field(alias="liveFrom")


class GetEventGetEventCircuits(BaseModel):
    updated_on: Optional[Any] = Field(alias="UpdatedOn")
    hash: Optional[str]
    circuit_code: Optional[str] = Field(alias="circuitCode")
    circuit_type_code: Optional[str] = Field(alias="circuitTypeCode")
    circuit_name: Optional[str] = Field(alias="circuitName")
    season: Optional[int]
    circuit_order: Optional[int] = Field(alias="circuitOrder")
    circuit_type_name: Optional[str] = Field(alias="circuitTypeName")


GetEvent.update_forward_refs()
GetEventGetEvent.update_forward_refs()
GetEventGetEventRelatedMedia.update_forward_refs()
GetEventGetEventCircuits.update_forward_refs()
