"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from circlemind_sdk.types import BaseModel
from typing_extensions import TypedDict


class ReasoningRequestTypedDict(TypedDict):
    query: str
    parameters: str


class ReasoningRequest(BaseModel):
    query: str
    parameters: str
