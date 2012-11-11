# $Id$
NAME = ascii
VERSION = 3.11
GARTYPE = v2

DESCRIPTION = Interactive ASCII name and synonym chart
define BLURB
endef

MASTER_SITES = http://www.catb.org/~esr/ascii/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Do-not-use-stdbool.h.patch
PATCHFILES += 0002-Honour-CFLAGS.patch

# No funky configure
CONFIGURE_SCRIPTS =

# No test script
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/ascii $(DESTDIR)$(bindir)/ascii
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/ascii.1 $(DESTDIR)$(mandir)/man1/ascii.1
	@$(MAKECOOKIE)
