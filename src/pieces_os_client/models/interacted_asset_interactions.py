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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, constr, validator

class InteractedAssetInteractions(BaseModel):
    """
    InteractedAssetInteractions
    """
    viewed: constr(strict=True) = Field(..., description="https://en.wikipedia.org/wiki/ISO_8601#Time_intervals")
    touched: Optional[StrictBool] = Field(False, description="If the user touched or panned over the asset.")
    scrolled: Optional[StrictBool] = Field(False, description="If the user scrolled over the asset.")
    __properties = ["viewed", "touched", "scrolled"]

    @validator('viewed')
    def viewed_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"P[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss]", value):
            raise ValueError(r"must validate the regular expression /P[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss]/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> InteractedAssetInteractions:
        """Create an instance of InteractedAssetInteractions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InteractedAssetInteractions:
        """Create an instance of InteractedAssetInteractions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InteractedAssetInteractions.parse_obj(obj)

        _obj = InteractedAssetInteractions.parse_obj({
            "viewed": obj.get("viewed"),
            "touched": obj.get("touched") if obj.get("touched") is not None else False,
            "scrolled": obj.get("scrolled") if obj.get("scrolled") is not None else False
        })
        return _obj

