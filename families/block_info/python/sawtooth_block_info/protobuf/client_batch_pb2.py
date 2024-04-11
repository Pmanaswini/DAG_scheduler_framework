# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: python/sawtooth_block_info/protobuf/client_batch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from python.sawtooth_block_info.protobuf import batch_pb2 as python_dot_sawtooth__block__info_dot_protobuf_dot_batch__pb2
from python.sawtooth_block_info.protobuf import client_list_control_pb2 as python_dot_sawtooth__block__info_dot_protobuf_dot_client__list__control__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='python/sawtooth_block_info/protobuf/client_batch.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\025sawtooth.sdk.protobufP\001Z\020client_batch_pb2'),
  serialized_pb=_b('\n6python/sawtooth_block_info/protobuf/client_batch.proto\x1a/python/sawtooth_block_info/protobuf/batch.proto\x1a=python/sawtooth_block_info/protobuf/client_list_control.proto\"\x89\x01\n\x16\x43lientBatchListRequest\x12\x0f\n\x07head_id\x18\x01 \x01(\t\x12\x11\n\tbatch_ids\x18\x02 \x03(\t\x12%\n\x06paging\x18\x03 \x01(\x0b\x32\x15.ClientPagingControls\x12$\n\x07sorting\x18\x04 \x03(\x0b\x32\x13.ClientSortControls\"\xb7\x02\n\x17\x43lientBatchListResponse\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.ClientBatchListResponse.Status\x12\x17\n\x07\x62\x61tches\x18\x02 \x03(\x0b\x32\x06.Batch\x12\x0f\n\x07head_id\x18\x03 \x01(\t\x12%\n\x06paging\x18\x04 \x01(\x0b\x32\x15.ClientPagingResponse\"\x99\x01\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\r\n\tNOT_READY\x10\x03\x12\x0b\n\x07NO_ROOT\x10\x04\x12\x0f\n\x0bNO_RESOURCE\x10\x05\x12\x12\n\x0eINVALID_PAGING\x10\x06\x12\x10\n\x0cINVALID_SORT\x10\x07\x12\x0e\n\nINVALID_ID\x10\x08\")\n\x15\x43lientBatchGetRequest\x12\x10\n\x08\x62\x61tch_id\x18\x01 \x01(\t\"\xb8\x01\n\x16\x43lientBatchGetResponse\x12.\n\x06status\x18\x01 \x01(\x0e\x32\x1e.ClientBatchGetResponse.Status\x12\x15\n\x05\x62\x61tch\x18\x02 \x01(\x0b\x32\x06.Batch\"W\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x0f\n\x0bNO_RESOURCE\x10\x05\x12\x0e\n\nINVALID_ID\x10\x08\x42+\n\x15sawtooth.sdk.protobufP\x01Z\x10\x63lient_batch_pb2b\x06proto3')
  ,
  dependencies=[python_dot_sawtooth__block__info_dot_protobuf_dot_batch__pb2.DESCRIPTOR,python_dot_sawtooth__block__info_dot_protobuf_dot_client__list__control__pb2.DESCRIPTOR,])



_CLIENTBATCHLISTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ClientBatchListResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_READY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ROOT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_RESOURCE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PAGING', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SORT', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ID', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=469,
  serialized_end=622,
)
_sym_db.RegisterEnumDescriptor(_CLIENTBATCHLISTRESPONSE_STATUS)

_CLIENTBATCHGETRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ClientBatchGetResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_RESOURCE', index=3, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ID', index=4, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=765,
  serialized_end=852,
)
_sym_db.RegisterEnumDescriptor(_CLIENTBATCHGETRESPONSE_STATUS)


_CLIENTBATCHLISTREQUEST = _descriptor.Descriptor(
  name='ClientBatchListRequest',
  full_name='ClientBatchListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head_id', full_name='ClientBatchListRequest.head_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_ids', full_name='ClientBatchListRequest.batch_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paging', full_name='ClientBatchListRequest.paging', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sorting', full_name='ClientBatchListRequest.sorting', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=171,
  serialized_end=308,
)


_CLIENTBATCHLISTRESPONSE = _descriptor.Descriptor(
  name='ClientBatchListResponse',
  full_name='ClientBatchListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ClientBatchListResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batches', full_name='ClientBatchListResponse.batches', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='head_id', full_name='ClientBatchListResponse.head_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paging', full_name='ClientBatchListResponse.paging', index=3,
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
    _CLIENTBATCHLISTRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=622,
)


_CLIENTBATCHGETREQUEST = _descriptor.Descriptor(
  name='ClientBatchGetRequest',
  full_name='ClientBatchGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='ClientBatchGetRequest.batch_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=624,
  serialized_end=665,
)


_CLIENTBATCHGETRESPONSE = _descriptor.Descriptor(
  name='ClientBatchGetResponse',
  full_name='ClientBatchGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ClientBatchGetResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch', full_name='ClientBatchGetResponse.batch', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTBATCHGETRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=668,
  serialized_end=852,
)

_CLIENTBATCHLISTREQUEST.fields_by_name['paging'].message_type = python_dot_sawtooth__block__info_dot_protobuf_dot_client__list__control__pb2._CLIENTPAGINGCONTROLS
_CLIENTBATCHLISTREQUEST.fields_by_name['sorting'].message_type = python_dot_sawtooth__block__info_dot_protobuf_dot_client__list__control__pb2._CLIENTSORTCONTROLS
_CLIENTBATCHLISTRESPONSE.fields_by_name['status'].enum_type = _CLIENTBATCHLISTRESPONSE_STATUS
_CLIENTBATCHLISTRESPONSE.fields_by_name['batches'].message_type = python_dot_sawtooth__block__info_dot_protobuf_dot_batch__pb2._BATCH
_CLIENTBATCHLISTRESPONSE.fields_by_name['paging'].message_type = python_dot_sawtooth__block__info_dot_protobuf_dot_client__list__control__pb2._CLIENTPAGINGRESPONSE
_CLIENTBATCHLISTRESPONSE_STATUS.containing_type = _CLIENTBATCHLISTRESPONSE
_CLIENTBATCHGETRESPONSE.fields_by_name['status'].enum_type = _CLIENTBATCHGETRESPONSE_STATUS
_CLIENTBATCHGETRESPONSE.fields_by_name['batch'].message_type = python_dot_sawtooth__block__info_dot_protobuf_dot_batch__pb2._BATCH
_CLIENTBATCHGETRESPONSE_STATUS.containing_type = _CLIENTBATCHGETRESPONSE
DESCRIPTOR.message_types_by_name['ClientBatchListRequest'] = _CLIENTBATCHLISTREQUEST
DESCRIPTOR.message_types_by_name['ClientBatchListResponse'] = _CLIENTBATCHLISTRESPONSE
DESCRIPTOR.message_types_by_name['ClientBatchGetRequest'] = _CLIENTBATCHGETREQUEST
DESCRIPTOR.message_types_by_name['ClientBatchGetResponse'] = _CLIENTBATCHGETRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientBatchListRequest = _reflection.GeneratedProtocolMessageType('ClientBatchListRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBATCHLISTREQUEST,
  __module__ = 'python.sawtooth_block_info.protobuf.client_batch_pb2'
  # @@protoc_insertion_point(class_scope:ClientBatchListRequest)
  ))
_sym_db.RegisterMessage(ClientBatchListRequest)

ClientBatchListResponse = _reflection.GeneratedProtocolMessageType('ClientBatchListResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBATCHLISTRESPONSE,
  __module__ = 'python.sawtooth_block_info.protobuf.client_batch_pb2'
  # @@protoc_insertion_point(class_scope:ClientBatchListResponse)
  ))
_sym_db.RegisterMessage(ClientBatchListResponse)

ClientBatchGetRequest = _reflection.GeneratedProtocolMessageType('ClientBatchGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBATCHGETREQUEST,
  __module__ = 'python.sawtooth_block_info.protobuf.client_batch_pb2'
  # @@protoc_insertion_point(class_scope:ClientBatchGetRequest)
  ))
_sym_db.RegisterMessage(ClientBatchGetRequest)

ClientBatchGetResponse = _reflection.GeneratedProtocolMessageType('ClientBatchGetResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBATCHGETRESPONSE,
  __module__ = 'python.sawtooth_block_info.protobuf.client_batch_pb2'
  # @@protoc_insertion_point(class_scope:ClientBatchGetResponse)
  ))
_sym_db.RegisterMessage(ClientBatchGetResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)