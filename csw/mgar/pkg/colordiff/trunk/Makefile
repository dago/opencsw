GARNAME = colordiff
GARVERSION = 1.0.9
CATEGORIES = utils

DESCRIPTION = Wrapper for for the diff command producing colored output
define BLURB
endef

MASTER_SITES = http://colordiff.sourceforge.net/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = fix-entity-nesting.patch
PATCHFILES += force-csw-perl.patch
PATCHFILES += force-csw-less.patch
PATCHFILES += force-csw-gdiff.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWdiffutils CSWperl CSWless

CONFIGURE_SCRIPTS = 
BUILD_ARGS = doc
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

sysconfdir = /etc/opt/csw
PRESERVECONF = $(sysconfdir)/colordiffrc

ARCHALL = 1

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(docdir)
	(cd $(WORKSRC) && ginstall BUGS CHANGES INSTALL README TODO $(DESTDIR)$(docdir))
	ginstall -d $(DESTDIR)$(mandir)/man1
	(cd $(WORKSRC) && ginstall cdiff.1 colordiff.1 $(DESTDIR)$(mandir)/man1)
	ginstall -d $(DESTDIR)$(sysconfdir)
	(cd $(WORKSRC) && ginstall colordiffrc colordiffrc-lightbg $(DESTDIR)$(sysconfdir))
	ginstall -d $(DESTDIR)$(bindir)
	sed -e "s%/etc%$(sysconfdir)%g" $(WORKSRC)/colordiff.pl >$(DESTDIR)$(bindir)/colordiff
	chmod 755 $(DESTDIR)$(bindir)/colordiff
	ginstall $(WORKSRC)/cdiff.sh $(DESTDIR)$(bindir)/cdiff
	@$(MAKECOOKIE)
