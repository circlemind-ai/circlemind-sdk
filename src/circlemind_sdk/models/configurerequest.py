"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from circlemind_sdk.types import BaseModel
import pydantic
from typing import List
from typing_extensions import Annotated, TypedDict


class ConfigureRequestTypedDict(TypedDict):
    domain: str
    example_queries: str
    entity_types: List[str]


class ConfigureRequest(BaseModel):
    domain: str

    example_queries: Annotated[str, pydantic.Field(alias="exampleQueries")]

    entity_types: Annotated[List[str], pydantic.Field(alias="entityTypes")]
