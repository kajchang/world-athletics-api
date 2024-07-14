# Generated by ariadne-codegen on 2024-07-13 19:16
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetAppearance(BaseModel):
    get_appearance: Optional["GetAppearanceGetAppearance"] = Field(
        alias="getAppearance"
    )


class GetAppearanceGetAppearance(BaseModel):
    id: Optional[str]
    name: Optional[str]
    logo_id: Optional[str] = Field(alias="logoId")
    logo: Optional["GetAppearanceGetAppearanceLogo"]
    logo_edited: Optional[str] = Field(alias="logoEdited")
    feature_image_id: Optional[str] = Field(alias="featureImageId")
    feature_image: Optional["GetAppearanceGetAppearanceFeatureImage"] = Field(
        alias="featureImage"
    )
    feature_image_edited: Optional[str] = Field(alias="featureImageEdited")
    theme: Optional[str]
    default_sponsor_ids: Optional[List[Optional[str]]] = Field(
        alias="defaultSponsorIds"
    )
    default_sponsors: Optional[
        List[Optional["GetAppearanceGetAppearanceDefaultSponsors"]]
    ] = Field(alias="defaultSponsors")
    sponsor_ids: Optional[List[Optional[str]]] = Field(alias="sponsorIds")
    sponsors: Optional[List[Optional["GetAppearanceGetAppearanceSponsors"]]]
    event_id: Optional[int] = Field(alias="eventId")
    primary_color: Optional[str] = Field(alias="primaryColor")
    secondary_color: Optional[str] = Field(alias="secondaryColor")
    tertiary_color: Optional[str] = Field(alias="tertiaryColor")
    additional_colours: Optional[List[Optional[str]]] = Field(alias="additionalColours")
    language_codes: Optional[List[Optional[str]]] = Field(alias="languageCodes")


class GetAppearanceGetAppearanceLogo(BaseModel):
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


class GetAppearanceGetAppearanceFeatureImage(BaseModel):
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


class GetAppearanceGetAppearanceDefaultSponsors(BaseModel):
    id: Optional[str]
    event_id: Optional[int] = Field(alias="eventId")
    type: Optional[str]
    name: Optional[str]
    url: Optional[str]
    logo_scale: Optional[str] = Field(alias="logoScale")
    light_bg_logo_id: Optional[str] = Field(alias="lightBgLogoId")
    light_bg_logo: Optional["GetAppearanceGetAppearanceDefaultSponsorsLightBgLogo"] = (
        Field(alias="lightBgLogo")
    )
    light_bg_logo_edited: Optional[str] = Field(alias="lightBgLogoEdited")
    dark_bg_logo_id: Optional[str] = Field(alias="darkBgLogoId")
    dark_bg_logo: Optional["GetAppearanceGetAppearanceDefaultSponsorsDarkBgLogo"] = (
        Field(alias="darkBgLogo")
    )
    dark_bg_logo_edited: Optional[str] = Field(alias="darkBgLogoEdited")


class GetAppearanceGetAppearanceDefaultSponsorsLightBgLogo(BaseModel):
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


class GetAppearanceGetAppearanceDefaultSponsorsDarkBgLogo(BaseModel):
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


class GetAppearanceGetAppearanceSponsors(BaseModel):
    id: Optional[str]
    event_id: Optional[int] = Field(alias="eventId")
    type: Optional[str]
    name: Optional[str]
    url: Optional[str]
    logo_scale: Optional[str] = Field(alias="logoScale")
    light_bg_logo_id: Optional[str] = Field(alias="lightBgLogoId")
    light_bg_logo: Optional["GetAppearanceGetAppearanceSponsorsLightBgLogo"] = Field(
        alias="lightBgLogo"
    )
    light_bg_logo_edited: Optional[str] = Field(alias="lightBgLogoEdited")
    dark_bg_logo_id: Optional[str] = Field(alias="darkBgLogoId")
    dark_bg_logo: Optional["GetAppearanceGetAppearanceSponsorsDarkBgLogo"] = Field(
        alias="darkBgLogo"
    )
    dark_bg_logo_edited: Optional[str] = Field(alias="darkBgLogoEdited")


class GetAppearanceGetAppearanceSponsorsLightBgLogo(BaseModel):
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


class GetAppearanceGetAppearanceSponsorsDarkBgLogo(BaseModel):
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


GetAppearance.update_forward_refs()
GetAppearanceGetAppearance.update_forward_refs()
GetAppearanceGetAppearanceLogo.update_forward_refs()
GetAppearanceGetAppearanceFeatureImage.update_forward_refs()
GetAppearanceGetAppearanceDefaultSponsors.update_forward_refs()
GetAppearanceGetAppearanceDefaultSponsorsLightBgLogo.update_forward_refs()
GetAppearanceGetAppearanceDefaultSponsorsDarkBgLogo.update_forward_refs()
GetAppearanceGetAppearanceSponsors.update_forward_refs()
GetAppearanceGetAppearanceSponsorsLightBgLogo.update_forward_refs()
GetAppearanceGetAppearanceSponsorsDarkBgLogo.update_forward_refs()
