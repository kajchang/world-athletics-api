# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class AirQualityDevices(BaseModel):
    air_quality_devices: Optional[
        List[Optional["AirQualityDevicesAirQualityDevices"]]
    ] = Field(alias="airQualityDevices")


class AirQualityDevicesAirQualityDevices(BaseModel):
    serial_number: Optional[str]
    tag: Optional[str]
    status: Optional[int]
    last_connection_ts: Optional[Any]
    location: Optional["AirQualityDevicesAirQualityDevicesLocation"]


class AirQualityDevicesAirQualityDevicesLocation(BaseModel):
    latitude: Optional[str]
    longitude: Optional[str]


AirQualityDevices.update_forward_refs()
AirQualityDevicesAirQualityDevices.update_forward_refs()
AirQualityDevicesAirQualityDevicesLocation.update_forward_refs()