NAME = pdns
VERSION = 2.9.22
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
PATCHFILES += 0001-stdint.h-patch.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CATALOGNAME = powerdns
LICENSE = $(FILEDIR)/LICENSE

GARCOMPILER = GCC3
PACKAGING_PLATFORMS +=  solaris9-sparc solaris9-i386
SKIPTEST = 1
EXTRA_LD_OPTIONS = -R/opt/csw/mysql5/lib/mysql

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw/pdns
CONFIGURE_ARGS += --with-mysql=/opt/csw/mysql5

RUNTIME_DEP_PKGS_CSWpdns += CSWzlib
RUNTIME_DEP_PKGS_CSWpdns += CSWgcc3core
RUNTIME_DEP_PKGS_CSWpdns += CSWgcc3g++
RUNTIME_DEP_PKGS_CSWpdns += CSWmysql5rt

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
