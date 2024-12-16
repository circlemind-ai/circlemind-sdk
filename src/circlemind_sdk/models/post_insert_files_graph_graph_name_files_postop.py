"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .body_post_insert_files_graph_graph_name_files_post import (
    BodyPostInsertFilesGraphGraphNameFilesPost,
    BodyPostInsertFilesGraphGraphNameFilesPostTypedDict,
)
from circlemind_sdk.types import BaseModel
from circlemind_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class PostInsertFilesGraphGraphNameFilesPostRequestTypedDict(TypedDict):
    graph_name: str
    body_post_insert_files_graph_graph_name_files_post: (
        BodyPostInsertFilesGraphGraphNameFilesPostTypedDict
    )


class PostInsertFilesGraphGraphNameFilesPostRequest(BaseModel):
    graph_name: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body_post_insert_files_graph_graph_name_files_post: Annotated[
        BodyPostInsertFilesGraphGraphNameFilesPost,
        FieldMetadata(request=RequestMetadata(media_type="multipart/form-data")),
    ]