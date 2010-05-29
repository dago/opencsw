# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = sharutils
GARVERSION = 4.9
CATEGORIES = utils
DESCRIPTION = makes so-called shell archives out of many files
define BLURB
endef
SPKG_SOURCEURL = http://www.gnu.org/software/sharutils/
MASTER_SITES = ftp://ftp.gnu.org/gnu/sharutils/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
TEST_TARGET = check
CONFIGURE_ARGS = $(DIRPATHS)
PATCHFILES = sun-sed.patch
BUILD64 = 1
# To make the test use gmd5sum
MD5SUM = gmd5sum
RUNTIME_DEP_PKGS_CSWsharutils += CSWggettextrt
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWsharutils) CSWtextutils
export MD5SUM
include gar/category.mk
