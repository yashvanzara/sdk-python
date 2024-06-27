# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/nexus/v1/message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from temporalio.api.common.v1 import (
    message_pb2 as temporal_dot_api_dot_common_dot_v1_dot_message__pb2,
)
from temporalio.api.sdk.v1 import (
    user_metadata_pb2 as temporal_dot_api_dot_sdk_dot_v1_dot_user__metadata__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#temporal/api/nexus/v1/message.proto\x12\x15temporal.api.nexus.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a$temporal/api/common/v1/message.proto\x1a\'temporal/api/sdk/v1/user_metadata.proto"\x9c\x01\n\x07\x46\x61ilure\x12\x0f\n\x07message\x18\x01 \x01(\t\x12>\n\x08metadata\x18\x02 \x03(\x0b\x32,.temporal.api.nexus.v1.Failure.MetadataEntry\x12\x0f\n\x07\x64\x65tails\x18\x03 \x01(\x0c\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"S\n\x0cHandlerError\x12\x12\n\nerror_type\x18\x01 \x01(\t\x12/\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32\x1e.temporal.api.nexus.v1.Failure"f\n\x1aUnsuccessfulOperationError\x12\x17\n\x0foperation_state\x18\x01 \x01(\t\x12/\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32\x1e.temporal.api.nexus.v1.Failure"\xa5\x02\n\x15StartOperationRequest\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x12\n\nrequest_id\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61llback\x18\x04 \x01(\t\x12\x30\n\x07payload\x18\x05 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload\x12Y\n\x0f\x63\x61llback_header\x18\x06 \x03(\x0b\x32@.temporal.api.nexus.v1.StartOperationRequest.CallbackHeaderEntry\x1a\x35\n\x13\x43\x61llbackHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"R\n\x16\x43\x61ncelOperationRequest\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x14\n\x0coperation_id\x18\x03 \x01(\t"\xc7\x02\n\x07Request\x12:\n\x06header\x18\x01 \x03(\x0b\x32*.temporal.api.nexus.v1.Request.HeaderEntry\x12\x32\n\x0escheduled_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12G\n\x0fstart_operation\x18\x03 \x01(\x0b\x32,.temporal.api.nexus.v1.StartOperationRequestH\x00\x12I\n\x10\x63\x61ncel_operation\x18\x04 \x01(\x0b\x32-.temporal.api.nexus.v1.CancelOperationRequestH\x00\x1a-\n\x0bHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\t\n\x07variant"\xe4\x02\n\x16StartOperationResponse\x12J\n\x0csync_success\x18\x01 \x01(\x0b\x32\x32.temporal.api.nexus.v1.StartOperationResponse.SyncH\x00\x12L\n\rasync_success\x18\x02 \x01(\x0b\x32\x33.temporal.api.nexus.v1.StartOperationResponse.AsyncH\x00\x12L\n\x0foperation_error\x18\x03 \x01(\x0b\x32\x31.temporal.api.nexus.v1.UnsuccessfulOperationErrorH\x00\x1a\x38\n\x04Sync\x12\x30\n\x07payload\x18\x01 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload\x1a\x1d\n\x05\x41sync\x12\x14\n\x0coperation_id\x18\x01 \x01(\tB\t\n\x07variant"\x19\n\x17\x43\x61ncelOperationResponse"\xab\x01\n\x08Response\x12H\n\x0fstart_operation\x18\x01 \x01(\x0b\x32-.temporal.api.nexus.v1.StartOperationResponseH\x00\x12J\n\x10\x63\x61ncel_operation\x18\x02 \x01(\x0b\x32..temporal.api.nexus.v1.CancelOperationResponseH\x00\x42\t\n\x07variant"\xd8\x01\n\x08\x45ndpoint\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12\n\n\x02id\x18\x02 \x01(\t\x12\x31\n\x04spec\x18\x03 \x01(\x0b\x32#.temporal.api.nexus.v1.EndpointSpec\x12\x30\n\x0c\x63reated_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x12last_modified_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nurl_prefix\x18\x06 \x01(\t"\x88\x01\n\x0c\x45ndpointSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x33\n\x08metadata\x18\x02 \x01(\x0b\x32!.temporal.api.sdk.v1.UserMetadata\x12\x35\n\x06target\x18\x03 \x01(\x0b\x32%.temporal.api.nexus.v1.EndpointTarget"\xe9\x01\n\x0e\x45ndpointTarget\x12>\n\x06worker\x18\x01 \x01(\x0b\x32,.temporal.api.nexus.v1.EndpointTarget.WorkerH\x00\x12\x42\n\x08\x65xternal\x18\x02 \x01(\x0b\x32..temporal.api.nexus.v1.EndpointTarget.ExternalH\x00\x1a/\n\x06Worker\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x12\n\ntask_queue\x18\x02 \x01(\t\x1a\x17\n\x08\x45xternal\x12\x0b\n\x03url\x18\x01 \x01(\tB\t\n\x07variantB\x84\x01\n\x18io.temporal.api.nexus.v1B\x0cMessageProtoP\x01Z!go.temporal.io/api/nexus/v1;nexus\xaa\x02\x17Temporalio.Api.Nexus.V1\xea\x02\x1aTemporalio::Api::Nexus::V1b\x06proto3'
)


_FAILURE = DESCRIPTOR.message_types_by_name["Failure"]
_FAILURE_METADATAENTRY = _FAILURE.nested_types_by_name["MetadataEntry"]
_HANDLERERROR = DESCRIPTOR.message_types_by_name["HandlerError"]
_UNSUCCESSFULOPERATIONERROR = DESCRIPTOR.message_types_by_name[
    "UnsuccessfulOperationError"
]
_STARTOPERATIONREQUEST = DESCRIPTOR.message_types_by_name["StartOperationRequest"]
_STARTOPERATIONREQUEST_CALLBACKHEADERENTRY = (
    _STARTOPERATIONREQUEST.nested_types_by_name["CallbackHeaderEntry"]
)
_CANCELOPERATIONREQUEST = DESCRIPTOR.message_types_by_name["CancelOperationRequest"]
_REQUEST = DESCRIPTOR.message_types_by_name["Request"]
_REQUEST_HEADERENTRY = _REQUEST.nested_types_by_name["HeaderEntry"]
_STARTOPERATIONRESPONSE = DESCRIPTOR.message_types_by_name["StartOperationResponse"]
_STARTOPERATIONRESPONSE_SYNC = _STARTOPERATIONRESPONSE.nested_types_by_name["Sync"]
_STARTOPERATIONRESPONSE_ASYNC = _STARTOPERATIONRESPONSE.nested_types_by_name["Async"]
_CANCELOPERATIONRESPONSE = DESCRIPTOR.message_types_by_name["CancelOperationResponse"]
_RESPONSE = DESCRIPTOR.message_types_by_name["Response"]
_ENDPOINT = DESCRIPTOR.message_types_by_name["Endpoint"]
_ENDPOINTSPEC = DESCRIPTOR.message_types_by_name["EndpointSpec"]
_ENDPOINTTARGET = DESCRIPTOR.message_types_by_name["EndpointTarget"]
_ENDPOINTTARGET_WORKER = _ENDPOINTTARGET.nested_types_by_name["Worker"]
_ENDPOINTTARGET_EXTERNAL = _ENDPOINTTARGET.nested_types_by_name["External"]
Failure = _reflection.GeneratedProtocolMessageType(
    "Failure",
    (_message.Message,),
    {
        "MetadataEntry": _reflection.GeneratedProtocolMessageType(
            "MetadataEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _FAILURE_METADATAENTRY,
                "__module__": "temporal.api.nexus.v1.message_pb2"
                # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.Failure.MetadataEntry)
            },
        ),
        "DESCRIPTOR": _FAILURE,
        "__module__": "temporal.api.nexus.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.Failure)
    },
)
_sym_db.RegisterMessage(Failure)
_sym_db.RegisterMessage(Failure.MetadataEntry)

HandlerError = _reflection.GeneratedProtocolMessageType(
    "HandlerError",
    (_message.Message,),
    {
        "DESCRIPTOR": _HANDLERERROR,
        "__module__": "temporal.api.nexus.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.HandlerError)
    },
)
_sym_db.RegisterMessage(HandlerError)

UnsuccessfulOperationError = _reflection.GeneratedProtocolMessageType(
    "UnsuccessfulOperationError",
    (_message.Message,),
    {
        "DESCRIPTOR": _UNSUCCESSFULOPERATIONERROR,
        "__module__": "temporal.api.nexus.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.UnsuccessfulOperationError)
    },
)
_sym_db.RegisterMessage(UnsuccessfulOperationError)

StartOperationRequest = _reflection.GeneratedProtocolMessageType(
    "StartOperationRequest",
    (_message.Message,),
    {
        "CallbackHeaderEntry": _reflection.GeneratedProtocolMessageType(
            "CallbackHeaderEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _STARTOPERATIONREQUEST_CALLBACKHEADERENTRY,
                "__module__": "temporal.api.nexus.v1.message_pb2"
                # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.StartOperationRequest.CallbackHeaderEntry)
            },
        ),
        "DESCRIPTOR": _STARTOPERATIONREQUEST,
        "__module__": "temporal.api.nexus.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.StartOperationRequest)
    },
)
_sym_db.RegisterMessage(StartOperationRequest)
_sym_db.RegisterMessage(StartOperationRequest.CallbackHeaderEntry)

CancelOperationRequest = _reflection.GeneratedProtocolMessageType(
    "CancelOperationRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELOPERATIONREQUEST,
        "__module__": "temporal.api.nexus.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.CancelOperationRequest)
    },
)
_sym_db.RegisterMessage(CancelOperationRequest)

Request = _reflection.GeneratedProtocolMessageType(
    "Request",
    (_message.Message,),
    {
        "HeaderEntry": _reflection.GeneratedProtocolMessageType(
            "HeaderEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _REQUEST_HEADERENTRY,
                "__module__": "temporal.api.nexus.v1.message_pb2"
                # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.Request.HeaderEntry)
            },
        ),
        "DESCRIPTOR": _REQUEST,
        "__module__": "temporal.api.nexus.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.Request)
    },
)
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.HeaderEntry)

StartOperationResponse = _reflection.GeneratedProtocolMessageType(
    "StartOperationResponse",
    (_message.Message,),
    {
        "Sync": _reflection.GeneratedProtocolMessageType(
            "Sync",
            (_message.Message,),
            {
                "DESCRIPTOR": _STARTOPERATIONRESPONSE_SYNC,
                "__module__": "temporal.api.nexus.v1.message_pb2"
                # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.StartOperationResponse.Sync)
            },
        ),
        "Async": _reflection.GeneratedProtocolMessageType(
            "Async",
            (_message.Message,),
            {
                "DESCRIPTOR": _STARTOPERATIONRESPONSE_ASYNC,
                "__module__": "temporal.api.nexus.v1.message_pb2"
                # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.StartOperationResponse.Async)
            },
        ),
        "DESCRIPTOR": _STARTOPERATIONRESPONSE,
        "__module__": "temporal.api.nexus.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.StartOperationResponse)
    },
)
_sym_db.RegisterMessage(StartOperationResponse)
_sym_db.RegisterMessage(StartOperationResponse.Sync)
_sym_db.RegisterMessage(StartOperationResponse.Async)

CancelOperationResponse = _reflection.GeneratedProtocolMessageType(
    "CancelOperationResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELOPERATIONRESPONSE,
        "__module__": "temporal.api.nexus.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.CancelOperationResponse)
    },
)
_sym_db.RegisterMessage(CancelOperationResponse)

Response = _reflection.GeneratedProtocolMessageType(
    "Response",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESPONSE,
        "__module__": "temporal.api.nexus.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.Response)
    },
)
_sym_db.RegisterMessage(Response)

Endpoint = _reflection.GeneratedProtocolMessageType(
    "Endpoint",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENDPOINT,
        "__module__": "temporal.api.nexus.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.Endpoint)
    },
)
_sym_db.RegisterMessage(Endpoint)

EndpointSpec = _reflection.GeneratedProtocolMessageType(
    "EndpointSpec",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENDPOINTSPEC,
        "__module__": "temporal.api.nexus.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.EndpointSpec)
    },
)
_sym_db.RegisterMessage(EndpointSpec)

EndpointTarget = _reflection.GeneratedProtocolMessageType(
    "EndpointTarget",
    (_message.Message,),
    {
        "Worker": _reflection.GeneratedProtocolMessageType(
            "Worker",
            (_message.Message,),
            {
                "DESCRIPTOR": _ENDPOINTTARGET_WORKER,
                "__module__": "temporal.api.nexus.v1.message_pb2"
                # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.EndpointTarget.Worker)
            },
        ),
        "External": _reflection.GeneratedProtocolMessageType(
            "External",
            (_message.Message,),
            {
                "DESCRIPTOR": _ENDPOINTTARGET_EXTERNAL,
                "__module__": "temporal.api.nexus.v1.message_pb2"
                # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.EndpointTarget.External)
            },
        ),
        "DESCRIPTOR": _ENDPOINTTARGET,
        "__module__": "temporal.api.nexus.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.nexus.v1.EndpointTarget)
    },
)
_sym_db.RegisterMessage(EndpointTarget)
_sym_db.RegisterMessage(EndpointTarget.Worker)
_sym_db.RegisterMessage(EndpointTarget.External)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\030io.temporal.api.nexus.v1B\014MessageProtoP\001Z!go.temporal.io/api/nexus/v1;nexus\252\002\027Temporalio.Api.Nexus.V1\352\002\032Temporalio::Api::Nexus::V1"
    _FAILURE_METADATAENTRY._options = None
    _FAILURE_METADATAENTRY._serialized_options = b"8\001"
    _STARTOPERATIONREQUEST_CALLBACKHEADERENTRY._options = None
    _STARTOPERATIONREQUEST_CALLBACKHEADERENTRY._serialized_options = b"8\001"
    _REQUEST_HEADERENTRY._options = None
    _REQUEST_HEADERENTRY._serialized_options = b"8\001"
    _FAILURE._serialized_start = 175
    _FAILURE._serialized_end = 331
    _FAILURE_METADATAENTRY._serialized_start = 284
    _FAILURE_METADATAENTRY._serialized_end = 331
    _HANDLERERROR._serialized_start = 333
    _HANDLERERROR._serialized_end = 416
    _UNSUCCESSFULOPERATIONERROR._serialized_start = 418
    _UNSUCCESSFULOPERATIONERROR._serialized_end = 520
    _STARTOPERATIONREQUEST._serialized_start = 523
    _STARTOPERATIONREQUEST._serialized_end = 816
    _STARTOPERATIONREQUEST_CALLBACKHEADERENTRY._serialized_start = 763
    _STARTOPERATIONREQUEST_CALLBACKHEADERENTRY._serialized_end = 816
    _CANCELOPERATIONREQUEST._serialized_start = 818
    _CANCELOPERATIONREQUEST._serialized_end = 900
    _REQUEST._serialized_start = 903
    _REQUEST._serialized_end = 1230
    _REQUEST_HEADERENTRY._serialized_start = 1174
    _REQUEST_HEADERENTRY._serialized_end = 1219
    _STARTOPERATIONRESPONSE._serialized_start = 1233
    _STARTOPERATIONRESPONSE._serialized_end = 1589
    _STARTOPERATIONRESPONSE_SYNC._serialized_start = 1491
    _STARTOPERATIONRESPONSE_SYNC._serialized_end = 1547
    _STARTOPERATIONRESPONSE_ASYNC._serialized_start = 1549
    _STARTOPERATIONRESPONSE_ASYNC._serialized_end = 1578
    _CANCELOPERATIONRESPONSE._serialized_start = 1591
    _CANCELOPERATIONRESPONSE._serialized_end = 1616
    _RESPONSE._serialized_start = 1619
    _RESPONSE._serialized_end = 1790
    _ENDPOINT._serialized_start = 1793
    _ENDPOINT._serialized_end = 2009
    _ENDPOINTSPEC._serialized_start = 2012
    _ENDPOINTSPEC._serialized_end = 2148
    _ENDPOINTTARGET._serialized_start = 2151
    _ENDPOINTTARGET._serialized_end = 2384
    _ENDPOINTTARGET_WORKER._serialized_start = 2301
    _ENDPOINTTARGET_WORKER._serialized_end = 2348
    _ENDPOINTTARGET_EXTERNAL._serialized_start = 2350
    _ENDPOINTTARGET_EXTERNAL._serialized_end = 2373
# @@protoc_insertion_point(module_scope)
