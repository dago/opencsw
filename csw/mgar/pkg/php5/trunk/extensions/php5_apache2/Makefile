PHP5EXT_NAME = ap2_modphp5

PACKAGES += CSWap2modphp5

CATALOGNAME_CSWap2modphp5 = ap2_modphp5
SPKG_DESC_CSWap2modphp5 = PHP 5 - Apache 2.2.x Module
REQUIRED_PKGS_CSWap2modphp5  = CSWphp5 CSWap2prefork CSWiconv 
REQUIRED_PKGS_CSWap2modphp5 += CSWexpat CSWlibxml2 CSWzlib

DISTFILES += CSWap2modphp5.preremove httpd-php5.conf.CSW
DISTFILES += CSWap2modphp5.postinstall CSWap2modphp5.space

STRIP_DIRS += $(DESTDIR)$(prefix)/apache2/libexec

PKGFILES_CSWap2modphp5 = .*/csw/apache2/.*

## This is configured in a post-install from the main Makefile
