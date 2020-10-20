# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hook.proto

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
import logistics_pb2 as logistics__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hook.proto',
  package='io.spoud.sdm.logistics.hooks.v1alpha',
  syntax='proto3',
  serialized_options=_b('\n$io.spoud.sdm.logistics.hooks.v1alphaP\001Z\027logistics.hooks.v1alpha'),
  serialized_pb=_b('\n\nhook.proto\x12$io.spoud.sdm.logistics.hooks.v1alpha\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0flogistics.proto\"\xba\x01\n\x16SubscribeChangeRequest\x12V\n\x0estart_position\x18\x01 \x01(\x0b\x32>.io.spoud.sdm.logistics.hooks.v1alpha.StateChangeStartPosition\x12H\n\x07\x66ilters\x18\x02 \x03(\x0b\x32\x37.io.spoud.sdm.logistics.hooks.v1alpha.StateChangeFilter\"\x97\x04\n\x17SubscribeChangeResponse\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12G\n\x06\x61\x63tion\x18\x03 \x01(\x0e\x32\x37.io.spoud.sdm.logistics.hooks.v1alpha.StateChangeAction\x12\x45\n\x0b\x65ntity_type\x18\x04 \x01(\x0e\x32\x30.io.spoud.sdm.logistics.hooks.v1alpha.EntityType\x12:\n\ndata_offer\x18\n \x01(\x0b\x32$.io.spoud.sdm.logistics.v1.DataOfferH\x00\x12\x45\n\x10\x64\x61ta_offer_state\x18\x0c \x01(\x0b\x32).io.spoud.sdm.logistics.v1.DataOfferStateH\x00\x12H\n\x11\x64\x61ta_subscription\x18\r \x01(\x0b\x32+.io.spoud.sdm.logistics.v1.DataSubscriptionH\x00\x12S\n\x17\x64\x61ta_subscription_state\x18\x0e \x01(\x0b\x32\x30.io.spoud.sdm.logistics.v1.DataSubscriptionStateH\x00\x42\x08\n\x06\x65ntity\"q\n\x0f\x44\x61taOfferFilter\x12\n\n\x02id\x18\x01 \x01(\t\x12R\n\x12properties_filters\x18\x02 \x03(\x0b\x32\x36.io.spoud.sdm.logistics.hooks.v1alpha.PropertiesFilter\"v\n\x14\x44\x61taOfferStateFilter\x12\n\n\x02id\x18\x01 \x01(\t\x12R\n\x12properties_filters\x18\x03 \x03(\x0b\x32\x36.io.spoud.sdm.logistics.hooks.v1alpha.PropertiesFilter\"\x8f\x01\n\x16\x44\x61taSubscriptionFilter\x12\n\n\x02id\x18\x01 \x01(\t\x12R\n\x12properties_filters\x18\x02 \x03(\x0b\x32\x36.io.spoud.sdm.logistics.hooks.v1alpha.PropertiesFilter\x12\x15\n\rdata_offer_id\x18\x03 \x01(\t\"}\n\x1b\x44\x61taSubscriptionStateFilter\x12\n\n\x02id\x18\x01 \x01(\t\x12R\n\x12properties_filters\x18\x02 \x03(\x0b\x32\x36.io.spoud.sdm.logistics.hooks.v1alpha.PropertiesFilter\".\n\x10PropertiesFilter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x9f\x03\n\x11StateChangeFilter\x12R\n\x11\x64\x61ta_offer_filter\x18\x01 \x01(\x0b\x32\x35.io.spoud.sdm.logistics.hooks.v1alpha.DataOfferFilterH\x00\x12]\n\x17\x64\x61ta_offer_state_filter\x18\x02 \x01(\x0b\x32:.io.spoud.sdm.logistics.hooks.v1alpha.DataOfferStateFilterH\x00\x12`\n\x18\x64\x61ta_subscription_filter\x18\x03 \x01(\x0b\x32<.io.spoud.sdm.logistics.hooks.v1alpha.DataSubscriptionFilterH\x00\x12k\n\x1e\x64\x61ta_subscription_state_filter\x18\x04 \x01(\x0b\x32\x41.io.spoud.sdm.logistics.hooks.v1alpha.DataSubscriptionStateFilterH\x00\x42\x08\n\x06\x66ilter\"n\n\x18StateChangeStartPosition\x12\x46\n\x06preset\x18\x01 \x01(\x0e\x32\x34.io.spoud.sdm.logistics.hooks.v1alpha.PositionPresetH\x00\x42\n\n\x08position**\n\x0ePositionPreset\x12\x0c\n\x08\x45\x41RLIEST\x10\x00\x12\n\n\x06LATEST\x10\x01*-\n\x11StateChangeAction\x12\x0b\n\x07UPDATED\x10\x00\x12\x0b\n\x07\x44\x45LETED\x10\x01*s\n\nEntityType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nDATA_OFFER\x10\x01\x12\x14\n\x10\x44\x41TA_OFFER_STATE\x10\x02\x12\x15\n\x11\x44\x41TA_SUBSCRIPTION\x10\x03\x12\x1b\n\x17\x44\x41TA_SUBSCRIPTION_STATE\x10\x04\x32\xa1\x01\n\x0cStateChanger\x12\x90\x01\n\x0fSubscribeChange\x12<.io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeRequest\x1a=.io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeResponse0\x01\x42\x41\n$io.spoud.sdm.logistics.hooks.v1alphaP\x01Z\x17logistics.hooks.v1alphab\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,logistics__pb2.DESCRIPTOR,])

_POSITIONPRESET = _descriptor.EnumDescriptor(
  name='PositionPreset',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.PositionPreset',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EARLIEST', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LATEST', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1915,
  serialized_end=1957,
)
_sym_db.RegisterEnumDescriptor(_POSITIONPRESET)

PositionPreset = enum_type_wrapper.EnumTypeWrapper(_POSITIONPRESET)
_STATECHANGEACTION = _descriptor.EnumDescriptor(
  name='StateChangeAction',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.StateChangeAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UPDATED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1959,
  serialized_end=2004,
)
_sym_db.RegisterEnumDescriptor(_STATECHANGEACTION)

StateChangeAction = enum_type_wrapper.EnumTypeWrapper(_STATECHANGEACTION)
_ENTITYTYPE = _descriptor.EnumDescriptor(
  name='EntityType',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.EntityType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_OFFER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_OFFER_STATE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_SUBSCRIPTION', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_SUBSCRIPTION_STATE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2006,
  serialized_end=2121,
)
_sym_db.RegisterEnumDescriptor(_ENTITYTYPE)

EntityType = enum_type_wrapper.EnumTypeWrapper(_ENTITYTYPE)
EARLIEST = 0
LATEST = 1
UPDATED = 0
DELETED = 1
UNKNOWN = 0
DATA_OFFER = 1
DATA_OFFER_STATE = 2
DATA_SUBSCRIPTION = 3
DATA_SUBSCRIPTION_STATE = 4



_SUBSCRIBECHANGEREQUEST = _descriptor.Descriptor(
  name='SubscribeChangeRequest',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_position', full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeRequest.start_position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeRequest.filters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=103,
  serialized_end=289,
)


_SUBSCRIBECHANGERESPONSE = _descriptor.Descriptor(
  name='SubscribeChangeResponse',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeResponse.entity_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeResponse.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeResponse.action', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity_type', full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeResponse.entity_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_offer', full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeResponse.data_offer', index=4,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_offer_state', full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeResponse.data_offer_state', index=5,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_subscription', full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeResponse.data_subscription', index=6,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_subscription_state', full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeResponse.data_subscription_state', index=7,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='entity', full_name='io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeResponse.entity',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=292,
  serialized_end=827,
)


_DATAOFFERFILTER = _descriptor.Descriptor(
  name='DataOfferFilter',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataOfferFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataOfferFilter.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties_filters', full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataOfferFilter.properties_filters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=829,
  serialized_end=942,
)


_DATAOFFERSTATEFILTER = _descriptor.Descriptor(
  name='DataOfferStateFilter',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataOfferStateFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataOfferStateFilter.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties_filters', full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataOfferStateFilter.properties_filters', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=944,
  serialized_end=1062,
)


_DATASUBSCRIPTIONFILTER = _descriptor.Descriptor(
  name='DataSubscriptionFilter',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataSubscriptionFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataSubscriptionFilter.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties_filters', full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataSubscriptionFilter.properties_filters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_offer_id', full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataSubscriptionFilter.data_offer_id', index=2,
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
  serialized_start=1065,
  serialized_end=1208,
)


_DATASUBSCRIPTIONSTATEFILTER = _descriptor.Descriptor(
  name='DataSubscriptionStateFilter',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataSubscriptionStateFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataSubscriptionStateFilter.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties_filters', full_name='io.spoud.sdm.logistics.hooks.v1alpha.DataSubscriptionStateFilter.properties_filters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1210,
  serialized_end=1335,
)


_PROPERTIESFILTER = _descriptor.Descriptor(
  name='PropertiesFilter',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.PropertiesFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='io.spoud.sdm.logistics.hooks.v1alpha.PropertiesFilter.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='io.spoud.sdm.logistics.hooks.v1alpha.PropertiesFilter.value', index=1,
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
  serialized_start=1337,
  serialized_end=1383,
)


_STATECHANGEFILTER = _descriptor.Descriptor(
  name='StateChangeFilter',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.StateChangeFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_offer_filter', full_name='io.spoud.sdm.logistics.hooks.v1alpha.StateChangeFilter.data_offer_filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_offer_state_filter', full_name='io.spoud.sdm.logistics.hooks.v1alpha.StateChangeFilter.data_offer_state_filter', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_subscription_filter', full_name='io.spoud.sdm.logistics.hooks.v1alpha.StateChangeFilter.data_subscription_filter', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_subscription_state_filter', full_name='io.spoud.sdm.logistics.hooks.v1alpha.StateChangeFilter.data_subscription_state_filter', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='filter', full_name='io.spoud.sdm.logistics.hooks.v1alpha.StateChangeFilter.filter',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1386,
  serialized_end=1801,
)


_STATECHANGESTARTPOSITION = _descriptor.Descriptor(
  name='StateChangeStartPosition',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.StateChangeStartPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='preset', full_name='io.spoud.sdm.logistics.hooks.v1alpha.StateChangeStartPosition.preset', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='position', full_name='io.spoud.sdm.logistics.hooks.v1alpha.StateChangeStartPosition.position',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1803,
  serialized_end=1913,
)

_SUBSCRIBECHANGEREQUEST.fields_by_name['start_position'].message_type = _STATECHANGESTARTPOSITION
_SUBSCRIBECHANGEREQUEST.fields_by_name['filters'].message_type = _STATECHANGEFILTER
_SUBSCRIBECHANGERESPONSE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SUBSCRIBECHANGERESPONSE.fields_by_name['action'].enum_type = _STATECHANGEACTION
_SUBSCRIBECHANGERESPONSE.fields_by_name['entity_type'].enum_type = _ENTITYTYPE
_SUBSCRIBECHANGERESPONSE.fields_by_name['data_offer'].message_type = logistics__pb2._DATAOFFER
_SUBSCRIBECHANGERESPONSE.fields_by_name['data_offer_state'].message_type = logistics__pb2._DATAOFFERSTATE
_SUBSCRIBECHANGERESPONSE.fields_by_name['data_subscription'].message_type = logistics__pb2._DATASUBSCRIPTION
_SUBSCRIBECHANGERESPONSE.fields_by_name['data_subscription_state'].message_type = logistics__pb2._DATASUBSCRIPTIONSTATE
_SUBSCRIBECHANGERESPONSE.oneofs_by_name['entity'].fields.append(
  _SUBSCRIBECHANGERESPONSE.fields_by_name['data_offer'])
_SUBSCRIBECHANGERESPONSE.fields_by_name['data_offer'].containing_oneof = _SUBSCRIBECHANGERESPONSE.oneofs_by_name['entity']
_SUBSCRIBECHANGERESPONSE.oneofs_by_name['entity'].fields.append(
  _SUBSCRIBECHANGERESPONSE.fields_by_name['data_offer_state'])
_SUBSCRIBECHANGERESPONSE.fields_by_name['data_offer_state'].containing_oneof = _SUBSCRIBECHANGERESPONSE.oneofs_by_name['entity']
_SUBSCRIBECHANGERESPONSE.oneofs_by_name['entity'].fields.append(
  _SUBSCRIBECHANGERESPONSE.fields_by_name['data_subscription'])
_SUBSCRIBECHANGERESPONSE.fields_by_name['data_subscription'].containing_oneof = _SUBSCRIBECHANGERESPONSE.oneofs_by_name['entity']
_SUBSCRIBECHANGERESPONSE.oneofs_by_name['entity'].fields.append(
  _SUBSCRIBECHANGERESPONSE.fields_by_name['data_subscription_state'])
_SUBSCRIBECHANGERESPONSE.fields_by_name['data_subscription_state'].containing_oneof = _SUBSCRIBECHANGERESPONSE.oneofs_by_name['entity']
_DATAOFFERFILTER.fields_by_name['properties_filters'].message_type = _PROPERTIESFILTER
_DATAOFFERSTATEFILTER.fields_by_name['properties_filters'].message_type = _PROPERTIESFILTER
_DATASUBSCRIPTIONFILTER.fields_by_name['properties_filters'].message_type = _PROPERTIESFILTER
_DATASUBSCRIPTIONSTATEFILTER.fields_by_name['properties_filters'].message_type = _PROPERTIESFILTER
_STATECHANGEFILTER.fields_by_name['data_offer_filter'].message_type = _DATAOFFERFILTER
_STATECHANGEFILTER.fields_by_name['data_offer_state_filter'].message_type = _DATAOFFERSTATEFILTER
_STATECHANGEFILTER.fields_by_name['data_subscription_filter'].message_type = _DATASUBSCRIPTIONFILTER
_STATECHANGEFILTER.fields_by_name['data_subscription_state_filter'].message_type = _DATASUBSCRIPTIONSTATEFILTER
_STATECHANGEFILTER.oneofs_by_name['filter'].fields.append(
  _STATECHANGEFILTER.fields_by_name['data_offer_filter'])
_STATECHANGEFILTER.fields_by_name['data_offer_filter'].containing_oneof = _STATECHANGEFILTER.oneofs_by_name['filter']
_STATECHANGEFILTER.oneofs_by_name['filter'].fields.append(
  _STATECHANGEFILTER.fields_by_name['data_offer_state_filter'])
_STATECHANGEFILTER.fields_by_name['data_offer_state_filter'].containing_oneof = _STATECHANGEFILTER.oneofs_by_name['filter']
_STATECHANGEFILTER.oneofs_by_name['filter'].fields.append(
  _STATECHANGEFILTER.fields_by_name['data_subscription_filter'])
_STATECHANGEFILTER.fields_by_name['data_subscription_filter'].containing_oneof = _STATECHANGEFILTER.oneofs_by_name['filter']
_STATECHANGEFILTER.oneofs_by_name['filter'].fields.append(
  _STATECHANGEFILTER.fields_by_name['data_subscription_state_filter'])
_STATECHANGEFILTER.fields_by_name['data_subscription_state_filter'].containing_oneof = _STATECHANGEFILTER.oneofs_by_name['filter']
_STATECHANGESTARTPOSITION.fields_by_name['preset'].enum_type = _POSITIONPRESET
_STATECHANGESTARTPOSITION.oneofs_by_name['position'].fields.append(
  _STATECHANGESTARTPOSITION.fields_by_name['preset'])
_STATECHANGESTARTPOSITION.fields_by_name['preset'].containing_oneof = _STATECHANGESTARTPOSITION.oneofs_by_name['position']
DESCRIPTOR.message_types_by_name['SubscribeChangeRequest'] = _SUBSCRIBECHANGEREQUEST
DESCRIPTOR.message_types_by_name['SubscribeChangeResponse'] = _SUBSCRIBECHANGERESPONSE
DESCRIPTOR.message_types_by_name['DataOfferFilter'] = _DATAOFFERFILTER
DESCRIPTOR.message_types_by_name['DataOfferStateFilter'] = _DATAOFFERSTATEFILTER
DESCRIPTOR.message_types_by_name['DataSubscriptionFilter'] = _DATASUBSCRIPTIONFILTER
DESCRIPTOR.message_types_by_name['DataSubscriptionStateFilter'] = _DATASUBSCRIPTIONSTATEFILTER
DESCRIPTOR.message_types_by_name['PropertiesFilter'] = _PROPERTIESFILTER
DESCRIPTOR.message_types_by_name['StateChangeFilter'] = _STATECHANGEFILTER
DESCRIPTOR.message_types_by_name['StateChangeStartPosition'] = _STATECHANGESTARTPOSITION
DESCRIPTOR.enum_types_by_name['PositionPreset'] = _POSITIONPRESET
DESCRIPTOR.enum_types_by_name['StateChangeAction'] = _STATECHANGEACTION
DESCRIPTOR.enum_types_by_name['EntityType'] = _ENTITYTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubscribeChangeRequest = _reflection.GeneratedProtocolMessageType('SubscribeChangeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECHANGEREQUEST,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeRequest)
  })
_sym_db.RegisterMessage(SubscribeChangeRequest)

SubscribeChangeResponse = _reflection.GeneratedProtocolMessageType('SubscribeChangeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECHANGERESPONSE,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.logistics.hooks.v1alpha.SubscribeChangeResponse)
  })
_sym_db.RegisterMessage(SubscribeChangeResponse)

DataOfferFilter = _reflection.GeneratedProtocolMessageType('DataOfferFilter', (_message.Message,), {
  'DESCRIPTOR' : _DATAOFFERFILTER,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.logistics.hooks.v1alpha.DataOfferFilter)
  })
_sym_db.RegisterMessage(DataOfferFilter)

DataOfferStateFilter = _reflection.GeneratedProtocolMessageType('DataOfferStateFilter', (_message.Message,), {
  'DESCRIPTOR' : _DATAOFFERSTATEFILTER,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.logistics.hooks.v1alpha.DataOfferStateFilter)
  })
_sym_db.RegisterMessage(DataOfferStateFilter)

DataSubscriptionFilter = _reflection.GeneratedProtocolMessageType('DataSubscriptionFilter', (_message.Message,), {
  'DESCRIPTOR' : _DATASUBSCRIPTIONFILTER,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.logistics.hooks.v1alpha.DataSubscriptionFilter)
  })
_sym_db.RegisterMessage(DataSubscriptionFilter)

DataSubscriptionStateFilter = _reflection.GeneratedProtocolMessageType('DataSubscriptionStateFilter', (_message.Message,), {
  'DESCRIPTOR' : _DATASUBSCRIPTIONSTATEFILTER,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.logistics.hooks.v1alpha.DataSubscriptionStateFilter)
  })
_sym_db.RegisterMessage(DataSubscriptionStateFilter)

PropertiesFilter = _reflection.GeneratedProtocolMessageType('PropertiesFilter', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTIESFILTER,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.logistics.hooks.v1alpha.PropertiesFilter)
  })
_sym_db.RegisterMessage(PropertiesFilter)

StateChangeFilter = _reflection.GeneratedProtocolMessageType('StateChangeFilter', (_message.Message,), {
  'DESCRIPTOR' : _STATECHANGEFILTER,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.logistics.hooks.v1alpha.StateChangeFilter)
  })
_sym_db.RegisterMessage(StateChangeFilter)

StateChangeStartPosition = _reflection.GeneratedProtocolMessageType('StateChangeStartPosition', (_message.Message,), {
  'DESCRIPTOR' : _STATECHANGESTARTPOSITION,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:io.spoud.sdm.logistics.hooks.v1alpha.StateChangeStartPosition)
  })
_sym_db.RegisterMessage(StateChangeStartPosition)


DESCRIPTOR._options = None

_STATECHANGER = _descriptor.ServiceDescriptor(
  name='StateChanger',
  full_name='io.spoud.sdm.logistics.hooks.v1alpha.StateChanger',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=2124,
  serialized_end=2285,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubscribeChange',
    full_name='io.spoud.sdm.logistics.hooks.v1alpha.StateChanger.SubscribeChange',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBECHANGEREQUEST,
    output_type=_SUBSCRIBECHANGERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATECHANGER)

DESCRIPTOR.services_by_name['StateChanger'] = _STATECHANGER

# @@protoc_insertion_point(module_scope)
