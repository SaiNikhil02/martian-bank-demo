# Copyright (c) 2023 Cisco Systems, Inc. and its affiliates All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accounts.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()



DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0e\x61\x63\x63ounts.proto\"\xbf\x01\n\x07\x41\x63\x63ount'
    b'\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x01 \x01(\t\x12\x10\n\x08'
    b'\x65mail_id\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63ount_type\x18\x03 \x01(\t'
    b'\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\x16\n\x0egovt_id_number\x18\x05 \x01(\t'
    b'\x12\x1a\n\x12government_id_type\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t'
    b'\x12\x10\n\x08\x63urrency\x18\x08 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\t \x01(\x01'
    b'\"\x91\x01\n\x14\x43reateAccountRequest\x12\x10\n\x08\x65mail_id\x18\x01 \x01(\t'
    b'\x12\x14\n\x0c\x61\x63\x63ount_type\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t'
    b'\x12\x16\n\x0egovt_id_number\x18\x04 \x01(\t\x12\x1a\n\x12government_id_type\x18\x05 \x01(\t'
    b'\x12\x0c\n\x04name\x18\x06 \x01(\t\"\'\n\x15\x43reateAccountResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08'
    b'\"&\n\x12GetAccountsRequest\x12\x10\n\x08\x65mail_id\x18\x01 \x01(\t'
    b'\"1\n\x13GetAccountsResponse\x12\x1a\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32\x08.Account'
    b'\"X\n\rAccountDetail\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t'
    b'\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x01\x12\x10\n\x08\x63urrency\x18\x04 \x01(\t'
    b'\"1\n\x17GetAccountDetailRequest\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x01 \x01(\t'
    b'2\xd0\x01\n\x15\x41\x63\x63ountDetailsService\x12=\n\x11getAccountDetails'
    b'\x12\x18.GetAccountDetailRequest\x1a\x0e.AccountDetail'
    b'\x12>\n\rcreateAccount\x12\x15.CreateAccountRequest\x1a\x16.CreateAccountResponse'
    b'\x12\x38\n\x0bgetAccounts\x12\x13.GetAccountsRequest\x1a\x14.GetAccountsResponseb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'accounts_pb2', globals())
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._options = None
  ACCOUNT._serialized_start=19
  ACCOUNT._serialized_end=210
  CREATEACCOUNTREQUEST._serialized_start=213
  CREATEACCOUNTREQUEST._serialized_end=358
  CREATEACCOUNTRESPONSE._serialized_start=360
  CREATEACCOUNTRESPONSE._serialized_end=399
  GETACCOUNTSREQUEST._serialized_start=401
  GETACCOUNTSREQUEST._serialized_end=439
  GETACCOUNTSRESPONSE._serialized_start=441
  GETACCOUNTSRESPONSE._serialized_end=490
  ACCOUNTDETAIL._serialized_start=492
  ACCOUNTDETAIL._serialized_end=580
  GETACCOUNTDETAILREQUEST._serialized_start=582
  GETACCOUNTDETAILREQUEST._serialized_end=631
  ACCOUNTDETAILSSERVICE._serialized_start=634
  ACCOUNTDETAILSSERVICE._serialized_end=842
# @@protoc_insertion_point(module_scope)
