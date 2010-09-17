GARNAME = libserf
GARVERSION = 0.7.0
DISTNAME = serf-$(GARVERSION)
CATEGORIES = lib

DESCRIPTION = HTTP client library built on APR, multiplexes connections.
define BLURB
    The serf library is a C-based HTTP client library built upon the
    Apache Portable Runtime (APR) library. It multiplexes connections,
    running the read/write communication asynchronously. Memory copies
    and transformations are kept to a minimum to provide high performance
    operation.
endef

MASTER_SITES = http://serf.googlecode.com/files/
DISTFILES  = $(DISTNAME).tar.bz2

RUNTIME_DEP_PKGS_CSWlibserf = CSWapache2rt CSWexpat CSWiconv CSWoldaprt CSWosslrt CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(DISTNAME)-(\d+(?:\.\d+)*).tar.bz2

LICENSE = LICENSE

VENDOR_URL = http://code.google.com/p/serf/

# Make sure the current directory comes before everything else
INCLUDE_FLAGS = -I. -I$(includedir)

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

CONFIGURE_ARGS = $(DIRPATHS)
# CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-apr=$(prefix)/apache2/bin/apr-config
CONFIGURE_ARGS += --with-apr-util=$(prefix)/apache2/bin/apu-config

TEST_TARGET = check

# as long as apache does not depend on apr, serf as well 
# does not depend on it
CHECKPKG_OVERRIDES_CSWlibserf += missing-dependency|CSWapr

include gar/category.mk

APR_LIBTOOL = $(shell /opt/csw/apache2/bin/apr-config --apr-libtool)
post-configure-modulated:
	gcp $(APR_LIBTOOL) $(WORKSRC)
	perl -i -pne 's|$(APR_LIBTOOL)|$(abspath $(WORKSRC)/libtool)|' $(WORKSRC)/Makefile
	$(GARBIN)/fixlibtool $(WORKSRC)
	@$(MAKECOOKIE)
