"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from circlemind_sdk.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class ReasoningResponseTypedDict(TypedDict):
    request_id: str
    request_time: int


class ReasoningResponse(BaseModel):
    request_id: Annotated[str, pydantic.Field(alias="requestId")]

    request_time: Annotated[int, pydantic.Field(alias="requestTime")]
