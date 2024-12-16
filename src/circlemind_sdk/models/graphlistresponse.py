"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from circlemind_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class GraphListResponseTypedDict(TypedDict):
    r"""Data model for graph list response."""

    graphs: List[str]
    r"""List of existing graphs"""


class GraphListResponse(BaseModel):
    r"""Data model for graph list response."""

    graphs: List[str]
    r"""List of existing graphs"""
