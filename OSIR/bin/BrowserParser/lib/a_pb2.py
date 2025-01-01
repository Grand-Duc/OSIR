# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: a.proto

from google.protobuf import descriptor as _descriptor  # type: ignore
from google.protobuf import message as _message  # type: ignore
from google.protobuf import reflection as _reflection  # type: ignore
from google.protobuf import symbol_database as _symbol_database  # type: ignore
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
  name='a.proto',
  package='content',
  syntax='proto2',
  serialized_options=b'H\003',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x07\x61.proto\x12\x07\x63ontent\"\xc4\n\n\x1dNotificationDatabaseDataProto\x12\"\n\x1apersistent_notification_id\x18\x01 \x01(\x03\x12\x17\n\x0fnotification_id\x18\x05 \x01(\t\x12\x0e\n\x06origin\x18\x02 \x01(\t\x12&\n\x1eservice_worker_registration_id\x18\x03 \x01(\x03\x12&\n\x1ereplaced_existing_notification\x18\x06 \x01(\x08\x12\x12\n\nnum_clicks\x18\x07 \x01(\x05\x12 \n\x18num_action_button_clicks\x18\x08 \x01(\x05\x12\x1c\n\x14\x63reation_time_millis\x18\t \x01(\x03\x12%\n\x1dtime_until_first_click_millis\x18\n \x01(\x03\x12$\n\x1ctime_until_last_click_millis\x18\x0b \x01(\x03\x12\x1f\n\x17time_until_close_millis\x18\x0c \x01(\x03\x12J\n\rclosed_reason\x18\r \x01(\x0e\x32\x33.content.NotificationDatabaseDataProto.ClosedReason\x12R\n\x11notification_data\x18\x04 \x01(\x0b\x32\x37.content.NotificationDatabaseDataProto.NotificationData\x12\x15\n\rhas_triggered\x18\x0e \x01(\x08\x12\x1b\n\x13is_shown_by_browser\x18\x0f \x01(\x08\x1a\xc2\x01\n\x12NotificationAction\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12L\n\x04type\x18\x04 \x01(\x0e\x32>.content.NotificationDatabaseDataProto.NotificationAction.Type\x12\x13\n\x0bplaceholder\x18\x05 \x01(\t\"\x1c\n\x04Type\x12\n\n\x06\x42UTTON\x10\x00\x12\x08\n\x04TEXT\x10\x01\x1a\xf4\x03\n\x10NotificationData\x12\r\n\x05title\x18\x01 \x01(\t\x12T\n\tdirection\x18\x02 \x01(\x0e\x32\x41.content.NotificationDatabaseDataProto.NotificationData.Direction\x12\x0c\n\x04lang\x18\x03 \x01(\t\x12\x0c\n\x04\x62ody\x18\x04 \x01(\t\x12\x0b\n\x03tag\x18\x05 \x01(\t\x12\r\n\x05image\x18\x0f \x01(\t\x12\x0c\n\x04icon\x18\x06 \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x0e \x01(\t\x12\x1d\n\x11vibration_pattern\x18\t \x03(\x05\x42\x02\x10\x01\x12\x11\n\ttimestamp\x18\x0c \x01(\x03\x12\x10\n\x08renotify\x18\r \x01(\x08\x12\x0e\n\x06silent\x18\x07 \x01(\x08\x12\x1b\n\x13require_interaction\x18\x0b \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x08 \x01(\x0c\x12J\n\x07\x61\x63tions\x18\n \x03(\x0b\x32\x39.content.NotificationDatabaseDataProto.NotificationAction\x12\x1e\n\x16show_trigger_timestamp\x18\x10 \x01(\x03\";\n\tDirection\x12\x11\n\rLEFT_TO_RIGHT\x10\x00\x12\x11\n\rRIGHT_TO_LEFT\x10\x01\x12\x08\n\x04\x41UTO\x10\x02\"4\n\x0c\x43losedReason\x12\x08\n\x04USER\x10\x00\x12\r\n\tDEVELOPER\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\x42\x02H\x03' # noqa
)


_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONACTION_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='content.NotificationDatabaseDataProto.NotificationAction.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUTTON', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=784,
  serialized_end=812,
)
_sym_db.RegisterEnumDescriptor(_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONACTION_TYPE)

_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='content.NotificationDatabaseDataProto.NotificationData.Direction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LEFT_TO_RIGHT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_TO_LEFT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1256,
  serialized_end=1315,
)
_sym_db.RegisterEnumDescriptor(_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA_DIRECTION)

_NOTIFICATIONDATABASEDATAPROTO_CLOSEDREASON = _descriptor.EnumDescriptor(
  name='ClosedReason',
  full_name='content.NotificationDatabaseDataProto.ClosedReason',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEVELOPER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1317,
  serialized_end=1369,
)
_sym_db.RegisterEnumDescriptor(_NOTIFICATIONDATABASEDATAPROTO_CLOSEDREASON)


_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONACTION = _descriptor.Descriptor(
  name='NotificationAction',
  full_name='content.NotificationDatabaseDataProto.NotificationAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='content.NotificationDatabaseDataProto.NotificationAction.action', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='content.NotificationDatabaseDataProto.NotificationAction.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='icon', full_name='content.NotificationDatabaseDataProto.NotificationAction.icon', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='content.NotificationDatabaseDataProto.NotificationAction.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='placeholder', full_name='content.NotificationDatabaseDataProto.NotificationAction.placeholder', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONACTION_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=618,
  serialized_end=812,
)

_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA = _descriptor.Descriptor(
  name='NotificationData',
  full_name='content.NotificationDatabaseDataProto.NotificationData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='content.NotificationDatabaseDataProto.NotificationData.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='content.NotificationDatabaseDataProto.NotificationData.direction', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lang', full_name='content.NotificationDatabaseDataProto.NotificationData.lang', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='content.NotificationDatabaseDataProto.NotificationData.body', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag', full_name='content.NotificationDatabaseDataProto.NotificationData.tag', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='content.NotificationDatabaseDataProto.NotificationData.image', index=5,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='icon', full_name='content.NotificationDatabaseDataProto.NotificationData.icon', index=6,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='badge', full_name='content.NotificationDatabaseDataProto.NotificationData.badge', index=7,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vibration_pattern', full_name='content.NotificationDatabaseDataProto.NotificationData.vibration_pattern', index=8,
      number=9, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='content.NotificationDatabaseDataProto.NotificationData.timestamp', index=9,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='renotify', full_name='content.NotificationDatabaseDataProto.NotificationData.renotify', index=10,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='silent', full_name='content.NotificationDatabaseDataProto.NotificationData.silent', index=11,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='require_interaction', full_name='content.NotificationDatabaseDataProto.NotificationData.require_interaction', index=12,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='content.NotificationDatabaseDataProto.NotificationData.data', index=13,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actions', full_name='content.NotificationDatabaseDataProto.NotificationData.actions', index=14,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='show_trigger_timestamp', full_name='content.NotificationDatabaseDataProto.NotificationData.show_trigger_timestamp', index=15,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA_DIRECTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=815,
  serialized_end=1315,
)

_NOTIFICATIONDATABASEDATAPROTO = _descriptor.Descriptor(
  name='NotificationDatabaseDataProto',
  full_name='content.NotificationDatabaseDataProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='persistent_notification_id', full_name='content.NotificationDatabaseDataProto.persistent_notification_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notification_id', full_name='content.NotificationDatabaseDataProto.notification_id', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin', full_name='content.NotificationDatabaseDataProto.origin', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_worker_registration_id', full_name='content.NotificationDatabaseDataProto.service_worker_registration_id', index=3,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='replaced_existing_notification', full_name='content.NotificationDatabaseDataProto.replaced_existing_notification', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_clicks', full_name='content.NotificationDatabaseDataProto.num_clicks', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_action_button_clicks', full_name='content.NotificationDatabaseDataProto.num_action_button_clicks', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time_millis', full_name='content.NotificationDatabaseDataProto.creation_time_millis', index=7,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_until_first_click_millis', full_name='content.NotificationDatabaseDataProto.time_until_first_click_millis', index=8,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_until_last_click_millis', full_name='content.NotificationDatabaseDataProto.time_until_last_click_millis', index=9,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_until_close_millis', full_name='content.NotificationDatabaseDataProto.time_until_close_millis', index=10,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='closed_reason', full_name='content.NotificationDatabaseDataProto.closed_reason', index=11,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notification_data', full_name='content.NotificationDatabaseDataProto.notification_data', index=12,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_triggered', full_name='content.NotificationDatabaseDataProto.has_triggered', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_shown_by_browser', full_name='content.NotificationDatabaseDataProto.is_shown_by_browser', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONACTION, _NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA, ],
  enum_types=[
    _NOTIFICATIONDATABASEDATAPROTO_CLOSEDREASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=1369,
)

_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONACTION.fields_by_name['type'].enum_type = _NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONACTION_TYPE
_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONACTION.containing_type = _NOTIFICATIONDATABASEDATAPROTO
_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONACTION_TYPE.containing_type = _NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONACTION
_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA.fields_by_name['direction'].enum_type = _NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA_DIRECTION
_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA.fields_by_name['actions'].message_type = _NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONACTION
_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA.containing_type = _NOTIFICATIONDATABASEDATAPROTO
_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA_DIRECTION.containing_type = _NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA
_NOTIFICATIONDATABASEDATAPROTO.fields_by_name['closed_reason'].enum_type = _NOTIFICATIONDATABASEDATAPROTO_CLOSEDREASON
_NOTIFICATIONDATABASEDATAPROTO.fields_by_name['notification_data'].message_type = _NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA
_NOTIFICATIONDATABASEDATAPROTO_CLOSEDREASON.containing_type = _NOTIFICATIONDATABASEDATAPROTO
DESCRIPTOR.message_types_by_name['NotificationDatabaseDataProto'] = _NOTIFICATIONDATABASEDATAPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NotificationDatabaseDataProto = _reflection.GeneratedProtocolMessageType('NotificationDatabaseDataProto', (_message.Message,), {

  'NotificationAction': _reflection.GeneratedProtocolMessageType('NotificationAction', (_message.Message,), {
    'DESCRIPTOR': _NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONACTION,
    '__module__': 'a_pb2'
    # @@protoc_insertion_point(class_scope:content.NotificationDatabaseDataProto.NotificationAction)
    }),

  'NotificationData': _reflection.GeneratedProtocolMessageType('NotificationData', (_message.Message,), {
    'DESCRIPTOR': _NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA,
    '__module__': 'a_pb2'
    # @@protoc_insertion_point(class_scope:content.NotificationDatabaseDataProto.NotificationData)
    }),
  'DESCRIPTOR': _NOTIFICATIONDATABASEDATAPROTO,
  '__module__': 'a_pb2'
  # @@protoc_insertion_point(class_scope:content.NotificationDatabaseDataProto)
  })
_sym_db.RegisterMessage(NotificationDatabaseDataProto)
_sym_db.RegisterMessage(NotificationDatabaseDataProto.NotificationAction)
_sym_db.RegisterMessage(NotificationDatabaseDataProto.NotificationData)


DESCRIPTOR._options = None
_NOTIFICATIONDATABASEDATAPROTO_NOTIFICATIONDATA.fields_by_name['vibration_pattern']._options = None
# @@protoc_insertion_point(module_scope)
