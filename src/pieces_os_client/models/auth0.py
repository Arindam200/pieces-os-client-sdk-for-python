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
from pieces_os_client.models.auth0_identity import Auth0Identity
from pieces_os_client.models.auth0_redirects import Auth0Redirects
from pieces_os_client.models.auth0_user import Auth0User
from pieces_os_client.models.auth0_user_metadata import Auth0UserMetadata
from pieces_os_client.models.o_auth_group import OAuthGroup
from typing import Optional, Set
from typing_extensions import Self

class Auth0(BaseModel):
    """
    An object representing all of the properties that are available within a Auth0 PKCE Flow
    """ # noqa: E501
    identity: Optional[Auth0Identity] = None
    user: Optional[Auth0User] = None
    metadata: Optional[Auth0UserMetadata] = None
    domain: StrictStr = Field(description="The domain of your Auth 0 Service")
    client: StrictStr = Field(description="The Client ID for your Auth0 Service")
    audience: StrictStr = Field(description="The Server Audience of your Auth0 Service")
    redirects: Auth0Redirects
    o_auth: OAuthGroup = Field(alias="oAuth")
    namespace: Optional[StrictStr] = Field(default=None, description="An optional namespace parameter to add an additional namespace")
    __properties: ClassVar[List[str]] = ["identity", "user", "metadata", "domain", "client", "audience", "redirects", "oAuth", "namespace"]

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
        """Create an instance of Auth0 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redirects
        if self.redirects:
            _dict['redirects'] = self.redirects.to_dict()
        # override the default output from pydantic by calling `to_dict()` of o_auth
        if self.o_auth:
            _dict['oAuth'] = self.o_auth.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Auth0 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identity": Auth0Identity.from_dict(obj["identity"]) if obj.get("identity") is not None else None,
            "user": Auth0User.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "metadata": Auth0UserMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "domain": obj.get("domain"),
            "client": obj.get("client"),
            "audience": obj.get("audience"),
            "redirects": Auth0Redirects.from_dict(obj["redirects"]) if obj.get("redirects") is not None else None,
            "oAuth": OAuthGroup.from_dict(obj["oAuth"]) if obj.get("oAuth") is not None else None,
            "namespace": obj.get("namespace")
        })
        return _obj


