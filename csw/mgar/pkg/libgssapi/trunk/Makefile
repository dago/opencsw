# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libgssapi
VERSION = 0.11
GARTYPE = v2

DESCRIPTION = Exports a gssapi interface, but doesn't implement any gssapi mechanisms itself

MASTER_SITES = http://www.citi.umich.edu/projects/nfsv4/linux/libgssapi/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Drop-unknown-linker-flags.patch

VENDOR_URL = http://cblfs.cross-lfs.org/index.php/Libgssapi

PACKAGES += CSWlibgssapi2
SPKG_DESC_CSWlibgssapi2 = Exports a gssapi interface, but doesn't implement any gssapi mechanisms itself, libgssapi.so.2
PKGFILES_CSWlibgssapi2 += $(call pkgfiles_lib,libgssapi.so.2)
RUNTIME_DEP_PKGS_CSWlibgssapi2 += CSWlibgcc-s1

PACKAGES += CSWlibgssapi-dev
SPKG_DESC_CSWlibgssapi-dev = Development files for libgssapi.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgssapi-dev += CSWlibgssapi2

GARCOMPILER = GNU

BUILD64 = 1

EXTRA_MERGE_EXCLUDE_FILES += .*/gssapi\.h

include gar/category.mk

