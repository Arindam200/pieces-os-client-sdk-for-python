# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.annotation_type_enum import AnnotationTypeEnum
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.flattened_conversation_messages import FlattenedConversationMessages
from pieces_os_client.models.mechanism_enum import MechanismEnum
from typing import Optional, Set
from typing_extensions import Self

class SeededAnnotation(BaseModel):
    """
    This is the percursor to a fully referenced Annotation.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    mechanism: Optional[MechanismEnum] = None
    asset: Optional[StrictStr] = None
    person: Optional[StrictStr] = None
    type: AnnotationTypeEnum
    text: StrictStr = Field(description="This is the text of the annotation.")
    model: Optional[StrictStr] = None
    pseudo: Optional[StrictBool] = None
    favorited: Optional[StrictBool] = None
    anchor: Optional[StrictStr] = None
    conversation: Optional[StrictStr] = None
    messages: Optional[FlattenedConversationMessages] = None
    __properties: ClassVar[List[str]] = ["schema", "mechanism", "asset", "person", "type", "text", "model", "pseudo", "favorited", "anchor", "conversation", "messages"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SeededAnnotation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of messages
        if self.messages:
            _dict['messages'] = self.messages.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SeededAnnotation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "mechanism": obj.get("mechanism"),
            "asset": obj.get("asset"),
            "person": obj.get("person"),
            "type": obj.get("type"),
            "text": obj.get("text"),
            "model": obj.get("model"),
            "pseudo": obj.get("pseudo"),
            "favorited": obj.get("favorited"),
            "anchor": obj.get("anchor"),
            "conversation": obj.get("conversation"),
            "messages": FlattenedConversationMessages.from_dict(obj["messages"]) if obj.get("messages") is not None else None
        })
        return _obj


