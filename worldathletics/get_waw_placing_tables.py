# Generated by ariadne-codegen on 2024-06-04 12:21
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetWawPlacingTables(BaseModel):
    get_waw_placing_tables: Optional[
        List[Optional["GetWawPlacingTablesGetWawPlacingTables"]]
    ] = Field(alias="getWawPlacingTables")


class GetWawPlacingTablesGetWawPlacingTables(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    event_id: Optional[int] = Field(alias="eventId")
    rank: Optional[int]
    country_name: Optional[str] = Field(alias="countryName")
    country_code: Optional[str] = Field(alias="countryCode")
    gold: Optional[int]
    silver: Optional[int]
    bronze: Optional[int]
    forth: Optional[int]
    fifth: Optional[int]
    sixth: Optional[int]
    seventh: Optional[int]
    eighth: Optional[int]
    points: Optional[int]
    table_order: Optional[int] = Field(alias="tableOrder")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")


GetWawPlacingTables.update_forward_refs()
GetWawPlacingTablesGetWawPlacingTables.update_forward_refs()
