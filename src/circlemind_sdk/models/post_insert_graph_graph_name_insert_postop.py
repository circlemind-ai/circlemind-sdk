"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .insertrequest import InsertRequest, InsertRequestTypedDict
from circlemind_sdk.types import BaseModel
from circlemind_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class PostInsertGraphGraphNameInsertPostRequestTypedDict(TypedDict):
    graph_name: str
    insert_request: InsertRequestTypedDict


class PostInsertGraphGraphNameInsertPostRequest(BaseModel):
    graph_name: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    insert_request: Annotated[
        InsertRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
