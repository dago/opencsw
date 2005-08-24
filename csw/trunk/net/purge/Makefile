GARNAME = purge
GARVERSION = 20040201
CATEGORIES = net

SPKG_PKGNAME = CSWpurge
SPKG_BITNAME = purge

DESCRIPTION = Purge squid cache entries.
define BLURB
  The purge tool is a kind of magnifying glass into your squid-2 cache. You
  can use purge to have a look at what URLs are stored in which file within
  your cache. The purge tool can also be used to release objects which URLs
  match user specified regular expressions.
endef

MASTER_SITES = http://www.wa.apana.org.au/~dean/sources/
DISTFILES = $(GARNAME)-$(GARVERSION)-src.tar.gz
WORKSRC = $(WORKDIR)/$(GARNAME)

# Build with SunONE
PATCHFILES  = suncc.diff
# ISO C++ says strstr returns a const char*
PATCHFILES += isocc.diff

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include ../category.mk

install-custom:
	@install -m 755 $(WORKSRC)/$(GARNAME) $(DESTDIR)$(sbindir)
