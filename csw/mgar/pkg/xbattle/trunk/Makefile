# $Id$
NAME = xbattle
VERSION = 5.4.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A multi-player real time strategy game
define BLURB
endef

MASTER_SITES = ftp://ftp.uni-frankfurt.de/pub/Mirrors2/gentoo.org/distfiles/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = COPYRIGHT

CONFIGURE_SCRIPTS = $(WORKSRC)/Imakefile
TEST_SCRIPTS =
INSTALL_ARGS = install install.man

INSTALL_OVERRIDE_VARS = BINDIR MANPATH
INSTALL_OVERRIDE_VAR_BINDIR = $(bindir)
INSTALL_OVERRIDE_VAR_MANPATH = $(mandir)

include gar/category.mk

post-extract-modulated:
	-perl -npe 's,/export/home/lesher/xbos,/opt/csw/share/xbattle/xbos,; \
		s,/export/home/lesher/xbts,/opt/csw/share/xbattle/xbts,; \
		s,/export/home/lesher/xbas,/opt/csw/share/xbattle/xbas,' \
		-i $(WORKSRC)/Imakefile
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)$(sharedstatedir)/xbattle
	cd $(WORKSRC) && cp -r xbos xbts xbas $(DESTDIR)$(sharedstatedir)/xbattle/
	ginstall -d $(DESTDIR)$(docdir)/xbattle
	cd $(WORKSRC) && cp -rp tutorial1 tutorial2 README $(DESTDIR)$(docdir)/xbattle
	@$(MAKECOOKIE)
