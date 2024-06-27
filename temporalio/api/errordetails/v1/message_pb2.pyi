"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
These error details are supplied in google.rpc.Status#details as described in "Google APIs, Error Model" (https://cloud.google.com/apis/design/errors#error_model)
and extend standard Error Details defined in https://github.com/googleapis/googleapis/blob/master/google/rpc/error_details.proto
"""
import builtins
import collections.abc
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import temporalio.api.common.v1.message_pb2
import temporalio.api.enums.v1.failed_cause_pb2
import temporalio.api.enums.v1.namespace_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class NotFoundFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CURRENT_CLUSTER_FIELD_NUMBER: builtins.int
    ACTIVE_CLUSTER_FIELD_NUMBER: builtins.int
    current_cluster: builtins.str
    active_cluster: builtins.str
    def __init__(
        self,
        *,
        current_cluster: builtins.str = ...,
        active_cluster: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "active_cluster", b"active_cluster", "current_cluster", b"current_cluster"
        ],
    ) -> None: ...

global___NotFoundFailure = NotFoundFailure

class WorkflowExecutionAlreadyStartedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_REQUEST_ID_FIELD_NUMBER: builtins.int
    RUN_ID_FIELD_NUMBER: builtins.int
    start_request_id: builtins.str
    run_id: builtins.str
    def __init__(
        self,
        *,
        start_request_id: builtins.str = ...,
        run_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "run_id", b"run_id", "start_request_id", b"start_request_id"
        ],
    ) -> None: ...

global___WorkflowExecutionAlreadyStartedFailure = WorkflowExecutionAlreadyStartedFailure

class NamespaceNotActiveFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_FIELD_NUMBER: builtins.int
    CURRENT_CLUSTER_FIELD_NUMBER: builtins.int
    ACTIVE_CLUSTER_FIELD_NUMBER: builtins.int
    namespace: builtins.str
    current_cluster: builtins.str
    active_cluster: builtins.str
    def __init__(
        self,
        *,
        namespace: builtins.str = ...,
        current_cluster: builtins.str = ...,
        active_cluster: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "active_cluster",
            b"active_cluster",
            "current_cluster",
            b"current_cluster",
            "namespace",
            b"namespace",
        ],
    ) -> None: ...

global___NamespaceNotActiveFailure = NamespaceNotActiveFailure

class NamespaceInvalidStateFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    ALLOWED_STATES_FIELD_NUMBER: builtins.int
    namespace: builtins.str
    state: temporalio.api.enums.v1.namespace_pb2.NamespaceState.ValueType
    """Current state of the requested namespace."""
    @property
    def allowed_states(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        temporalio.api.enums.v1.namespace_pb2.NamespaceState.ValueType
    ]:
        """Allowed namespace states for requested operation.
        For example NAMESPACE_STATE_DELETED is forbidden for most operations but allowed for DescribeNamespace.
        """
    def __init__(
        self,
        *,
        namespace: builtins.str = ...,
        state: temporalio.api.enums.v1.namespace_pb2.NamespaceState.ValueType = ...,
        allowed_states: collections.abc.Iterable[
            temporalio.api.enums.v1.namespace_pb2.NamespaceState.ValueType
        ]
        | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "allowed_states",
            b"allowed_states",
            "namespace",
            b"namespace",
            "state",
            b"state",
        ],
    ) -> None: ...

global___NamespaceInvalidStateFailure = NamespaceInvalidStateFailure

class NamespaceNotFoundFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_FIELD_NUMBER: builtins.int
    namespace: builtins.str
    def __init__(
        self,
        *,
        namespace: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["namespace", b"namespace"]
    ) -> None: ...

global___NamespaceNotFoundFailure = NamespaceNotFoundFailure

class NamespaceAlreadyExistsFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___NamespaceAlreadyExistsFailure = NamespaceAlreadyExistsFailure

class ClientVersionNotSupportedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_VERSION_FIELD_NUMBER: builtins.int
    CLIENT_NAME_FIELD_NUMBER: builtins.int
    SUPPORTED_VERSIONS_FIELD_NUMBER: builtins.int
    client_version: builtins.str
    client_name: builtins.str
    supported_versions: builtins.str
    def __init__(
        self,
        *,
        client_version: builtins.str = ...,
        client_name: builtins.str = ...,
        supported_versions: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "client_name",
            b"client_name",
            "client_version",
            b"client_version",
            "supported_versions",
            b"supported_versions",
        ],
    ) -> None: ...

global___ClientVersionNotSupportedFailure = ClientVersionNotSupportedFailure

class ServerVersionNotSupportedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_VERSION_FIELD_NUMBER: builtins.int
    CLIENT_SUPPORTED_SERVER_VERSIONS_FIELD_NUMBER: builtins.int
    server_version: builtins.str
    client_supported_server_versions: builtins.str
    def __init__(
        self,
        *,
        server_version: builtins.str = ...,
        client_supported_server_versions: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "client_supported_server_versions",
            b"client_supported_server_versions",
            "server_version",
            b"server_version",
        ],
    ) -> None: ...

global___ServerVersionNotSupportedFailure = ServerVersionNotSupportedFailure

class CancellationAlreadyRequestedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CancellationAlreadyRequestedFailure = CancellationAlreadyRequestedFailure

class QueryFailedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryFailedFailure = QueryFailedFailure

class PermissionDeniedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REASON_FIELD_NUMBER: builtins.int
    reason: builtins.str
    def __init__(
        self,
        *,
        reason: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["reason", b"reason"]
    ) -> None: ...

global___PermissionDeniedFailure = PermissionDeniedFailure

class ResourceExhaustedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CAUSE_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    cause: temporalio.api.enums.v1.failed_cause_pb2.ResourceExhaustedCause.ValueType
    scope: temporalio.api.enums.v1.failed_cause_pb2.ResourceExhaustedScope.ValueType
    def __init__(
        self,
        *,
        cause: temporalio.api.enums.v1.failed_cause_pb2.ResourceExhaustedCause.ValueType = ...,
        scope: temporalio.api.enums.v1.failed_cause_pb2.ResourceExhaustedScope.ValueType = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["cause", b"cause", "scope", b"scope"],
    ) -> None: ...

global___ResourceExhaustedFailure = ResourceExhaustedFailure

class SystemWorkflowFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WORKFLOW_EXECUTION_FIELD_NUMBER: builtins.int
    WORKFLOW_ERROR_FIELD_NUMBER: builtins.int
    @property
    def workflow_execution(
        self,
    ) -> temporalio.api.common.v1.message_pb2.WorkflowExecution:
        """WorkflowId and RunId of the Temporal system workflow performing the underlying operation.
        Looking up the info of the system workflow run may help identify the issue causing the failure.
        """
    workflow_error: builtins.str
    """Serialized error returned by the system workflow performing the underlying operation."""
    def __init__(
        self,
        *,
        workflow_execution: temporalio.api.common.v1.message_pb2.WorkflowExecution
        | None = ...,
        workflow_error: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "workflow_execution", b"workflow_execution"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "workflow_error",
            b"workflow_error",
            "workflow_execution",
            b"workflow_execution",
        ],
    ) -> None: ...

global___SystemWorkflowFailure = SystemWorkflowFailure

class WorkflowNotReadyFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___WorkflowNotReadyFailure = WorkflowNotReadyFailure

class NewerBuildExistsFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEFAULT_BUILD_ID_FIELD_NUMBER: builtins.int
    default_build_id: builtins.str
    """The current default compatible build ID which will receive tasks"""
    def __init__(
        self,
        *,
        default_build_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["default_build_id", b"default_build_id"],
    ) -> None: ...

global___NewerBuildExistsFailure = NewerBuildExistsFailure

class MultiOperationExecutionFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class OperationStatus(google.protobuf.message.Message):
        """NOTE: `OperationStatus` is modelled after
        [`google.rpc.Status`](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto).

        (-- api-linter: core::0146::any=disabled
            aip.dev/not-precedent: details are meant to hold arbitrary payloads. --)
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CODE_FIELD_NUMBER: builtins.int
        MESSAGE_FIELD_NUMBER: builtins.int
        DETAILS_FIELD_NUMBER: builtins.int
        code: builtins.int
        message: builtins.str
        @property
        def details(
            self,
        ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
            google.protobuf.any_pb2.Any
        ]: ...
        def __init__(
            self,
            *,
            code: builtins.int = ...,
            message: builtins.str = ...,
            details: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "code", b"code", "details", b"details", "message", b"message"
            ],
        ) -> None: ...

    STATUSES_FIELD_NUMBER: builtins.int
    @property
    def statuses(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___MultiOperationExecutionFailure.OperationStatus
    ]:
        """One status for each requested operation from the failed MultiOperation. The failed
        operation(s) have the same error details as if it was executed separately. All other operations have the
        status code `Aborted` and `MultiOperationExecutionAborted` is added to the details field.
        """
    def __init__(
        self,
        *,
        statuses: collections.abc.Iterable[
            global___MultiOperationExecutionFailure.OperationStatus
        ]
        | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["statuses", b"statuses"]
    ) -> None: ...

global___MultiOperationExecutionFailure = MultiOperationExecutionFailure
