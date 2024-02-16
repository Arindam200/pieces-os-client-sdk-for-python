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

from pydantic import BaseModel, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.score import Score
from pieces_os_client.models.website import Website
from typing import Optional, Set
from typing_extensions import Self

class Websites(BaseModel):
    """
    This is a specific model for related websites to an asset.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    iterable: List[Website]
    indices: Optional[Dict[str, StrictInt]] = Field(default=None, description="This is a Map<String, int> where the the key is an website id.")
    score: Optional[Score] = None
    __properties: ClassVar[List[str]] = ["schema", "iterable", "indices", "score"]

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
        """Create an instance of Websites from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in iterable (list)
        _items = []
        if self.iterable:
            for _item in self.iterable:
                if _item:
                    _items.append(_item.to_dict())
            _dict['iterable'] = _items
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Websites from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "iterable": [Website.from_dict(_item) for _item in obj["iterable"]] if obj.get("iterable") is not None else None,
            "indices": obj.get("indices"),
            "score": Score.from_dict(obj["score"]) if obj.get("score") is not None else None
        })
        return _obj


