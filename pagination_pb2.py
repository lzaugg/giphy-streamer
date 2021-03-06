# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pagination.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pagination.proto',
  package='io.spoud.sdm.common.pagination.v1',
  syntax='proto3',
  serialized_options=_b('\n!io.spoud.sdm.common.pagination.v1P\001Z\rpagination.v1'),
  serialized_pb=_b('\n\x10pagination.proto\x12!io.spoud.sdm.common.pagination.v1\"4\n\x0bPageRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\"%\n\nPageResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\tB4\n!io.spoud.sdm.common.pagination.v1P\x01Z\rpagination.v1b\x06proto3')
)




_PAGEREQUEST = _descriptor.Descriptor(
  name='PageRequest',
  full_name='io.spoud.sdm.common.pagination.v1.PageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='io.spoud.sdm.common.pagination.v1.PageRequest.page_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='io.spoud.sdm.common.pagination.v1.PageRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=55,
  serialized_end=107,
)


_PAGERESULT = _descriptor.Descriptor(
  name='PageResult',
  full_name='io.spoud.sdm.common.pagination.v1.PageResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='io.spoud.sdm.common.pagination.v1.PageResult.next_page_token', index=0,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=109,
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['PageRequest'] = _PAGEREQUEST
DESCRIPTOR.message_types_by_name['PageResult'] = _PAGERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PageRequest = _reflection.GeneratedProtocolMessageType('PageRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAGEREQUEST,
  '__module__' : 'pagination_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.common.pagination.v1.PageRequest)
  })
_sym_db.RegisterMessage(PageRequest)

PageResult = _reflection.GeneratedProtocolMessageType('PageResult', (_message.Message,), {
  'DESCRIPTOR' : _PAGERESULT,
  '__module__' : 'pagination_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.common.pagination.v1.PageResult)
  })
_sym_db.RegisterMessage(PageResult)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
