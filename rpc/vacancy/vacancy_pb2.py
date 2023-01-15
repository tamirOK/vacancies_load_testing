# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vacancy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rvacancy.proto\x12\x02pb\x1a\x1fgoogle/protobuf/timestamp.proto\"s\n\x14\x43reateVacancyRequest\x12\r\n\x05Title\x18\x01 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x02 \x01(\t\x12&\n\x08\x44ivision\x18\x03 \x01(\x0e\x32\x14.pb.Vacancy.DIVISION\x12\x0f\n\x07\x43ountry\x18\x04 \x01(\t\"\x1c\n\x0eVacancyRequest\x12\n\n\x02Id\x18\x01 \x01(\t\"/\n\x0fVacancyResponse\x12\x1c\n\x07vacancy\x18\x01 \x01(\x0b\x32\x0b.pb.Vacancy\"O\n\x13GetVacanciesRequest\x12\x11\n\x04page\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x12\n\x05limit\x18\x02 \x01(\x03H\x01\x88\x01\x01\x42\x07\n\x05_pageB\x08\n\x06_limit\"\xa2\x02\n\x07Vacancy\x12\n\n\x02Id\x18\x01 \x01(\t\x12\r\n\x05Title\x18\x02 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x03 \x01(\t\x12\r\n\x05Views\x18\x04 \x01(\x05\x12&\n\x08\x44ivision\x18\x05 \x01(\x0e\x32\x14.pb.Vacancy.DIVISION\x12\x0f\n\x07\x43ountry\x18\x06 \x01(\t\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"?\n\x08\x44IVISION\x12\x0f\n\x0b\x44\x45VELOPMENT\x10\x00\x12\x0c\n\x08SECURITY\x10\x01\x12\t\n\x05SALES\x10\x02\x12\t\n\x05OTHER\x10\x03\"\xe4\x01\n\x14UpdateVacancyRequest\x12\n\n\x02Id\x18\x01 \x01(\t\x12\x12\n\x05Title\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x44\x65scription\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05Views\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12+\n\x08\x44ivision\x18\x05 \x01(\x0e\x32\x14.pb.Vacancy.DIVISIONH\x03\x88\x01\x01\x12\x14\n\x07\x43ountry\x18\x06 \x01(\tH\x04\x88\x01\x01\x42\x08\n\x06_TitleB\x0e\n\x0c_DescriptionB\x08\n\x06_ViewsB\x0b\n\t_DivisionB\n\n\x08_Country\"(\n\x15\x44\x65leteVacancyResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xc9\x02\n\x0eVacancyService\x12@\n\rCreateVacancy\x12\x18.pb.CreateVacancyRequest\x1a\x13.pb.VacancyResponse\"\x00\x12@\n\rUpdateVacancy\x12\x18.pb.UpdateVacancyRequest\x1a\x13.pb.VacancyResponse\"\x00\x12\x37\n\nGetVacancy\x12\x12.pb.VacancyRequest\x1a\x13.pb.VacancyResponse\"\x00\x12@\n\rDeleteVacancy\x12\x12.pb.VacancyRequest\x1a\x19.pb.DeleteVacancyResponse\"\x00\x12\x38\n\x0cGetVacancies\x12\x17.pb.GetVacanciesRequest\x1a\x0b.pb.Vacancy\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vacancy_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEVACANCYREQUEST._serialized_start=54
  _CREATEVACANCYREQUEST._serialized_end=169
  _VACANCYREQUEST._serialized_start=171
  _VACANCYREQUEST._serialized_end=199
  _VACANCYRESPONSE._serialized_start=201
  _VACANCYRESPONSE._serialized_end=248
  _GETVACANCIESREQUEST._serialized_start=250
  _GETVACANCIESREQUEST._serialized_end=329
  _VACANCY._serialized_start=332
  _VACANCY._serialized_end=622
  _VACANCY_DIVISION._serialized_start=559
  _VACANCY_DIVISION._serialized_end=622
  _UPDATEVACANCYREQUEST._serialized_start=625
  _UPDATEVACANCYREQUEST._serialized_end=853
  _DELETEVACANCYRESPONSE._serialized_start=855
  _DELETEVACANCYRESPONSE._serialized_end=895
  _VACANCYSERVICE._serialized_start=898
  _VACANCYSERVICE._serialized_end=1227
# @@protoc_insertion_point(module_scope)