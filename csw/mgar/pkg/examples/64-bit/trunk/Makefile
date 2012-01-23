# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = hello
VERSION = 0.1.1
CATEGORIES = lib
DESCRIPTION = A test of a 64-bit build
define BLURB
endef
SPKG_SOURCEURL = http://www.opencsw.org/
MASTER_SITES =
DISTFILES  = $(NAME)-$(VERSION).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES += CSWlibhello0
CATALOGNAME_CSWlibhello0 = libhello0
PKGFILES_CSWlibhello0 += $(call baseisadirs,$(libdir),libhello\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibhello0 += $(DESCRIPTION), libhello.so.0
RUNTIME_DEP_PKGS_CSWhello += CSWlibhello0

prefix = $(BUILD_PREFIX)/foo
libdir = $(BUILD_PREFIX)/lib
BUILD64_LIBS_ONLY = 1

include gar/category.mk

post-merge:
	$(FILEDIR)/check_pkgroot.sh "$(PKGROOT)"
