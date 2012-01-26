NAME = par
VERSION = 1.52
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Paragraph reformatter similar to fmt
define BLURB
  par is a paragraph reformatter, vaguely similar to fmt, but better.
endef

MASTER_SITES = http://www.nicemice.net/par/
DISTNAME = Par152
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += $(DISTNAME)-autoconf.tar.gz

LICENSE = par.doc

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	mkdir -p $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/par $(DESTDIR)$(bindir)/par
	mkdir -p $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/par.1 $(DESTDIR)$(mandir)/man1/par.1
	mkdir -p $(DESTDIR)$(docdir)/par
	ginstall $(WORKSRC)/par.doc $(DESTDIR)$(docdir)/par/par.txt
