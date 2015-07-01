# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = librelp
VERSION = 1.2.7
GARTYPE = v2

DESCRIPTION = A reliable logging library

MASTER_SITES = http://download.rsyslog.com/librelp/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://www.librelp.com

PACKAGES += CSWlibrelp0
SPKG_DESC_CSWlibrelp0 = A reliable logging library, librelp.so.0
PKGFILES_CSWlibrelp0 += $(call pkgfiles_lib,librelp.so.0)
RUNTIME_DEP_PKGS_CSWlibrelp0 += CSWlibgnutls28

PACKAGES += CSWlibrelp-dev
SPKG_DESC_CSWlibrelp-dev = Development files for librelp.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibrelp-dev += CSWlibrelp0

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

