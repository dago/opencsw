# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = bsdiff
VERSION = 4.3
GARTYPE = v2

DESCRIPTION = Binary diff/patch utility
define BLURB
endef

MASTER_SITES = http://www.daemonology.net/bsdiff/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += COPYING

PATCHFILES += 0001-Add-substitutes-for-err-errx-warn-warnx.patch

PACKAGES += CSWbsdiff
SPKG_DESC_CSWmypkg = Binary diff/patch utility
# PKGFILES is catchall

EXTRA_CFLAGS += -I.

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	cd $(WORKSRC) && $(CC) $(CFLAGS) -lbz2 -o bsdiff bsdiff.c err.c
	cd $(WORKSRC) && $(CC) $(CFLAGS) -lbz2 -o bspatch bspatch.c err.c
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/bsdiff $(DESTDIR)$(bindir)/bsdiff
	ginstall -m 755 $(WORKSRC)/bspatch $(DESTDIR)$(bindir)/bspatch
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -m 755 $(WORKSRC)/bsdiff.1 $(DESTDIR)$(mandir)/man1/bsdiff.1
	ginstall -m 755 $(WORKSRC)/bspatch.1 $(DESTDIR)$(mandir)/man1/bspatch.1
	@$(MAKECOOKIE)

