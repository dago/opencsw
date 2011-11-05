# $Id$
NAME = talloc
VERSION = 2.0.7
CATEGORIES = lib

DESCRIPTION = A hierarchical, reference counted memory pool system
define BLURB
endef

MASTER_SITES = http://samba.org/ftp/talloc/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://talloc.samba.org/talloc/doc/html/index.html

LICENSE = NEWS

PACKAGES += CSWlibtalloc2
CATALOGNAME_CSWlibtalloc2 = libtalloc2
SPKG_DESC_CSWlibtalloc2 = A hierarchical, reference counted memory pool system, libtalloc.so.2
PKGFILES_CSWlibtalloc2 += $(call pkgfiles_lib,libtalloc.so.2)

PACKAGES += CSWlibtalloc-dev
CATALOGNAME_CSWlibtalloc-dev = libtalloc_dev
SPKG_DESC_CSWlibtalloc-dev = Development Files for libtalloc
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibtalloc-dev += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibtalloc-dev += CSWpy-talloc

PACKAGES += CSWlibpytalloc-util2
CATALOGNAME_CSWlibpytalloc-util2 = libpytalloc_util2
SPKG_DESC_CSWlibpytalloc-util2 = Python talloc library, libpytalloc-util.so.2
PKGFILES_CSWlibpytalloc-util2 = $(call pkgfiles_lib,libpytalloc-util.so.2)
RUNTIME_DEP_PKGS_CSWlibpytalloc-util2 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibpytalloc-util2 += CSWlibpython2-6-1-0

PACKAGES += CSWpy-talloc
CATALOGNAME_CSWpy-talloc = py_talloc
SPKG_DESC_CSWpy-talloc = Python Bindings for libtalloc
PKGFILES_CSWpy-talloc += $(libdir)/python/.*
RUNTIME_DEP_PKGS_CSWpy-talloc += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWpy-talloc += CSWlibpytalloc-util2
RUNTIME_DEP_PKGS_CSWpy-talloc += CSWlibpython2-6-1-0

PACKAGES += CSWpy-talloc-dev
CATALOGNAME_CSWpy-talloc-dev = py_talloc_dev
SPKG_DESC_CSWpy-talloc-dev = Development Files for libtalloc Python Bindings
PKGFILES_CSWpy-talloc-dev += $(includedir)/pytalloc\.h
PKGFILES_CSWpy-talloc-dev += $(call baseisadirs,$(libdir),libpytalloc-util\.so)
PKGFILES_CSWpy-talloc-dev += $(call baseisadirs,$(libdir),pkgconfig/pytalloc-util\.pc)
RUNTIME_DEP_PKGS_CSWpy-talloc-dev += CSWpython-devel
RUNTIME_DEP_PKGS_CSWpy-talloc-dev += CSWpy-talloc
RUNTIME_DEP_PKGS_CSWpy-talloc-dev += CSWlibpytalloc-util2

BUILD64 = 1
NODIRPATHS = --exec_prefix
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --exec-prefix=$(exec_prefix)

EXTRA_TEST_EXPORTS = LD_LIBRARY_PATH
LD_LIBRARY_PATH=$(abspath $(WORKSRC)/bin/shared)

include gar/category.mk
