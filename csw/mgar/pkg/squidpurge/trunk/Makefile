GARNAME = purge
GARVERSION = 20040201
CATEGORIES = net

DESCRIPTION = Purge squid cache entries.
define BLURB
  The purge tool is a kind of magnifying glass into your squid-2 cache. You
  can use purge to have a look at what URLs are stored in which file within
  your cache. The purge tool can also be used to release objects which URLs
  match user specified regular expressions.
endef

BASEURL = http://www.wa.apana.org.au/~dean
SPKG_SRCURL  = $(BASEURL)/squidpurge/
MASTER_SITES = $(BASEURL)/sources/
DISTFILES = $(GARNAME)-$(GARVERSION)-src.tar.gz
WORKSRC = $(WORKDIR)/$(GARNAME)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-src.tar.gz

DISTFILES += $(call admfiles,CSWsquidpurge,prototype copyright)

# Build with SunONE
PATCHFILES  = suncc.diff
# ISO C++ says strstr returns a const char*
PATCHFILES += isocc.diff

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(docdir)/squidpurge $(DESTDIR)$(sbindir)
	@ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(docdir)/squidpurge
	@ginstall -m 755 $(WORKSRC)/purge  $(DESTDIR)$(sbindir)/squidpurge
	@$(MAKECOOKIE)

