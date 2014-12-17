# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME    = npth
VERSION = 1.1
GARTYPE = v2

DESCRIPTION = The New GNU Portable Threads Library
define BLURB
  This is a library to provide the GNU Pth API and thus a
  non-preemptive threads implementation.
  In contrast to GNU Pth is is based on the system's standard threads
  implementation.  This allows the use of libraries which are not
  compatible to GNU Pth.  Experience with a Windows Pth emulation
  showed that this is a solid way to provide a co-routine based
  framework.
endef

GARCOMPILER = GCC4

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/npth/
DISTFILES  = $(DISTNAME).tar.bz2

BUILD64 = 1

PACKAGES += CSWlibnpth0
CATALOGNAME_CSWlibnpth0 = libnpth0
PKGFILES_CSWlibnpth0 += $(call baseisadirs,$(libdir),libnpth\.so\.0\.0\.4)
PKGFILES_CSWlibnpth0 += $(call baseisadirs,$(libdir),libnpth\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibnpth0 += $(DESCRIPTION), libnpth.so.0
RUNTIME_DEP_PKGS_CSWlibnpth0 += CSWlibgcc-s1


PACKAGES += CSWnpth-dev
CATALOGNAME_CSWnpth-dev = npth_dev
SPKG_DESC_CSWnpth-dev = Development files for libnpth.so.0
PKGFILES_CSWnpth-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWnpth-dev += CSWlibnpth0

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_CFLAGS = -std=c99

include gar/category.mk

