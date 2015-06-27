# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libmetalink
VERSION = 0.1.3
GARTYPE = v2

DESCRIPTION = A library to add Metalink functionality

MASTER_SITES = https://launchpad.net/libmetalink/trunk/$(DISTNAME)/+download/
DISTFILES += $(DISTNAME).tar.xz

GARCOMPILER = GNU

PACKAGES += CSWlibmetalink3
SPKG_DESC_CSWlibmetalink3 = A library to add Metalink functionality, libmetalink.so.3
PKGFILES_CSWlibmetalink3 += $(call pkgfiles_lib,libmetalink.so.3)
RUNTIME_DEP_PKGS_CSWlibmetalink3 += CSWlibgcc-s1  
RUNTIME_DEP_PKGS_CSWlibmetalink3 += CSWlibexpat1

PACKAGES += CSWlibmetalink-dev
SPKG_DESC_CSWlibmetalink-dev = Development files for libmetalink.so.3
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibmetalink-dev += CSWlibmetalink3

BUILD64 = 1

include gar/category.mk

