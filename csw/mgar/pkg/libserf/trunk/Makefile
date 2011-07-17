NAME = libserf
VERSION = 1.0.0
DISTNAME = serf-$(VERSION)
CATEGORIES = lib

DESCRIPTION = HTTP client library built on APR, multiplexes connections
define BLURB
    The serf library is a C-based HTTP client library built upon the
    Apache Portable Runtime (APR) library. It multiplexes connections,
    running the read/write communication asynchronously. Memory copies
    and transformations are kept to a minimum to provide high performance
    operation.
endef

MASTER_SITES = http://serf.googlecode.com/files/
DISTFILES  = $(DISTNAME).tar.bz2
LICENSE = LICENSE
VENDOR_URL = http://code.google.com/p/serf/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = serf-(\d+(?:\.\d+)*).tar.bz2

PACKAGES += CSWlibserf1-0
CATALOGNAME_CSWlibserf1-0 = libserf1_0
SPKG_DESC_CSWlibserf1-0 += HTTP client library built on APR, multiplexes connections, provides libserf-1.so.0
DEP_PKGS = CSWapr CSWapr-util CSWbdb48 CSWlibexpat1 CSWiconv CSWoldaprt CSWosslrt CSWzlib

OBSOLETED_BY_CSWlibserf1-0 = CSWlibserf-devel

# Make sure the current directory comes before everything else
INCLUDE_FLAGS = -I. -I$(includedir)

EXTRA_LIB = $(prefix)/bdb48/lib

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(bindir)/apr-1-config
CONFIGURE_ARGS += --with-apr-util=$(bindir)/apu-1-config

TEST_TARGET = check

CHECKPKG_OVERRIDES_CSWlibserf1-0 += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libserf-0.so
CHECKPKG_OVERRIDES_CSWlibserf1-0 += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libserf-1.so
CHECKPKG_OVERRIDES_CSWlibserf1-0 += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libserf-1.so

# overrides which whould not be necessary, as the package is obsoleted by this one
CHECKPKG_OVERRIDES_CSWlibserf1-0 += file-collision|/opt/csw/include/serf_bucket_util.h|CSWlibserf-devel|CSWlibserf1-0
CHECKPKG_OVERRIDES_CSWlibserf1-0 += file-collision|/opt/csw/include/serf_declare.h|CSWlibserf-devel|CSWlibserf1-0
CHECKPKG_OVERRIDES_CSWlibserf1-0 += file-collision|/opt/csw/include/serf_private.h|CSWlibserf-devel|CSWlibserf1-0
CHECKPKG_OVERRIDES_CSWlibserf1-0 += file-collision|/opt/csw/include/serf_bucket_types.h|CSWlibserf-devel|CSWlibserf1-0
CHECKPKG_OVERRIDES_CSWlibserf1-0 += file-collision|/opt/csw/include/serf.h|CSWlibserf-devel|CSWlibserf1-0
CHECKPKG_OVERRIDES_CSWlibserf1-0 += file-collision|/opt/csw/lib/libserf-0.so|CSWlibserf-devel|CSWlibserf1-0
CHECKPKG_OVERRIDES_CSWlibserf1-0 += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libserf-0.so
CHECKPKG_OVERRIDES_CSWlibserf1-0 += shared-lib-pkgname-mismatch|sonames=libserf-0.so.0,libserf-1.so.0|pkgname=CSWlibserf1-0|expected=CSWlibserf0|


include gar/category.mk

post-configure-modulated: APR_LIBTOOL = $(shell $(bindir)/apr-1-config --apr-libtool)
post-configure-modulated:
	gcp $(APR_LIBTOOL) $(WORKSRC)
	perl -i -pne 's|$(APR_LIBTOOL)|$(abspath $(WORKSRC)/libtool)|' $(WORKSRC)/Makefile
	$(GARBIN)/fixlibtool $(WORKSRC)
	@$(MAKECOOKIE)
