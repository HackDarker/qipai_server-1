# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: table.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ddz_pb2
import majiang_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='table.proto',
  package='table',
  serialized_pb=_b('\n\x0btable.proto\x12\x05table\x1a\tddz.proto\x1a\rmajiang.proto\"!\n\tREQ_ENTER\x12\x14\n\ttable_gid\x18\x01 \x01(\x06:\x01\x30\"\xa3\x01\n\tRSP_ENTER\x12\x11\n\x06result\x18\x01 \x01(\x05:\x01\x30\x12\x14\n\tgame_type\x18\x02 \x01(\r:\x01\x30\x12\x15\n\ntable_type\x18\x03 \x01(\r:\x01\x30\x12&\n\x0e\x64\x64z_enter_info\x18\x04 \x01(\x0b\x32\x0e.ddz.EnterInfo\x12.\n\x12majiang_enter_info\x18\x05 \x01(\x0b\x32\x12.majiang.EnterInfo\"\x89\x01\n\x10REQ_CONFIG_CARDS\x12\x14\n\tgame_type\x18\x01 \x01(\r:\x01\x30\x12\x14\n\nself_cards\x18\x02 \x01(\t:\x00\x12\x10\n\x06\x63\x61rds1\x18\x03 \x01(\t:\x00\x12\x10\n\x06\x63\x61rds2\x18\x04 \x01(\t:\x00\x12\x10\n\x06\x63\x61rds3\x18\x05 \x01(\t:\x00\x12\x13\n\x08laizi_id\x18\x06 \x01(\r:\x01\x30\"%\n\x10RSP_CONFIG_CARDS\x12\x11\n\x06result\x18\x01 \x01(\x05:\x01\x30')
  ,
  dependencies=[ddz_pb2.DESCRIPTOR,majiang_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQ_ENTER = _descriptor.Descriptor(
  name='REQ_ENTER',
  full_name='table.REQ_ENTER',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_gid', full_name='table.REQ_ENTER.table_gid', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=81,
)


_RSP_ENTER = _descriptor.Descriptor(
  name='RSP_ENTER',
  full_name='table.RSP_ENTER',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='table.RSP_ENTER.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_type', full_name='table.RSP_ENTER.game_type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table_type', full_name='table.RSP_ENTER.table_type', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ddz_enter_info', full_name='table.RSP_ENTER.ddz_enter_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='majiang_enter_info', full_name='table.RSP_ENTER.majiang_enter_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=247,
)


_REQ_CONFIG_CARDS = _descriptor.Descriptor(
  name='REQ_CONFIG_CARDS',
  full_name='table.REQ_CONFIG_CARDS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_type', full_name='table.REQ_CONFIG_CARDS.game_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='self_cards', full_name='table.REQ_CONFIG_CARDS.self_cards', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cards1', full_name='table.REQ_CONFIG_CARDS.cards1', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cards2', full_name='table.REQ_CONFIG_CARDS.cards2', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cards3', full_name='table.REQ_CONFIG_CARDS.cards3', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='laizi_id', full_name='table.REQ_CONFIG_CARDS.laizi_id', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=387,
)


_RSP_CONFIG_CARDS = _descriptor.Descriptor(
  name='RSP_CONFIG_CARDS',
  full_name='table.RSP_CONFIG_CARDS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='table.RSP_CONFIG_CARDS.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=426,
)

_RSP_ENTER.fields_by_name['ddz_enter_info'].message_type = ddz_pb2._ENTERINFO
_RSP_ENTER.fields_by_name['majiang_enter_info'].message_type = majiang_pb2._ENTERINFO
DESCRIPTOR.message_types_by_name['REQ_ENTER'] = _REQ_ENTER
DESCRIPTOR.message_types_by_name['RSP_ENTER'] = _RSP_ENTER
DESCRIPTOR.message_types_by_name['REQ_CONFIG_CARDS'] = _REQ_CONFIG_CARDS
DESCRIPTOR.message_types_by_name['RSP_CONFIG_CARDS'] = _RSP_CONFIG_CARDS

REQ_ENTER = _reflection.GeneratedProtocolMessageType('REQ_ENTER', (_message.Message,), dict(
  DESCRIPTOR = _REQ_ENTER,
  __module__ = 'table_pb2'
  # @@protoc_insertion_point(class_scope:table.REQ_ENTER)
  ))
_sym_db.RegisterMessage(REQ_ENTER)

RSP_ENTER = _reflection.GeneratedProtocolMessageType('RSP_ENTER', (_message.Message,), dict(
  DESCRIPTOR = _RSP_ENTER,
  __module__ = 'table_pb2'
  # @@protoc_insertion_point(class_scope:table.RSP_ENTER)
  ))
_sym_db.RegisterMessage(RSP_ENTER)

REQ_CONFIG_CARDS = _reflection.GeneratedProtocolMessageType('REQ_CONFIG_CARDS', (_message.Message,), dict(
  DESCRIPTOR = _REQ_CONFIG_CARDS,
  __module__ = 'table_pb2'
  # @@protoc_insertion_point(class_scope:table.REQ_CONFIG_CARDS)
  ))
_sym_db.RegisterMessage(REQ_CONFIG_CARDS)

RSP_CONFIG_CARDS = _reflection.GeneratedProtocolMessageType('RSP_CONFIG_CARDS', (_message.Message,), dict(
  DESCRIPTOR = _RSP_CONFIG_CARDS,
  __module__ = 'table_pb2'
  # @@protoc_insertion_point(class_scope:table.RSP_CONFIG_CARDS)
  ))
_sym_db.RegisterMessage(RSP_CONFIG_CARDS)


# @@protoc_insertion_point(module_scope)