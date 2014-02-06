# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = sane-backends
VERSION = 1.0.24
GARTYPE = v2
# CATEGORIES = category

DESCRIPTION = Sane backend
define BLURB
  Long description
endef

# http://sourceforge.net/projects/cupsdriverkodak/files/Scanning%20-%20sane%20backend/sane-backends-1.0.24.tar.gz/download
MASTER_SITES = $(SF_MIRRORS)
SF_PROJECT = cupsdriverkodak
DISTFILES  = $(DISTNAME).tar.gz

# solaris studio does not like __attribute__ and __pack__
GARCOMPILER = GCC4

PACKAGES += CSWlibsane1
CATALOGNAME_CSWlibsane1 = libsane1
PKGFILES_CSWlibsane1 += $(call baseisadirs,$(libdir),libsane\.so\.1\.0\.24)
PKGFILES_CSWlibsane1 += $(call baseisadirs,$(libdir),libsane\.so\.1(\.\d+)*)
PKGFILES_CSWlibsane1 += $(libdir)/sane/libsane.*
PKGFILES_CSWlibsane1 += $(sysconfdir)/sane.d/.*
SPKG_DESC_CSWlibsane1 += $(DESCRIPTION), libsane.so.1
RUNTIME_DEP_PKGS_CSWlibsane1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsane1 += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWlibsane1 += CSWlibjpeg7
CHECKPKG_OVERRIDES_CSWlibsane1 += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWlibsane1 += soname-not-part-of-filename

OBSOLETED_BY_CSWlibsane1 = CSWsaneback

PACKAGES += CSWsane-backends
SPKG_DESC_CSWsane-backends += $(DESCRIPTION), tools and docs
RUNTIME_DEP_PKGS_CSWsane-backends += CSWlibsane1
CHECKPKG_OVERRIDES_CSWsane-backends += file-with-bad-content


PACKAGES += CSWsane-backends-dev
CATALOGNAME_CSWsane-backends-dev = sane_backends_dev
SPKG_DESC_CSWsane-backends-dev += $(DESCRIPTION), development files
PKGFILES_CSWsane-backends-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWsane-backends-dev += CSWlibsane1
OBSOLETED_BY_CSWsane-backends-dev = CSWsaneback

EXTRA_LDFLAGS = -lrt

CONFIGURE_ARGS = $(DIRPATHS)
# option from net-snmp-config --cflags prevents comiling with gcc
CONFIGURE_ARGS += --with-snmp=no

EXTRA_TEST_ENV = PATH=/opt/csw/gnu:$(PATH)
SKIPTEST = 1

include gar/category.mk

