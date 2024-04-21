# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cache.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cache.proto',
  package='cache',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x63\x61\x63he.proto\x12\x05\x63\x61\x63he\"\x19\n\x08\x43onsulta\x12\r\n\x05llave\x18\x01 \x01(\t\"\x1a\n\tRespuesta\x12\r\n\x05valor\x18\x01 \x01(\t2q\n\x05\x43\x61\x63he\x12\x33\n\x0cobtener_sala\x12\x0f.cache.Consulta\x1a\x10.cache.Respuesta\"\x00\x12\x33\n\x0cguardar_sala\x12\x0f.cache.Consulta\x1a\x10.cache.Respuesta\"\x00\x62\x06proto3'
)




_CONSULTA = _descriptor.Descriptor(
  name='Consulta',
  full_name='cache.Consulta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='llave', full_name='cache.Consulta.llave', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=22,
  serialized_end=47,
)


_RESPUESTA = _descriptor.Descriptor(
  name='Respuesta',
  full_name='cache.Respuesta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='valor', full_name='cache.Respuesta.valor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=49,
  serialized_end=75,
)

DESCRIPTOR.message_types_by_name['Consulta'] = _CONSULTA
DESCRIPTOR.message_types_by_name['Respuesta'] = _RESPUESTA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Consulta = _reflection.GeneratedProtocolMessageType('Consulta', (_message.Message,), {
  'DESCRIPTOR' : _CONSULTA,
  '__module__' : 'cache_pb2'
  # @@protoc_insertion_point(class_scope:cache.Consulta)
  })
_sym_db.RegisterMessage(Consulta)

Respuesta = _reflection.GeneratedProtocolMessageType('Respuesta', (_message.Message,), {
  'DESCRIPTOR' : _RESPUESTA,
  '__module__' : 'cache_pb2'
  # @@protoc_insertion_point(class_scope:cache.Respuesta)
  })
_sym_db.RegisterMessage(Respuesta)



_CACHE = _descriptor.ServiceDescriptor(
  name='Cache',
  full_name='cache.Cache',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=77,
  serialized_end=190,
  methods=[
  _descriptor.MethodDescriptor(
    name='obtener_sala',
    full_name='cache.Cache.obtener_sala',
    index=0,
    containing_service=None,
    input_type=_CONSULTA,
    output_type=_RESPUESTA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='guardar_sala',
    full_name='cache.Cache.guardar_sala',
    index=1,
    containing_service=None,
    input_type=_CONSULTA,
    output_type=_RESPUESTA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CACHE)

DESCRIPTOR.services_by_name['Cache'] = _CACHE

# @@protoc_insertion_point(module_scope)