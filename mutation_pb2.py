# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mutation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mutation.proto',
  package='io.spoud.sdm.logistics.service.mutation.v1',
  syntax='proto3',
  serialized_options=_b('\n*io.spoud.sdm.logistics.service.mutation.v1P\001Z\035logistics.service.mutation.v1'),
  serialized_pb=_b('\n\x0emutation.proto\x12*io.spoud.sdm.logistics.service.mutation.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"o\n\x0f\x41ttributeChange\x12M\n\x04type\x18\x01 \x01(\x0e\x32?.io.spoud.sdm.logistics.service.mutation.v1.AttributeChangeType\x12\r\n\x05value\x18\x03 \x01(\t\"\x80\x01\n\x13MetaAttributeChange\x12M\n\x04type\x18\x01 \x01(\x0e\x32?.io.spoud.sdm.logistics.service.mutation.v1.AttributeChangeType\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t*-\n\x13\x41ttributeChangeType\x12\n\n\x06UPDATE\x10\x00\x12\n\n\x06\x44\x45LETE\x10\x01*6\n\x0bStateChange\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tAVAILABLE\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\x42M\n*io.spoud.sdm.logistics.service.mutation.v1P\x01Z\x1dlogistics.service.mutation.v1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_ATTRIBUTECHANGETYPE = _descriptor.EnumDescriptor(
  name='AttributeChangeType',
  full_name='io.spoud.sdm.logistics.service.mutation.v1.AttributeChangeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=339,
  serialized_end=384,
)
_sym_db.RegisterEnumDescriptor(_ATTRIBUTECHANGETYPE)

AttributeChangeType = enum_type_wrapper.EnumTypeWrapper(_ATTRIBUTECHANGETYPE)
_STATECHANGE = _descriptor.EnumDescriptor(
  name='StateChange',
  full_name='io.spoud.sdm.logistics.service.mutation.v1.StateChange',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVAILABLE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=386,
  serialized_end=440,
)
_sym_db.RegisterEnumDescriptor(_STATECHANGE)

StateChange = enum_type_wrapper.EnumTypeWrapper(_STATECHANGE)
UPDATE = 0
DELETE = 1
UNKNOWN = 0
AVAILABLE = 1
DELETED = 2



_ATTRIBUTECHANGE = _descriptor.Descriptor(
  name='AttributeChange',
  full_name='io.spoud.sdm.logistics.service.mutation.v1.AttributeChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='io.spoud.sdm.logistics.service.mutation.v1.AttributeChange.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='io.spoud.sdm.logistics.service.mutation.v1.AttributeChange.value', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=206,
)


_METAATTRIBUTECHANGE = _descriptor.Descriptor(
  name='MetaAttributeChange',
  full_name='io.spoud.sdm.logistics.service.mutation.v1.MetaAttributeChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='io.spoud.sdm.logistics.service.mutation.v1.MetaAttributeChange.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='io.spoud.sdm.logistics.service.mutation.v1.MetaAttributeChange.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='io.spoud.sdm.logistics.service.mutation.v1.MetaAttributeChange.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=337,
)

_ATTRIBUTECHANGE.fields_by_name['type'].enum_type = _ATTRIBUTECHANGETYPE
_METAATTRIBUTECHANGE.fields_by_name['type'].enum_type = _ATTRIBUTECHANGETYPE
DESCRIPTOR.message_types_by_name['AttributeChange'] = _ATTRIBUTECHANGE
DESCRIPTOR.message_types_by_name['MetaAttributeChange'] = _METAATTRIBUTECHANGE
DESCRIPTOR.enum_types_by_name['AttributeChangeType'] = _ATTRIBUTECHANGETYPE
DESCRIPTOR.enum_types_by_name['StateChange'] = _STATECHANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AttributeChange = _reflection.GeneratedProtocolMessageType('AttributeChange', (_message.Message,), {
  'DESCRIPTOR' : _ATTRIBUTECHANGE,
  '__module__' : 'mutation_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.logistics.service.mutation.v1.AttributeChange)
  })
_sym_db.RegisterMessage(AttributeChange)

MetaAttributeChange = _reflection.GeneratedProtocolMessageType('MetaAttributeChange', (_message.Message,), {
  'DESCRIPTOR' : _METAATTRIBUTECHANGE,
  '__module__' : 'mutation_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.logistics.service.mutation.v1.MetaAttributeChange)
  })
_sym_db.RegisterMessage(MetaAttributeChange)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
