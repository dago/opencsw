# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libestr
VERSION = 0.1.10
GARTYPE = v2

DESCRIPTION = Some essentials for string handling

MASTER_SITES = http://libestr.adiscon.com/files/download/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://libestr.adiscon.com

PACKAGES += CSWlibestr0
SPKG_DESC_CSWlibestr0 = Some essentials for string handling, libestr.so.0
PKGFILES_CSWlibestr0 += $(call pkgfiles_lib,libestr.so.0)

PACKAGES += CSWlibestr-dev
SPKG_DESC_CSWlibestr-dev = Development files for libestr.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibestr-dev += CSWlibestr0

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

