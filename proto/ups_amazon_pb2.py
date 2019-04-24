# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ups_amazon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ups_amazon.proto',
  package='UA',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10ups_amazon.proto\x12\x02UA\",\n\tInitWorld\x12\x0f\n\x07worldid\x18\x01 \x02(\x03\x12\x0e\n\x06seqnum\x18\x02 \x02(\x03\"o\n\x0c\x41PackageInfo\x12\x13\n\x0b\x64\x65scription\x18\x01 \x02(\t\x12\r\n\x05\x63ount\x18\x02 \x02(\x05\x12\x11\n\tpackageid\x18\x03 \x02(\x03\x12\t\n\x01x\x18\x04 \x02(\x05\x12\t\n\x01y\x18\x05 \x02(\x05\x12\x12\n\nupsaccount\x18\x06 \x01(\t\"v\n\x12\x44\x65termineWarehouse\x12\x0c\n\x04whid\x18\x01 \x02(\x05\x12\x0c\n\x04wh_x\x18\x02 \x02(\x05\x12\x0c\n\x04wh_y\x18\x03 \x02(\x05\x12&\n\x0cpackageinfos\x18\x04 \x03(\x0b\x32\x10.UA.APackageInfo\x12\x0e\n\x06seqnum\x18\x05 \x02(\x03\"J\n\x0e\x44\x65termineTruck\x12(\n\rarrivedtrucks\x18\x01 \x03(\x0b\x32\x11.UA.TruckLocation\x12\x0e\n\x06seqnum\x18\x02 \x02(\x03\"O\n\rTruckLocation\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x0c\n\x04wh_x\x18\x02 \x02(\x05\x12\x0c\n\x04wh_y\x18\x03 \x02(\x05\x12\x11\n\tpackageid\x18\x04 \x02(\x03\"C\n\x0c\x44\x65termineDst\x12#\n\rleavingtrucks\x18\x01 \x03(\x0b\x32\x0c.UA.TruckDst\x12\x0e\n\x06seqnum\x18\x02 \x02(\x03\".\n\x08TruckDst\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x11\n\tpackageid\x18\x02 \x02(\x03\"3\n\x0eSettleShipment\x12\x11\n\tpackageid\x18\x01 \x03(\x03\x12\x0e\n\x06seqnum\x18\x02 \x02(\x03\"3\n\x0e\x46inishShipment\x12\x11\n\tpackageid\x18\x01 \x03(\x03\x12\x0e\n\x06seqnum\x18\x02 \x02(\x03\"\xa7\x01\n\nUACommands\x12\x1d\n\x06worlds\x18\x01 \x03(\x0b\x32\r.UA.InitWorld\x12\"\n\x06trucks\x18\x02 \x03(\x0b\x32\x12.UA.DetermineTruck\x12#\n\x07settled\x18\x03 \x03(\x0b\x32\x12.UA.SettleShipment\x12$\n\x08\x66inished\x18\x04 \x03(\x0b\x32\x12.UA.FinishShipment\x12\x0b\n\x03\x61\x63k\x18\x05 \x03(\x03\"f\n\nAUCommands\x12*\n\nwarehouses\x18\x01 \x03(\x0b\x32\x16.UA.DetermineWarehouse\x12\x1f\n\x05\x64\x65sts\x18\x02 \x03(\x0b\x32\x10.UA.DetermineDst\x12\x0b\n\x03\x61\x63k\x18\x04 \x03(\x03')
)




_INITWORLD = _descriptor.Descriptor(
  name='InitWorld',
  full_name='UA.InitWorld',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='worldid', full_name='UA.InitWorld.worldid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UA.InitWorld.seqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=68,
)


_APACKAGEINFO = _descriptor.Descriptor(
  name='APackageInfo',
  full_name='UA.APackageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='UA.APackageInfo.description', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='UA.APackageInfo.count', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageid', full_name='UA.APackageInfo.packageid', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='UA.APackageInfo.x', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='UA.APackageInfo.y', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upsaccount', full_name='UA.APackageInfo.upsaccount', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=181,
)


_DETERMINEWAREHOUSE = _descriptor.Descriptor(
  name='DetermineWarehouse',
  full_name='UA.DetermineWarehouse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='whid', full_name='UA.DetermineWarehouse.whid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wh_x', full_name='UA.DetermineWarehouse.wh_x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wh_y', full_name='UA.DetermineWarehouse.wh_y', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageinfos', full_name='UA.DetermineWarehouse.packageinfos', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UA.DetermineWarehouse.seqnum', index=4,
      number=5, type=3, cpp_type=2, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=301,
)


_DETERMINETRUCK = _descriptor.Descriptor(
  name='DetermineTruck',
  full_name='UA.DetermineTruck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arrivedtrucks', full_name='UA.DetermineTruck.arrivedtrucks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UA.DetermineTruck.seqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=377,
)


_TRUCKLOCATION = _descriptor.Descriptor(
  name='TruckLocation',
  full_name='UA.TruckLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='UA.TruckLocation.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wh_x', full_name='UA.TruckLocation.wh_x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wh_y', full_name='UA.TruckLocation.wh_y', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageid', full_name='UA.TruckLocation.packageid', index=3,
      number=4, type=3, cpp_type=2, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=379,
  serialized_end=458,
)


_DETERMINEDST = _descriptor.Descriptor(
  name='DetermineDst',
  full_name='UA.DetermineDst',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='leavingtrucks', full_name='UA.DetermineDst.leavingtrucks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UA.DetermineDst.seqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=527,
)


_TRUCKDST = _descriptor.Descriptor(
  name='TruckDst',
  full_name='UA.TruckDst',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='UA.TruckDst.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageid', full_name='UA.TruckDst.packageid', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=575,
)


_SETTLESHIPMENT = _descriptor.Descriptor(
  name='SettleShipment',
  full_name='UA.SettleShipment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageid', full_name='UA.SettleShipment.packageid', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UA.SettleShipment.seqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=577,
  serialized_end=628,
)


_FINISHSHIPMENT = _descriptor.Descriptor(
  name='FinishShipment',
  full_name='UA.FinishShipment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageid', full_name='UA.FinishShipment.packageid', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UA.FinishShipment.seqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=630,
  serialized_end=681,
)


_UACOMMANDS = _descriptor.Descriptor(
  name='UACommands',
  full_name='UA.UACommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='worlds', full_name='UA.UACommands.worlds', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trucks', full_name='UA.UACommands.trucks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settled', full_name='UA.UACommands.settled', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished', full_name='UA.UACommands.finished', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ack', full_name='UA.UACommands.ack', index=4,
      number=5, type=3, cpp_type=2, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=684,
  serialized_end=851,
)


_AUCOMMANDS = _descriptor.Descriptor(
  name='AUCommands',
  full_name='UA.AUCommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='warehouses', full_name='UA.AUCommands.warehouses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dests', full_name='UA.AUCommands.dests', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ack', full_name='UA.AUCommands.ack', index=2,
      number=4, type=3, cpp_type=2, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=853,
  serialized_end=955,
)

_DETERMINEWAREHOUSE.fields_by_name['packageinfos'].message_type = _APACKAGEINFO
_DETERMINETRUCK.fields_by_name['arrivedtrucks'].message_type = _TRUCKLOCATION
_DETERMINEDST.fields_by_name['leavingtrucks'].message_type = _TRUCKDST
_UACOMMANDS.fields_by_name['worlds'].message_type = _INITWORLD
_UACOMMANDS.fields_by_name['trucks'].message_type = _DETERMINETRUCK
_UACOMMANDS.fields_by_name['settled'].message_type = _SETTLESHIPMENT
_UACOMMANDS.fields_by_name['finished'].message_type = _FINISHSHIPMENT
_AUCOMMANDS.fields_by_name['warehouses'].message_type = _DETERMINEWAREHOUSE
_AUCOMMANDS.fields_by_name['dests'].message_type = _DETERMINEDST
DESCRIPTOR.message_types_by_name['InitWorld'] = _INITWORLD
DESCRIPTOR.message_types_by_name['APackageInfo'] = _APACKAGEINFO
DESCRIPTOR.message_types_by_name['DetermineWarehouse'] = _DETERMINEWAREHOUSE
DESCRIPTOR.message_types_by_name['DetermineTruck'] = _DETERMINETRUCK
DESCRIPTOR.message_types_by_name['TruckLocation'] = _TRUCKLOCATION
DESCRIPTOR.message_types_by_name['DetermineDst'] = _DETERMINEDST
DESCRIPTOR.message_types_by_name['TruckDst'] = _TRUCKDST
DESCRIPTOR.message_types_by_name['SettleShipment'] = _SETTLESHIPMENT
DESCRIPTOR.message_types_by_name['FinishShipment'] = _FINISHSHIPMENT
DESCRIPTOR.message_types_by_name['UACommands'] = _UACOMMANDS
DESCRIPTOR.message_types_by_name['AUCommands'] = _AUCOMMANDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitWorld = _reflection.GeneratedProtocolMessageType('InitWorld', (_message.Message,), dict(
  DESCRIPTOR = _INITWORLD,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UA.InitWorld)
  ))
_sym_db.RegisterMessage(InitWorld)

APackageInfo = _reflection.GeneratedProtocolMessageType('APackageInfo', (_message.Message,), dict(
  DESCRIPTOR = _APACKAGEINFO,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UA.APackageInfo)
  ))
_sym_db.RegisterMessage(APackageInfo)

DetermineWarehouse = _reflection.GeneratedProtocolMessageType('DetermineWarehouse', (_message.Message,), dict(
  DESCRIPTOR = _DETERMINEWAREHOUSE,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UA.DetermineWarehouse)
  ))
_sym_db.RegisterMessage(DetermineWarehouse)

DetermineTruck = _reflection.GeneratedProtocolMessageType('DetermineTruck', (_message.Message,), dict(
  DESCRIPTOR = _DETERMINETRUCK,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UA.DetermineTruck)
  ))
_sym_db.RegisterMessage(DetermineTruck)

TruckLocation = _reflection.GeneratedProtocolMessageType('TruckLocation', (_message.Message,), dict(
  DESCRIPTOR = _TRUCKLOCATION,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UA.TruckLocation)
  ))
_sym_db.RegisterMessage(TruckLocation)

DetermineDst = _reflection.GeneratedProtocolMessageType('DetermineDst', (_message.Message,), dict(
  DESCRIPTOR = _DETERMINEDST,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UA.DetermineDst)
  ))
_sym_db.RegisterMessage(DetermineDst)

TruckDst = _reflection.GeneratedProtocolMessageType('TruckDst', (_message.Message,), dict(
  DESCRIPTOR = _TRUCKDST,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UA.TruckDst)
  ))
_sym_db.RegisterMessage(TruckDst)

SettleShipment = _reflection.GeneratedProtocolMessageType('SettleShipment', (_message.Message,), dict(
  DESCRIPTOR = _SETTLESHIPMENT,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UA.SettleShipment)
  ))
_sym_db.RegisterMessage(SettleShipment)

FinishShipment = _reflection.GeneratedProtocolMessageType('FinishShipment', (_message.Message,), dict(
  DESCRIPTOR = _FINISHSHIPMENT,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UA.FinishShipment)
  ))
_sym_db.RegisterMessage(FinishShipment)

UACommands = _reflection.GeneratedProtocolMessageType('UACommands', (_message.Message,), dict(
  DESCRIPTOR = _UACOMMANDS,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UA.UACommands)
  ))
_sym_db.RegisterMessage(UACommands)

AUCommands = _reflection.GeneratedProtocolMessageType('AUCommands', (_message.Message,), dict(
  DESCRIPTOR = _AUCOMMANDS,
  __module__ = 'ups_amazon_pb2'
  # @@protoc_insertion_point(class_scope:UA.AUCommands)
  ))
_sym_db.RegisterMessage(AUCommands)


# @@protoc_insertion_point(module_scope)
