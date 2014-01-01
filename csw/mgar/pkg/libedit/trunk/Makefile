# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)

NAME = libedit
VERSION = 20130712-3.1
GARTYPE = v2

DESCRIPTION = Non-GPL replacement for readline library

MASTER_SITES = http://thrysoee.dk/editline/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://thrysoee.dk/editline/

PACKAGES += CSWlibedit0
SPKG_DESC_CSWlibedit0 = Non-GPL replacement for readline library
PKGFILES_CSWlibedit0 += $(call pkgfiles_lib,libedit.so.0)

PACKAGES += CSWlibedit-dev
SPKG_DESC_CSWlibedit-dev = Development files to libedit.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibedit-dev += CSWlibedit0

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS += $(DIRPATHS)

include gar/category.mk
