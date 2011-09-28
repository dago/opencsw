NAME = pcp
VERSION = 1.10
CATEGORIES = net

DESCRIPTION = Maps ports to PIDs and vice versa
define BLURB
  Maps ports to PIDs and vice versa
endef

MASTER_SITES = http://www.unix.ms/pcp/
DISTFILES    = pcp.txt
DISTFILES   += COPYING

PACKAGES                   = CSWpidconport
CATALOGNAME                = pidconport
SPKG_DESC_CSWpidconport    = $(DESCRIPTION)
OBSOLETED_BY_CSWpidconport = CSWpcp

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = custom

include gar/category.mk

post-extract-modulated: FOUND_VERSION=$(shell perl -n -e 'print $$1 if( /^# v(\d+\.\d+)/ );' $(WORKDIR)/pcp.txt)
post-extract-modulated:
	@echo " ==> Checking version of $(NAME)"
	$(if $(filter $(VERSION),$(FOUND_VERSION)),,$(error Packaging up $(VERSION) but pcp.txt is $(FOUND_VERSION)))

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)$(bindir)
	@ginstall -m 755 $(WORKDIR)/pcp.txt $(DESTDIR)$(bindir)/pidconport
	@$(MAKECOOKIE)
