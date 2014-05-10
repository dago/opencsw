NAME = phpsysinfo
VERSION = 3.1.12
GARTYPE = v2

DESCRIPTION = Displays information about the host being accessed
define BLURBhost being acceECTssed
endef

SF_PROJ = $(NAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWphpsysinfo
CATALOGNAME_CSWphpsysinfo = phpsysinfo
SPKG_DESC = $(DESCRIPTION)
SPKG_SOURCEURL = http://phpsysinfo.sourceforge.net

RUNTIME_DEP_PKGS  = CSWapache2
RUNTIME-modphp5
RUNTIME_DEP_PKGS += CSWphp5
RUNTIME_DEP_PKGS += CSWphp5-mbstring
RUNTIME_DEP_PKGS += CSWphp5-dom+= CSWphp5-mbstring

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALLEXTRA_MERGE_EXCLUDE_FILES += .*/.git/.* .*/.git .*/.gitignore

SAMPLECONF = .*phpsysinfo.iniCONF = .*config.php

CHECKPKG_OVERRIDES_CSWphpsysinfo += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphpsysinfo += surplu-s-dependency|CSWap2modphp5
CHECKPKG_OVERRIDES_CSWphpsysinfo += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDEsurplus-dependency|CSWphp5-mbstringoCHECKPKG_OVERRIDES_CSWphpsysinfo += surplus-dependency|CSWphp5-domonFunctions.inc.php

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)$(prefix)/share/www/phpsysinfo
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -d $(DESTDIR)$(prefix)/share/www
	@cp -R $(WORKSRC) $(DESTDIR)$(prefix)/share/www/phpsysinfo
	@( cd $(DESTDIR)$(prefix)/share/www/phpphpsysinfo.ini.new phpsysinfo.ini ; \
	   mv COPYING $(DESTDIR)$(docdir)/$(NAME)/license )
	@$(MAKECOOKIE)
