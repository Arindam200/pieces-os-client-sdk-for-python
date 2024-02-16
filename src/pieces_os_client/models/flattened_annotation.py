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
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.mechanism_enum import MechanismEnum
from pieces_os_client.models.referenced_model import ReferencedModel
from pieces_os_client.models.score import Score
from typing import Optional, Set
from typing_extensions import Self

class FlattenedAnnotation(BaseModel):
    """
    This is the flattened Version of the annotation, IMPORTANT: when referencing these, ONLY Take the UUID, do NOT polinate(ie w/ asset/person/model) the FlattenedAnnotation as it can create an infinite loop.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr
    created: GroupedTimestamp
    updated: GroupedTimestamp
    deleted: Optional[GroupedTimestamp] = None
    mechanism: Optional[MechanismEnum] = None
    asset: Optional[ReferencedAsset] = None
    person: Optional[ReferencedPerson] = None
    type: AnnotationTypeEnum
    text: StrictStr = Field(description="This is the text of the annotation.")
    model: Optional[ReferencedModel] = None
    pseudo: Optional[StrictBool] = None
    favorited: Optional[StrictBool] = None
    anchor: Optional[ReferencedAnchor] = None
    conversation: Optional[ReferencedConversation] = None
    score: Optional[Score] = None
    messages: Optional[FlattenedConversationMessages] = None
    __properties: ClassVar[List[str]] = ["schema", "id", "created", "updated", "deleted", "mechanism", "asset", "person", "type", "text", "model", "pseudo", "favorited", "anchor", "conversation", "score", "messages"]

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
        """Create an instance of FlattenedAnnotation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of person
        if self.person:
            _dict['person'] = self.person.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchor
        if self.anchor:
            _dict['anchor'] = self.anchor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation
        if self.conversation:
            _dict['conversation'] = self.conversation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        # override the default output from pydantic by calling `to_dict()` of messages
        if self.messages:
            _dict['messages'] = self.messages.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlattenedAnnotation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "created": GroupedTimestamp.from_dict(obj["created"]) if obj.get("created") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj["updated"]) if obj.get("updated") is not None else None,
            "deleted": GroupedTimestamp.from_dict(obj["deleted"]) if obj.get("deleted") is not None else None,
            "mechanism": obj.get("mechanism"),
            "asset": ReferencedAsset.from_dict(obj["asset"]) if obj.get("asset") is not None else None,
            "person": ReferencedPerson.from_dict(obj["person"]) if obj.get("person") is not None else None,
            "type": obj.get("type"),
            "text": obj.get("text"),
            "model": ReferencedModel.from_dict(obj["model"]) if obj.get("model") is not None else None,
            "pseudo": obj.get("pseudo"),
            "favorited": obj.get("favorited"),
            "anchor": ReferencedAnchor.from_dict(obj["anchor"]) if obj.get("anchor") is not None else None,
            "conversation": ReferencedConversation.from_dict(obj["conversation"]) if obj.get("conversation") is not None else None,
            "score": Score.from_dict(obj["score"]) if obj.get("score") is not None else None,
            "messages": FlattenedConversationMessages.from_dict(obj["messages"]) if obj.get("messages") is not None else None
        })
        return _obj

from pieces_os_client.models.flattened_conversation_messages import FlattenedConversationMessages
from pieces_os_client.models.referenced_anchor import ReferencedAnchor
from pieces_os_client.models.referenced_asset import ReferencedAsset
from pieces_os_client.models.referenced_conversation import ReferencedConversation
from pieces_os_client.models.referenced_person import ReferencedPerson
# TODO: Rewrite to not use raise_errors
FlattenedAnnotation.model_rebuild(raise_errors=False)

