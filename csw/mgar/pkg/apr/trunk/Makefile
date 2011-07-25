NAME = apr
VERSION = 1.4.5
CATEGORIES = lib

DESCRIPTION = Apache Portable Runtime
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES = http://apache.crihan.fr/dist/apr/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = LICENSE

PACKAGES += CSWlibapr1-0
SPKG_DESC_CSWlibapr1-0 = Apache portable runtime, libapr-1.so.0
PKGFILES_CSWlibapr1-0 += $(call pkgfiles_lib,libapr-1.so.0)
OBSOLETED_BY_CSWlibapr1-0 = CSWapr

PACKAGES += CSWlibapr-dev
SPKG_DESC_CSWlibapr-dev = Development file for libapr-1.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibapr-dev += CSWlibapr1-0

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-other-child
CONFIGURE_ARGS += --with-installbuilddir=$(datadir)/$(MM_BINDIR)/build-1

MERGEBASE_/opt/csw/share/sparcv9 = $(datadir)
MERGEBASE_/opt/csw/share/amd64= $(datadir)
EXTRA_MERGE_DIRS_isa-extra = $(abspath $(datadir)/$(MM_BINDIR))

include gar/category.mk

post-install-modulated:
	perl -pi -e 's,/usr/local/lib,$(libdir),g' \
		$(DESTDIR)$(datadir)/$(MM_BINDIR)/build-1/libtool
