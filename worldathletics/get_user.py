# Generated by ariadne-codegen on 2024-07-13 19:16
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetUser(BaseModel):
    get_user: Optional["GetUserGetUser"] = Field(alias="getUser")


class GetUserGetUser(BaseModel):
    cognito_id: str = Field(alias="cognitoId")
    registration_date: Optional[str] = Field(alias="registrationDate")
    date_modified: Optional[str] = Field(alias="dateModified")
    name: Optional[str]
    settings: Optional["GetUserGetUserSettings"]


class GetUserGetUserSettings(BaseModel):
    first_name: Optional[str] = Field(alias="firstName")
    last_name: Optional[str] = Field(alias="lastName")
    email: Optional[str]
    age_group: Optional[str] = Field(alias="ageGroup")
    sex: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    national_team_support_country_code: Optional[str] = Field(
        alias="nationalTeamSupportCountryCode"
    )
    mailing_list_consent: Optional[bool] = Field(alias="mailingListConsent")
    global_tokyo_mailing_list_consent: Optional[bool] = Field(
        alias="globalTokyoMailingListConsent"
    )
    kids_athletics_terms_and_conditions: Optional[str] = Field(
        alias="kidsAthleticsTermsAndConditions"
    )
    user_types: Optional[List[Optional[str]]] = Field(alias="userTypes")
    user_sub_types: Optional[List[Optional[str]]] = Field(alias="userSubTypes")
    discipline_categories: Optional[List[Optional[str]]] = Field(
        alias="disciplineCategories"
    )
    interests: Optional[List[Optional[str]]]
    contact_preferences: Optional[List[Optional[str]]] = Field(
        alias="contactPreferences"
    )
    source: Optional[str]
    tags: Optional[List[Optional[str]]]
    followed_competitors: Optional[List[Optional[int]]] = Field(
        alias="followedCompetitors"
    )
    followed_countries: Optional[
        List[Optional["GetUserGetUserSettingsFollowedCountries"]]
    ] = Field(alias="followedCountries")
    nickname: Optional[str]
    locale: Optional[str]
    country_region_code: Optional[str] = Field(alias="countryRegionCode")


class GetUserGetUserSettingsFollowedCountries(BaseModel):
    competition: Optional[int]
    countries: Optional[List[Optional[str]]]


GetUser.update_forward_refs()
GetUserGetUser.update_forward_refs()
GetUserGetUserSettings.update_forward_refs()
GetUserGetUserSettingsFollowedCountries.update_forward_refs()
