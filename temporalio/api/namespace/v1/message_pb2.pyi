"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
The MIT License

Copyright (c) 2020 Temporal Technologies Inc.  All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import temporalio.api.enums.v1.namespace_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class NamespaceInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class DataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    class Capabilities(google.protobuf.message.Message):
        """Namespace capability details. Should contain what features are enabled in a namespace."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        EAGER_WORKFLOW_START_FIELD_NUMBER: builtins.int
        SYNC_UPDATE_FIELD_NUMBER: builtins.int
        ASYNC_UPDATE_FIELD_NUMBER: builtins.int
        eager_workflow_start: builtins.bool
        """True if the namespace supports eager workflow start."""
        sync_update: builtins.bool
        """True if the namespace supports sync update"""
        async_update: builtins.bool
        """True if the namespace supports async update"""
        def __init__(
            self,
            *,
            eager_workflow_start: builtins.bool = ...,
            sync_update: builtins.bool = ...,
            async_update: builtins.bool = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "async_update",
                b"async_update",
                "eager_workflow_start",
                b"eager_workflow_start",
                "sync_update",
                b"sync_update",
            ],
        ) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    OWNER_EMAIL_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    CAPABILITIES_FIELD_NUMBER: builtins.int
    SUPPORTS_SCHEDULES_FIELD_NUMBER: builtins.int
    name: builtins.str
    state: temporalio.api.enums.v1.namespace_pb2.NamespaceState.ValueType
    description: builtins.str
    owner_email: builtins.str
    @property
    def data(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """A key-value map for any customized purpose."""
    id: builtins.str
    @property
    def capabilities(self) -> global___NamespaceInfo.Capabilities:
        """All capabilities the namespace supports."""
    supports_schedules: builtins.bool
    """Whether scheduled workflows are supported on this namespace. This is only needed
    temporarily while the feature is experimental, so we can give it a high tag.
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        state: temporalio.api.enums.v1.namespace_pb2.NamespaceState.ValueType = ...,
        description: builtins.str = ...,
        owner_email: builtins.str = ...,
        data: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        id: builtins.str = ...,
        capabilities: global___NamespaceInfo.Capabilities | None = ...,
        supports_schedules: builtins.bool = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["capabilities", b"capabilities"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "capabilities",
            b"capabilities",
            "data",
            b"data",
            "description",
            b"description",
            "id",
            b"id",
            "name",
            b"name",
            "owner_email",
            b"owner_email",
            "state",
            b"state",
            "supports_schedules",
            b"supports_schedules",
        ],
    ) -> None: ...

global___NamespaceInfo = NamespaceInfo

class NamespaceConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class CustomSearchAttributeAliasesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    WORKFLOW_EXECUTION_RETENTION_TTL_FIELD_NUMBER: builtins.int
    BAD_BINARIES_FIELD_NUMBER: builtins.int
    HISTORY_ARCHIVAL_STATE_FIELD_NUMBER: builtins.int
    HISTORY_ARCHIVAL_URI_FIELD_NUMBER: builtins.int
    VISIBILITY_ARCHIVAL_STATE_FIELD_NUMBER: builtins.int
    VISIBILITY_ARCHIVAL_URI_FIELD_NUMBER: builtins.int
    CUSTOM_SEARCH_ATTRIBUTE_ALIASES_FIELD_NUMBER: builtins.int
    @property
    def workflow_execution_retention_ttl(
        self,
    ) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def bad_binaries(self) -> global___BadBinaries: ...
    history_archival_state: temporalio.api.enums.v1.namespace_pb2.ArchivalState.ValueType
    """If unspecified (ARCHIVAL_STATE_UNSPECIFIED) then default server configuration is used."""
    history_archival_uri: builtins.str
    visibility_archival_state: temporalio.api.enums.v1.namespace_pb2.ArchivalState.ValueType
    """If unspecified (ARCHIVAL_STATE_UNSPECIFIED) then default server configuration is used."""
    visibility_archival_uri: builtins.str
    @property
    def custom_search_attribute_aliases(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Map from field name to alias."""
    def __init__(
        self,
        *,
        workflow_execution_retention_ttl: google.protobuf.duration_pb2.Duration
        | None = ...,
        bad_binaries: global___BadBinaries | None = ...,
        history_archival_state: temporalio.api.enums.v1.namespace_pb2.ArchivalState.ValueType = ...,
        history_archival_uri: builtins.str = ...,
        visibility_archival_state: temporalio.api.enums.v1.namespace_pb2.ArchivalState.ValueType = ...,
        visibility_archival_uri: builtins.str = ...,
        custom_search_attribute_aliases: collections.abc.Mapping[
            builtins.str, builtins.str
        ]
        | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "bad_binaries",
            b"bad_binaries",
            "workflow_execution_retention_ttl",
            b"workflow_execution_retention_ttl",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "bad_binaries",
            b"bad_binaries",
            "custom_search_attribute_aliases",
            b"custom_search_attribute_aliases",
            "history_archival_state",
            b"history_archival_state",
            "history_archival_uri",
            b"history_archival_uri",
            "visibility_archival_state",
            b"visibility_archival_state",
            "visibility_archival_uri",
            b"visibility_archival_uri",
            "workflow_execution_retention_ttl",
            b"workflow_execution_retention_ttl",
        ],
    ) -> None: ...

global___NamespaceConfig = NamespaceConfig

class BadBinaries(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class BinariesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___BadBinaryInfo: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___BadBinaryInfo | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    BINARIES_FIELD_NUMBER: builtins.int
    @property
    def binaries(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        builtins.str, global___BadBinaryInfo
    ]: ...
    def __init__(
        self,
        *,
        binaries: collections.abc.Mapping[builtins.str, global___BadBinaryInfo]
        | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["binaries", b"binaries"]
    ) -> None: ...

global___BadBinaries = BadBinaries

class BadBinaryInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REASON_FIELD_NUMBER: builtins.int
    OPERATOR_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    reason: builtins.str
    operator: builtins.str
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        reason: builtins.str = ...,
        operator: builtins.str = ...,
        create_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["create_time", b"create_time"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "create_time", b"create_time", "operator", b"operator", "reason", b"reason"
        ],
    ) -> None: ...

global___BadBinaryInfo = BadBinaryInfo

class UpdateNamespaceInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class DataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    DESCRIPTION_FIELD_NUMBER: builtins.int
    OWNER_EMAIL_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    description: builtins.str
    owner_email: builtins.str
    @property
    def data(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """A key-value map for any customized purpose.
        If data already exists on the namespace,
        this will merge with the existing key values.
        """
    state: temporalio.api.enums.v1.namespace_pb2.NamespaceState.ValueType
    """New namespace state, server will reject if transition is not allowed.
    Allowed transitions are:
     Registered -> [ Deleted | Deprecated | Handover ]
     Handover -> [ Registered ]
    Default is NAMESPACE_STATE_UNSPECIFIED which is do not change state.
    """
    def __init__(
        self,
        *,
        description: builtins.str = ...,
        owner_email: builtins.str = ...,
        data: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        state: temporalio.api.enums.v1.namespace_pb2.NamespaceState.ValueType = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "data",
            b"data",
            "description",
            b"description",
            "owner_email",
            b"owner_email",
            "state",
            b"state",
        ],
    ) -> None: ...

global___UpdateNamespaceInfo = UpdateNamespaceInfo

class NamespaceFilter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INCLUDE_DELETED_FIELD_NUMBER: builtins.int
    include_deleted: builtins.bool
    """By default namespaces in NAMESPACE_STATE_DELETED state are not included.
    Setting include_deleted to true will include deleted namespaces.
    Note: Namespace is in NAMESPACE_STATE_DELETED state when it was deleted from the system but associated data is not deleted yet.
    """
    def __init__(
        self,
        *,
        include_deleted: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["include_deleted", b"include_deleted"],
    ) -> None: ...

global___NamespaceFilter = NamespaceFilter
