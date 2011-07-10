# TBD:
# - There are tests failing, this is serious as some fields seem to have the wrong size:
#
#   File: script/00-login.scr, Line: 45
#   Invalid data length 150 vs expected 147
#
#     0000:  31 00 00 00 8e 00 00 00 56 34 12 00 70 6c 01 09  1.......V4..pl..
#     0010:  ad 7d 58 00 00 00 00 00 00 00 00 00 00 00 00 00  .}X.............
#     0020:  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
#     0030:  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
#     0040:  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
#     0050:  16 00 00 00 44 33 22 11 37 27 00 00 00 00 00 00  ....D3".7'......
#     0060:  00 00 00 00 00 00 00 00 00 00 ff 64 1e 00 00 00  ...........d....
#     0070:  47 61 64 75 2d 47 61 64 75 20 43 6c 69 65 6e 74  Gadu-Gadu Client
#     0080:  20 42 75 69 6c 64 20 31 2e 32 2e 33 2e 34 04 00   Build 1.2.3.4..
#     0090:  00 00 54 65 73 74                                ..Test          
#     
#   expect data (
#     31 00 00 00, auto, 56 34 12 00, "pl", 01, 09		-> OK
#     ad 7d 58 00*60,						-> too long by 1
#     16 00 00 00, 44 33 22 11, 37 27 00 00, 00 00 00 00,	-> OK
#     00 00, 00 00 00 00, 00 00, ff, 64, 1e 00 00 00,		-> too long by 2
#     "Gadu-Gadu", 20, "Client",				-> OK
#     20, "Build", 20, "1.2.3.4", 04 00				-> OK
#     00 00, "Test")						-> OK
#

NAME = libgadu
#
VERSION = 1.11.0
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Gadu-Gadu protocol implementation library

MASTER_SITES = http://toxygen.net/libgadu/files/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Use-127.0.0.1-for-localhost-or-fail.patch
PATCHFILES += 0002-Do-not-forcefully-set-CFLAGS-to-gcc-specific-stuff.patch

VENDOR_URL = http://toxygen.net/libgadu

# There are zero-sized structs
EXTRA_CFLAGS += -features=extensions

BUILD64 = 1

include gar/category.mk
