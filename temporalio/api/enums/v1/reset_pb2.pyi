"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ResetReapplyType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ResetReapplyTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _ResetReapplyType.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RESET_REAPPLY_TYPE_UNSPECIFIED: _ResetReapplyType.ValueType  # 0
    RESET_REAPPLY_TYPE_SIGNAL: _ResetReapplyType.ValueType  # 1
    RESET_REAPPLY_TYPE_NONE: _ResetReapplyType.ValueType  # 2

class ResetReapplyType(_ResetReapplyType, metaclass=_ResetReapplyTypeEnumTypeWrapper):
    """TODO: What is this?"""

    pass

RESET_REAPPLY_TYPE_UNSPECIFIED: ResetReapplyType.ValueType  # 0
RESET_REAPPLY_TYPE_SIGNAL: ResetReapplyType.ValueType  # 1
RESET_REAPPLY_TYPE_NONE: ResetReapplyType.ValueType  # 2
global___ResetReapplyType = ResetReapplyType