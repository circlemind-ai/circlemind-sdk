"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .queryrequest import QueryRequest, QueryRequestTypedDict
from circlemind_sdk.types import BaseModel
from circlemind_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class PostQueryGraphGraphNameQueryPostRequestTypedDict(TypedDict):
    graph_name: str
    query_request: QueryRequestTypedDict


class PostQueryGraphGraphNameQueryPostRequest(BaseModel):
    graph_name: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    query_request: Annotated[
        QueryRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
