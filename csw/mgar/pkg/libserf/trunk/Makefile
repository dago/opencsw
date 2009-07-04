GARNAME = libserf
GARVERSION = 0.3.0
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

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(DISTNAME)-(\d+(?:\.\d+)*).tar.bz2

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

DEPENDS = server/apache2rt

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(prefix)/apache2/bin/apr-config
CONFIGURE_ARGS += --with-apr-util=$(prefix)/apache2/bin/apu-config

TEST_TARGET = check
include gar/category.mk

EXTRA_LDFLAGS = -R/opt/csw/bdb44/lib
APR_LIBTOOL = $(shell /opt/csw/apache2/bin/apr-config --apr-libtool)
post-configure-modulated:
	gcp $(APR_LIBTOOL) $(WORKSRC)
	perl -i -pne 's|$(APR_LIBTOOL)|$(abspath $(WORKSRC)/libtool)|' $(WORKSRC)/Makefile
	$(GARBIN)/fixlibtool $(WORKSRC)
	@$(MAKECOOKIE)
