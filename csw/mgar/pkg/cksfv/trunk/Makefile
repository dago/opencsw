# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = cksfv
VERSION = 1.3.14
GARTYPE = v2

DESCRIPTION = Simple File Verification program. Does crc32 checksums on files. 
define BLURB
   Some files that you download will come with a .sfv file.
   This is used to verify that the files that you received
   are the same as the originals. cksfv is a program that
   can use the .sfv file to verify the downloaded files.
   Also, it can be used to create new .sfv files. 
endef

VENDOR_URL = http://zakalwe.fi/~shd/foss/cksfv/
MASTER_SITES =  http://zakalwe.fi/~shd/foss/cksfv/files/
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

REINPLACE_MATCH  = -Wall
REINPLACE_WITH   = 
REINPLACE_FILES += src/Makefile.in

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1
ISAEXEC = 1

include gar/category.mk

