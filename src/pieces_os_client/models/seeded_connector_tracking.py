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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.seeded_tracked_adoption_event import SeededTrackedAdoptionEvent
from pieces_os_client.models.seeded_tracked_interaction_event import SeededTrackedInteractionEvent
from pieces_os_client.models.seeded_tracked_keyboard_event import SeededTrackedKeyboardEvent
from pieces_os_client.models.seeded_tracked_machine_learning_event import SeededTrackedMachineLearningEvent
from pieces_os_client.models.seeded_tracked_session_event import SeededTrackedSessionEvent
from typing import Optional, Set
from typing_extensions import Self

class SeededConnectorTracking(BaseModel):
    """
    This model is designed to be light weight and low friction while most of the heavy lifting will be happening inside of the context servers.  This Model is important because this has references to our materials, instead of fully referenced materials.(very similar to our SeededTrackedEvent, consider consolidating and converting these to Referenced models instead of ID's)
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    format: Optional[SeededTrackedFormatEvent] = None
    asset: Optional[SeededTrackedAssetEvent] = None
    interaction: Optional[SeededTrackedInteractionEvent] = None
    keyboard: Optional[SeededTrackedKeyboardEvent] = None
    session: Optional[SeededTrackedSessionEvent] = None
    assets: Optional[SeededTrackedAssetsEvent] = None
    ml: Optional[SeededTrackedMachineLearningEvent] = None
    adoption: Optional[SeededTrackedAdoptionEvent] = None
    conversation: Optional[SeededTrackedConversationEvent] = None
    __properties: ClassVar[List[str]] = ["schema", "format", "asset", "interaction", "keyboard", "session", "assets", "ml", "adoption", "conversation"]

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
        """Create an instance of SeededConnectorTracking from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of format
        if self.format:
            _dict['format'] = self.format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interaction
        if self.interaction:
            _dict['interaction'] = self.interaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyboard
        if self.keyboard:
            _dict['keyboard'] = self.keyboard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of session
        if self.session:
            _dict['session'] = self.session.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ml
        if self.ml:
            _dict['ml'] = self.ml.to_dict()
        # override the default output from pydantic by calling `to_dict()` of adoption
        if self.adoption:
            _dict['adoption'] = self.adoption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation
        if self.conversation:
            _dict['conversation'] = self.conversation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SeededConnectorTracking from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "format": SeededTrackedFormatEvent.from_dict(obj["format"]) if obj.get("format") is not None else None,
            "asset": SeededTrackedAssetEvent.from_dict(obj["asset"]) if obj.get("asset") is not None else None,
            "interaction": SeededTrackedInteractionEvent.from_dict(obj["interaction"]) if obj.get("interaction") is not None else None,
            "keyboard": SeededTrackedKeyboardEvent.from_dict(obj["keyboard"]) if obj.get("keyboard") is not None else None,
            "session": SeededTrackedSessionEvent.from_dict(obj["session"]) if obj.get("session") is not None else None,
            "assets": SeededTrackedAssetsEvent.from_dict(obj["assets"]) if obj.get("assets") is not None else None,
            "ml": SeededTrackedMachineLearningEvent.from_dict(obj["ml"]) if obj.get("ml") is not None else None,
            "adoption": SeededTrackedAdoptionEvent.from_dict(obj["adoption"]) if obj.get("adoption") is not None else None,
            "conversation": SeededTrackedConversationEvent.from_dict(obj["conversation"]) if obj.get("conversation") is not None else None
        })
        return _obj

from pieces_os_client.models.seeded_tracked_asset_event import SeededTrackedAssetEvent
from pieces_os_client.models.seeded_tracked_assets_event import SeededTrackedAssetsEvent
from pieces_os_client.models.seeded_tracked_conversation_event import SeededTrackedConversationEvent
from pieces_os_client.models.seeded_tracked_format_event import SeededTrackedFormatEvent
# TODO: Rewrite to not use raise_errors
SeededConnectorTracking.model_rebuild(raise_errors=False)

