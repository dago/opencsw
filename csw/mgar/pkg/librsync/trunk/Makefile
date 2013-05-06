# $Id$

NAME = librsync
VERSION = 0.9.7
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Library with the rolling-checksum algorithm known from rsync
define BLURB
  librsync implements the rolling-checksum algorithm of remote file
  synchronization that was popularized by the rsync utility and is used in
  rproxy. This algorithm transfers the differences between 2 files without
  needing both files on the same system.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTNAME).tar.gz

# If it builds fine, why not.
PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparcbrsync += CSWzlib

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared=yes
CONFIGURE_ARGS += --enable-static=no

# delta.c contains inlined functions without storage qualifiers, treat them
# as static as the only references are within delta.c itself. Otherwise the
# linking will fail to resolve those references. See "inline functions"
#   http://docs.sun.com/app/docs/doc/820-7598/6nirjunib?a=view
EXTRA_CFLAGS = -feaPACKAGES += CSWlibrsync1
PKGFILES_CSWlibrsync1 += $(call baseisadirs,$(libdir),librsync\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibrsync1 += $(DESCRIPTION), librsync.so.1

PACKAGES += CSWlibrsync-dev
PKGFILES_CSWlibrsync-dev = $(PKGFILES_DEVEL)
SPKG_DESC_CSWlibrsync-dev += Development files for librsync
RUNTIME_DEP_PKGS_CSWlibrsync-dev += CSWlibrsync1

# This package contains the "rdiff" utility.
PACKAGES += CSWlibrsync
SPKG_DESC_CSWlibrsync += $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWlibrsync += CSWlibrsync1
RUNTIME_DEP_PKGS_CSWlibrsync += CSWlibpopt0eatures=no%extinl

include