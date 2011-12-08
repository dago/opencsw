NAME = ganglia-modules-solaris
VERSION = 1.0
CATEGORIES = utils

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# Hardwired to skip the tests
ifeq ($(VERSION),1.0)
#TEST_TARGET = check
TEST_SCRIPTS = 
endif

DESCRIPTION = Ganglia modules for IO and per-core CPU stats on Solaris
define BLURB
  Ganglia is a distributed architecture for performance metrics.
  These modules provide statistics from IO (disk) activity and 
  individual CPU cores.  The IO module includes read and write
  request rates, average service time and average wait time.
endef

SF_PROJ = gmod-solaris
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += $(PATCHFILES)
DISTNAME = $(NAME)-$(VERSION)

EXTRA_DOCS = $(PATCHFILES)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

BUILD64 = 1

BUILD_DEP_PKGS = CSWlibapr1-0 CSWganglia-dev

RUNTIME_DEP_PKGS = CSWlibapr1-0 CSWgangliaagent CSWlibganglia0

PKGFILES = /opt/csw/lib/ganglia/modio.so
PKGFILES += /opt/csw/lib/ganglia/modmulticpu.so
PKGFILES += /etc/opt/csw/ganglia/conf.d/mod_io.conf.CSW
PKGFILES += /etc/opt/csw/ganglia/conf.d/mod_multicpu.conf.CSW

PRESERVECONF = /etc/opt/csw/ganglia/conf.d/mod_io.conf
PRESERVECONF += /etc/opt/csw/ganglia/conf.d/mod_multicpu.conf

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-nls

include gar/category.mk

post-install-modulated:
	@ginstall -d $(DESTDIR)/etc/opt/csw/ganglia
	cp $(WORKSRC)/conf.d/mod_io.conf $(DESTDIR)/etc/opt/csw/ganglia/mod_io.conf.CSW
	cp $(WORKSRC)/conf.d/mod_multicpu.conf $(DESTDIR)/etc/opt/csw/ganglia/mod_multicpu.conf.CSW

