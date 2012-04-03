NAME = pdns
VERSION = 3.0.1
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = An advanced DNS server with multiple backends
define BLURB
  PowerDNS is an advanced DNS server, which allows for several different
  backends. Current backends include MySQL, PostgreSQL, bind, etc.
endef

# XXX: Open Issues:
# - build recursor

MASTER_SITES = http://downloads.powerdns.com/releases/
SPKG_SOURCEURL = http://www.powerdns.com/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += LICENSE
DISTFILES += cswpdns
PATCHFILES += 0003-Make-checking-for-LUA-behave-correctly.patch
PATCHFILES += 0004-Use-sys-isa_defs.h-instead-of-endian.h.patch
PATCHFILES += 0005-Include-correct-sys-ethernet.h.patch

WORKSRC = $(WORKDIR)/$(NAME)-$(VERSION)

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CATALOGNAME = powerdns
LICENSE = $(FILEDIR)/LICENSE

GARCOMPILER = GNU
#PACKAGING_PLATFORMS +=  solaris9-sparc solaris9-i386
#PACKAGING_PLATFORMS +=  solaris10-sparc solaris10-i386
PACKAGING_PLATFORMS +=  solaris10-i386

# PowerDNS does not have any "test" target
SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/$(prefix)/pdns
CONFIGURE_ARGS += --disable-recursor
CONFIGURE_ARGS += --with-lua=no
CONFIGURE_ARGS += --with-boost=/opt/csw/gxx
CONFIGURE_ARGS += --with-mysql=$(prefix)
CONFIGURE_ARGS += --with-mysql-lib=$(prefix)/lib
CONFIGURE_ARGS += --with-mysql-includes=$(prefix)/include/mysql
EXTRA_INC = /opt/csw/gxx/include
LDFLAGS += -L/opt/csw/gxx/lib

RUNTIME_DEP_PKGS_CSWpdns += CSWzlib
RUNTIME_DEP_PKGS_CSWpdns += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpdns += CSWlibmysqlclient15
RUNTIME_DEP_PKGS_CSWpdns += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWpdns += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWpdns += CSWlibboost-prog-opts1-49-0-gxx
RUNTIME_DEP_PKGS_CSWpdns += CSWlibboost-s13n1-49-0-gxx
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
