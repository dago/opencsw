NAME = pigz
VERSION = 2.1.7
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A parallel implementation of gzip
define BLURB
  pigz, which stands for parallel implementation of gzip, is a fully
  functional replacement for gzip that exploits multiple processors
  and multiple cores to the hilt when compressing data. pigz was written
  by Mark Adler, and uses the zlib and pthread libraries.
endef

MASTER_SITES = http://www.zlib.net/pigz/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTNAME = $(NAME)
DISTFILES += pigz-wrapper
DISTFILES += unpigz-wrapper

VENDOR_URL = http://www.zlib.net/pigz/

LICENSE = README

PACKAGES += CSWpigz
SPKG_DESC_CSWpigz = A parallel implementation of gzip
RUNTIME_DEP_PKGS_CSWpigz += CSWlibz1
# This is just the license
CHECKPKG_OVERRIDES_CSWpigz += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pigz/license

# Optimization show effects < 5%
#REQUESTED_ISAS = $(ISALIST_$(GARCOMPILER))

EXTRA_CFLAGS = -mt

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

include gar/category.mk

build-custom:
	cd $(WORKSRC) && $(CC) $(CPPFLAGS) $(CFLAGS) -c yarn.c
	cd $(WORKSRC) && $(CC) $(CPPFLAGS) $(CFLAGS) -c pigz.c
	cd $(WORKSRC) && LD_OPTIONS="$(LD_OPTIONS)" $(CC) $(LDFLAGS) -o pigz yarn.o pigz.o -lpthread -lz
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKDIR)/pigz-wrapper $(DESTDIR)$(bindir)/pigz
	ginstall $(WORKDIR)/unpigz-wrapper $(DESTDIR)$(bindir)/unpigz
	ginstall -d $(DESTDIR)$(libexecdir)
	ginstall $(WORKSRC)/pigz $(DESTDIR)$(libexecdir)
	cd $(DESTDIR)$(libexecdir) && gln pigz unpigz
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/pigz.1 $(DESTDIR)$(mandir)/man1
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	ginstall $(WORKSRC)/pigz.pdf $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)
