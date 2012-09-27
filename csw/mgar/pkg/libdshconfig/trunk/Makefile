# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libdshconfig
VERSION = 0.20.9
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = Library for parsing dsh-style configuration files

MASTER_SITES = http://www.netfort.gr.jp/~dancer/software/downloads/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://www.netfort.gr.jp/~dancer/software/dsh.html.en

PACKAGES += CSWlibdshconfig1
SPKG_DESC_CSWlibdshconfig1 = Library for parsing dsh-style configuration files, libdshconfig.so.1
PKGFILES_CSWlibdshconfig1 += $(call pkgfiles_lib,libdshconfig.so.1)

PACKAGES += CSWlibdshconfig-dev
SPKG_DESC_CSWlibdshconfig-dev = Development files for libdshconfig.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibdshconfig-dev += CSWlibdshconfig1

BUILD64 = 1

include gar/category.mk

