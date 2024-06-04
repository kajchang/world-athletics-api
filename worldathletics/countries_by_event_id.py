# Generated by ariadne-codegen on 2024-06-04 12:21
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class CountriesByEventId(BaseModel):
    countries_by_event_id: Optional[
        List[Optional["CountriesByEventIdCountriesByEventId"]]
    ] = Field(alias="countriesByEventId")


class CountriesByEventIdCountriesByEventId(BaseModel):
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    id: Optional[str]
    country_name: Optional[str] = Field(alias="countryName")
    country_order: Optional[int] = Field(alias="countryOrder")
    area_code: Optional[str] = Field(alias="areaCode")
    area_name: Optional[str] = Field(alias="areaName")
    area_order: Optional[int] = Field(alias="areaOrder")
    is_valid: Optional[bool] = Field(alias="isValid")
    area_name_url_slug: Optional[str] = Field(alias="areaNameUrlSlug")
    country_name_url_slug: Optional[str] = Field(alias="countryNameUrlSlug")


CountriesByEventId.update_forward_refs()
CountriesByEventIdCountriesByEventId.update_forward_refs()
