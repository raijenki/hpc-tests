# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mpi_monitor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11mpi_monitor.proto\x12\x0bmpi_monitor\"\x1b\n\navailNodes\x12\r\n\x05nodes\x18\x01 \x01(\x05\"\x1c\n\x08nodeName\x12\x10\n\x08nodeName\x18\x01 \x01(\t\"&\n\x0c\x43onfirmation\x12\x16\n\x0e\x63onfirmMessage\x18\x01 \x01(\t2\x92\x01\n\x07Monitor\x12\x45\n\rSendResources\x12\x17.mpi_monitor.availNodes\x1a\x19.mpi_monitor.Confirmation\"\x00\x12@\n\nactiveNode\x12\x15.mpi_monitor.nodeName\x1a\x19.mpi_monitor.Confirmation\"\x00\x42.\n\x13io.grpc.mpi_monitorB\x0fMPIMonitorProtoP\x01\xa2\x02\x03MMGb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mpi_monitor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023io.grpc.mpi_monitorB\017MPIMonitorProtoP\001\242\002\003MMG'
  _AVAILNODES._serialized_start=34
  _AVAILNODES._serialized_end=61
  _NODENAME._serialized_start=63
  _NODENAME._serialized_end=91
  _CONFIRMATION._serialized_start=93
  _CONFIRMATION._serialized_end=131
  _MONITOR._serialized_start=134
  _MONITOR._serialized_end=280
# @@protoc_insertion_point(module_scope)
