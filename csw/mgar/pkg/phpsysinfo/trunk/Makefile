GARNAME = phpsysinfo
GARVERSION = 2.5.4
CATEGORIES = utils

DESCRIPTION = displays information about the host being accessed
define BLURB
  displays information about the host being accessed
endef

SF_PROJ = $(GARNAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWphpsysinfo
CATALOGNAME_CSWphpsysinfo = phpsysinfo
SPKG_DESC = $(DESCRIPTION)
SPKG_SOURCEURL = http://phpsysinfo.sourceforge.net

REQUIRED_PKGS = CSWapache2 CSWap2modphp5 CSWphp5 CSWcswclassutils

SPKG_CLASSES_CSWphpsysinfo = none cswcpsampleconf

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

WORKSRC = $(WORKDIR)/$(GARNAME)

PROTOTYPE_FILTER  = awk ' \
$$$$3 ~ /\/config.php.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
{ print }'

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)$(prefix)/share/www/phpsysinfo
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -d $(DESTDIR)$(prefix)/share/www
	@cp -R $(WORKSRC) $(DESTDIR)$(prefix)/share/www/phpsysinfo
	@( cd $(DESTDIR)$(prefix)/share/www/phpsysinfo ; \
	   mv config.php.new config.php.CSW ; \
	   mv COPYING $(DESTDIR)$(docdir)/$(GARNAME)/license )
	@( cd $(DESTDIR)$(prefix)/share/www/phpsysinfo/includes/os ; \
	   gpatch < ../../../../../../../../../$(FILEDIR)/CSWphpsysinfo.class.SunOS.inc.php.p )
	@$(MAKECOOKIE)
