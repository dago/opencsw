GARNAME = man2html
GARVERSION = 3.0.1
CATEGORIES = utils

DESCRIPTION = A Unix manpage-to-HTML converter
define BLURB
  A Unix manpage-to-HTML converter.
endef

MASTER_SITES = http://hydra.nac.uci.edu/indiv/ehood/tar/
DISTNAME = $(GARNAME)$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://hydra.nac.uci.edu/indiv/ehood/man2html.html

REQUIRED_PKGS = CSWperl

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

ARCHALL = 1

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	cd $(WORKSRC) && perl install.me -batch \
		-binpath $(DESTDIR)$(bindir) \
		-manpath $(DESTDIR)$(mandir) \
		-perlpath $(bindir)/perl
	ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	cd $(WORKSRC) && ginstall \
		README CHANGES \
		doc/man2html.ps doc/man2html.html doc/man2html.txt \
		$(DESTDIR)$(docdir)/$(GARNAME)
	ginstall -d $(DESTDIR)$(sharedstatedir)/www/$(GARNAME)/cgi-bin
	cd $(WORKSRC) && ginstall man.cgi \
		$(DESTDIR)$(sharedstatedir)/www/$(GARNAME)/cgi-bin
	ginstall -d $(DESTDIR)/opt/csw/apache2/share/cgi-bin
	gln -s ../../../share/www/$(GARNAME)/cgi-bin/man.cgi \
		$(DESTDIR)/opt/csw/apache2/share/cgi-bin/man.cgi
	@$(MAKECOOKIE)
