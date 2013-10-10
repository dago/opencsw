NAME = pigz
VERSION = 2.3.1
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
DISTFILES += pigz-wrapper
DISTFILES += unpigz-wrapper

VENDOR_URL = http://www.zlib.net/pigz/

LICENSE = README

PACKAGES += CSWpigz
SPKG_DESC_CSWpigz = A parallel implementation of gzip
RUNTIME_DEP_PKGS_Ce/doc/pigz/license

# Optimization show effects < 5%
#REQUESTED_ISAS = $(ISALISREINPLACEMENTS += which
REINPLACE_MATCH_which = whereis
REINPLACE_WITH_which = which
REINPLACE_FILES_which += Makefile

EXTRA_CFLAGS = -mt

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_SCRIPTS =

BUILD_OVERRIDE_VARS += CC CFLAGS
BUILD_OVERRIDE_VAR_CC += $(CC) $(LDFLAGS) -lm -lpthread
BUILD_OVERRIDE_VAR_CFLAGS += $(CFLAGS)

TEST_TARGET = test

INSTALL_SCRIPTS = custom

include gar/category.mk-lz
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
	ginstall $(WORKSRC)/pigz.pdf $(DESTDIR)$(docdir)/$(NAM