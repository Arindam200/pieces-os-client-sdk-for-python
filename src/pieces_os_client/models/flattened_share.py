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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.access_enum import AccessEnum
from pieces_os_client.models.accessors import Accessors
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.flattened_distributions import FlattenedDistributions
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.score import Score
from typing import Optional, Set
from typing_extensions import Self

class FlattenedShare(BaseModel):
    """
    This is a dag safe version of the Share.  if user is undefined && access is public then we have an asset that is publicly available.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr = Field(description="This references the share it self.")
    asset: Optional[StrictStr] = Field(default=None, description="this is the asset id on the flattened share.")
    user: Optional[StrictStr] = Field(default=None, description="this is the uuid of the user that the share is created for.")
    link: StrictStr = Field(description="this is the prebuilt link.")
    access: AccessEnum
    accessors: Accessors
    created: GroupedTimestamp
    short: StrictStr = Field(description="This is a shortened version of our uuid.")
    name: Optional[StrictStr] = None
    assets: Optional[FlattenedAssets] = None
    distributions: Optional[FlattenedDistributions] = None
    score: Optional[Score] = None
    __properties: ClassVar[List[str]] = ["schema", "id", "asset", "user", "link", "access", "accessors", "created", "short", "name", "assets", "distributions", "score"]

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
        """Create an instance of FlattenedShare from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of accessors
        if self.accessors:
            _dict['accessors'] = self.accessors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of distributions
        if self.distributions:
            _dict['distributions'] = self.distributions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlattenedShare from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "asset": obj.get("asset"),
            "user": obj.get("user"),
            "link": obj.get("link"),
            "access": obj.get("access"),
            "accessors": Accessors.from_dict(obj["accessors"]) if obj.get("accessors") is not None else None,
            "created": GroupedTimestamp.from_dict(obj["created"]) if obj.get("created") is not None else None,
            "short": obj.get("short"),
            "name": obj.get("name"),
            "assets": FlattenedAssets.from_dict(obj["assets"]) if obj.get("assets") is not None else None,
            "distributions": FlattenedDistributions.from_dict(obj["distributions"]) if obj.get("distributions") is not None else None,
            "score": Score.from_dict(obj["score"]) if obj.get("score") is not None else None
        })
        return _obj

from pieces_os_client.models.flattened_assets import FlattenedAssets
# TODO: Rewrite to not use raise_errors
FlattenedShare.model_rebuild(raise_errors=False)

