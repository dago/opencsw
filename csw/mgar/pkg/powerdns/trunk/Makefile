NAME = pdns
VERSION = 3.0.1
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = An advanced DNS server with multiple backends
define BLURB
  PowerDNS is an advanced DNS server, which allows for several different
  backends. Current backends include MySQL, PostgreSQL, bind, etc.
endef

MASTER_SITES = http://downloads.powerdns.com/releases/
SPKG_SOURCEURL = http://www.powerdns.com/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += LICENSE
DISTFILES += cswpdns
# PATCHFILES += 0001-stdint.h-patch.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CATALOGNAME = powerdns
LICENSE = $(FILEDIR)/LICENSE

GARCOMPILER = GNU
# PACKAGING_PLATFORMS +=  solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS +=  solaris10-sparc solaris10-i386
SKIPTEST = 1
BUILD64_ONLY = 1
BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/$(prefix)/pdns
CONFIGURE_ARGS += --with-mysql=$(prefix)
CONFIGURE_ARGS += --with-boost=/opt/csw/gxx

RUNTIME_DEP_PKGS_CSWpdns += CSWzlib
RUNTIME_DEP_PKGS_CSWpdns += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpdns += CSWlibmysqlclient15
RUNTIME_DEP_PKGS_CSWpdns += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWpdns += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWpdns += CSWboostrt
BUILD_DEP_PKGS  = CSWmysql-dev CSWboostdevel

INITSMF = /etc/opt/csw/init.d/cswpdns
PRESERVECONF = /etc/opt/csw/pdns/pdns.conf

post-install-modulated:
	@echo " ==> Installing Init Script"
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswpdns $(DESTDIR)/etc/opt/csw/init.d/cswpdns
	@echo " ==> Moving config file"
	@mv $(DESTDIR)/etc/opt/csw/pdns/pdns.conf-dist $(DESTDIR)/etc/opt/csw/pdns/pdns.conf
	@$(MAKECOOKIE)

include gar/category.mk
