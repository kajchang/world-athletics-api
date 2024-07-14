# Generated by ariadne-codegen on 2024-07-13 19:17
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetUsersVotes(BaseModel):
    get_users_votes: Optional[List[Optional["GetUsersVotesGetUsersVotes"]]] = Field(
        alias="getUsersVotes"
    )


class GetUsersVotesGetUsersVotes(BaseModel):
    id: Optional[str]
    vote_id: Optional[str] = Field(alias="voteId")
    user_cognito_id: Optional[str] = Field(alias="userCognitoId")


GetUsersVotes.update_forward_refs()
GetUsersVotesGetUsersVotes.update_forward_refs()
