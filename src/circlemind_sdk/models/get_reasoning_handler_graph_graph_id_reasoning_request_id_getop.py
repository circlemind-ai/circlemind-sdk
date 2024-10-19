"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from circlemind_sdk.types import BaseModel
from circlemind_sdk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class GetReasoningHandlerGraphGraphIDReasoningRequestIDGetRequestTypedDict(TypedDict):
    graph_id: str
    request_id: str
    request_time: int


class GetReasoningHandlerGraphGraphIDReasoningRequestIDGetRequest(BaseModel):
    graph_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_time: Annotated[
        int,
        pydantic.Field(alias="requestTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]