GARNAME = mharc
GARVERSION = 0.7.3
CATEGORIES = utils
GARCH = all

DESCRIPTION = Perl scripts for generating web-based mail archives
define BLURB
  mharc is part of the MHonArc Project. mharc is a collection of Perl scripts
  for generating and managing web-based searchable mail archives.
endef

MASTER_SITES = http://www.mhonarc.org/release/mharc/tar/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += CSWmharc.gspec CSWmharc.depend CSWmharc.prototype
DISTFILES += CSWmharc.postinstall CSWmharc.space

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@( cd $(WORKSRC) ; perl install.pl -batch \
		-path $(DESTDIR)$(prefix)/mharc -url "" )
	@echo "Fixing $(DESTDIR) references..."
	@perl -i -plne 's#$(DESTDIR)##g' `find $(DESTDIR)$(prefix) -type f`

