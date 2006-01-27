GARNAME = MHonArc
GARVERSION = 2.6.14
CATEGORIES = utils
GARCH = all

DESCRIPTION = mail-to-HTML converter
define BLURB
  MHonArc is a Perl program for converting mail or news messages into HTML
  archives. It can also be used to convert individual messages into HTML
  documents. Other capabilities include robust MIME support and powerful user
  customization features.
endef

MASTER_SITES = http://www.oac.uci.edu/indiv/ehood/tar/
DISTFILES  = $(DISTNAME).tar.bz2
DISTFILES += CSWmhonarc.gspec CSWmhonarc.depend CSWmhonarc.prototype

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include ../category.mk

install-custom:
	@( cd $(WORKSRC) ; perl install.me -batch \
		-prefix $(DESTDIR)$(prefix) \
		-docpath $(DESTDIR)$(docdir)/$(GARNAME) \
		-manpath $(DESTDIR)$(mandir) )
	@echo "Fixing $(DESTDIR) references..."
	@perl -i -plne 's#$(DESTDIR)##g' `find $(DESTDIR)$(prefix) -type f`

