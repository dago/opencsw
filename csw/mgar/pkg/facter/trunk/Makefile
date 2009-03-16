GARNAME = facter
GARVERSION = 1.5.4
CATEGORIES = apps

DESCRIPTION =	a system fact gatherer
define BLURB
  Long description
endef

MASTER_SITES = http://reductivelabs.com/downloads/facter/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

REQUIRED_PKGS = CSWruby

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL=1

CONFIGURE_SCRIPTS = none
BUILD_SCRIPTS     = none
TEST_SCRIPTS      = none
INSTALL_SCRIPTS   = facter

include gar/category.mk

configure-none:
	@$(MAKECOOKIE)

test-none:
	@$(MAKECOOKIE)

build-none:
	@$(MAKECOOKIE)

install-facter:
	@ginstall -d $(DESTDIR)
	(cd $(WORKDIR)/$(DISTNAME); DESTDIR=$(DESTDIR) ruby install.rb)
