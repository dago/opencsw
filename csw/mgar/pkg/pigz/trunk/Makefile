GARNAME = pigz
GARVERSION = 2.1.5
CATEGORIES = utils

DESCRIPTION = A parallel implementation of gzip
define BLURB
  pigz, which stands for parallel implementation of gzip, is a fully
  functional replacement for gzip that exploits multiple processors
  and multiple cores to the hilt when compressing data. pigz was written
  by Mark Adler, and uses the zlib and pthread libraries.
endef

MASTER_SITES = http://www.zlib.net/pigz/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

SPKG_SOURCEURL = http://www.zlib.net/pigz/

LICENSE = README

REQUIRED_PKGS = CSWzlib

REQUESTED_ISAS = $(ISALIST_$(GARCOMPILER))

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

include gar/category.mk

build-custom:
	cd $(WORKSRC) && $(CC) $(CFLAGS) -c yarn.c
	cd $(WORKSRC) && $(CC) $(CFLAGS) -c pigz.c
	cd $(WORKSRC) && $(CC) $(LDFLAGS) -o pigz yarn.o pigz.o -lpthread -lz
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/pigz $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/pigz.1 $(DESTDIR)$(mandir)/man1
	ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	ginstall $(WORKSRC)/pigz.pdf $(DESTDIR)$(docdir)/$(GARNAME)
	@$(MAKECOOKIE)
