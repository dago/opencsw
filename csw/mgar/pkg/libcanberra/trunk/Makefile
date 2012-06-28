# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libcanberra
VERSION = 0.29
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = XDG sound theme and name specifications

MASTER_SITES = http://0pointer.de/lennart/projects/libcanberra/
DISTFILES  = $(DISTNAME).tar.xz

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWmypkg
SPKG_DESC_CSWmypkg = My package
PKGFILES_CSWmypkg += $(call pkgfiles_lib,libabc.so.1)
PKGFILES_CSWmypkg += $(call baseisadirs,$(bindir),myexec)
PKGFILES_CSWmypkg += $(sysconfdir)/myconf

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
# CONFIGURE_ARGS += cc_cv_LDFLAGS_-Wl,--as-needed=no
# CONFIGURE_ARGS += cc_cv_LDFLAGS_-Wl,--gc-sections=no

include gar/category.mk

