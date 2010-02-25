# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = sharutils
GARVERSION = 4.6.3
CATEGORIES = utils
DESCRIPTION = makes so-called shell archives out of many files
define BLURB
endef
SPKG_SOURCEURL = http://www.gnu.org/software/sharutils/
MASTER_SITES = ftp://ftp.gnu.org/gnu/sharutils/REL-$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
TEST_TARGET = check
CONFIGURE_ARGS = $(DIRPATHS)
BUILD64 = 1
MD5SUM = gm5sum
export MD5SUM
include gar/category.mk
