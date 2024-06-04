# Generated by ariadne-codegen on 2024-06-04 12:20
# Source: graphql/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetNewsTicker(BaseModel):
    get_news_ticker: Optional["GetNewsTickerGetNewsTicker"] = Field(
        alias="getNewsTicker"
    )


class GetNewsTickerGetNewsTicker(BaseModel):
    content: Optional[str]


GetNewsTicker.update_forward_refs()
GetNewsTickerGetNewsTicker.update_forward_refs()
