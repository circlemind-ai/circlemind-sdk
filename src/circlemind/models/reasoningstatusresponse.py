"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from circlemind.types import BaseModel
from typing_extensions import TypedDict


class ReasoningStatusResponseTypedDict(TypedDict):
    status: str
    memories: str
    context: str


class ReasoningStatusResponse(BaseModel):
    status: str

    memories: str

    context: str
