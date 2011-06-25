NAME = phpsysinfo
VERSION = 3.0.11
CATEGORIES = utils

DESCRIPTION = Displays information about the host being accessed
define BLURB
  Displays information about the host being accessed
endef

SF_PROJ = $(NAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWphpsysinfo
CATALOGNAME_CSWphpsysinfo = phpsysinfo
SPKG_DESC = $(DESCRIPTION)
SPKG_SOURCEURL = http://phpsysinfo.sourceforge.net

RUNTIME_DEP_PKGS = CSWapache2 CSWap2modphp5 CSWphp5

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

WORKSRC = $(WORKDIR)/$(NAME)

SAMPLECONF = .*config.php

CHECKPKG_OVERRIDES_CSWphpsysinfo += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphpsysinfo += surplus-dependency|CSWap2modphp5
CHECKPKG_OVERRIDES_CSWphpsysinfo += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWphpsysinfo += file-with-bad-content|/usr/local|root/opt/csw/share/www/phpsysinfo/includes/class.CommonFunctions.inc.php

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)$(prefix)/share/www/phpsysinfo
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -d $(DESTDIR)$(prefix)/share/www
	@cp -R $(WORKSRC) $(DESTDIR)$(prefix)/share/www/phpsysinfo
	@( cd $(DESTDIR)$(prefix)/share/www/phpsysinfo ; \
	   mv config.php.new config.php ; \
	   mv COPYING $(DESTDIR)$(docdir)/$(NAME)/license )
#	@( cd $(DESTDIR)$(prefix)/share/www/phpsysinfo/includes/os ; \
#	   gpatch < ../../../../../../../../../$(FILEDIR)/CSWphpsysinfo.class.SunOS.inc.php.p )
	@$(MAKECOOKIE)
