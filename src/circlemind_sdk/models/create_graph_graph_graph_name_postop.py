"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .configurerequest import ConfigureRequest, ConfigureRequestTypedDict
from circlemind_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from circlemind_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from pydantic import model_serializer
from typing_extensions import Annotated, TypedDict


class CreateGraphGraphGraphNamePostRequestTypedDict(TypedDict):
    graph_name: Nullable[str]
    configure_request: ConfigureRequestTypedDict


class CreateGraphGraphGraphNamePostRequest(BaseModel):
    graph_name: Annotated[
        Nullable[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    configure_request: Annotated[
        ConfigureRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["graph_name"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m