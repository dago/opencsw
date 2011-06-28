NAME = pcp
VERSION = 1.10
CATEGORIES = net

DESCRIPTION = Maps ports to PIDs and vice versa
define BLURB
  Maps ports to PIDs and vice versa
endef

MASTER_SITES = http://www.unix.ms/pcp/
DISTFILES  = pcp.txt
DISTFILES += COPYING

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)$(bindir)
	@ginstall -m 755 $(WORKDIR)/pcp.txt $(DESTDIR)$(bindir)/pidconport
	@$(MAKECOOKIE)
