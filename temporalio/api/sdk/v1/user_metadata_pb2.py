# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/sdk/v1/user_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from temporalio.api.common.v1 import (
    message_pb2 as temporal_dot_api_dot_common_dot_v1_dot_message__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n'temporal/api/sdk/v1/user_metadata.proto\x12\x13temporal.api.sdk.v1\x1a$temporal/api/common/v1/message.proto\"r\n\x0cUserMetadata\x12\x30\n\x07summary\x18\x01 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload\x12\x30\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.PayloadB\x7f\n\x16io.temporal.api.sdk.v1B\x11UserMetadataProtoP\x01Z\x1dgo.temporal.io/api/sdk/v1;sdk\xaa\x02\x15Temporalio.Api.Sdk.V1\xea\x02\x18Temporalio::Api::Sdk::V1b\x06proto3"
)


_USERMETADATA = DESCRIPTOR.message_types_by_name["UserMetadata"]
UserMetadata = _reflection.GeneratedProtocolMessageType(
    "UserMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _USERMETADATA,
        "__module__": "temporal.api.sdk.v1.user_metadata_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.sdk.v1.UserMetadata)
    },
)
_sym_db.RegisterMessage(UserMetadata)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\026io.temporal.api.sdk.v1B\021UserMetadataProtoP\001Z\035go.temporal.io/api/sdk/v1;sdk\252\002\025Temporalio.Api.Sdk.V1\352\002\030Temporalio::Api::Sdk::V1"
    _USERMETADATA._serialized_start = 102
    _USERMETADATA._serialized_end = 216
# @@protoc_insertion_point(module_scope)
