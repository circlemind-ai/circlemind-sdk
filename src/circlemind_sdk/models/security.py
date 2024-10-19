"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from circlemind_sdk.types import BaseModel
from circlemind_sdk.utils import FieldMetadata, SecurityMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SecurityTypedDict(TypedDict):
    api_key_header: NotRequired[str]


class Security(BaseModel):
    api_key_header: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="apiKey",
                sub_type="header",
                field_name="apiKey",
            )
        ),
    ] = None
