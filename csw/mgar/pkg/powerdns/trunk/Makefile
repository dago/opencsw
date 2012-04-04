# PowerDNS
# $Id$
#
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
PATCHFILES += 0001-Make-checking-for-LUA-behave-correctly.patch
PATCHFILES += 0002-Use-sys-isa_defs.h-instead-of-endian.h.patch
PATCHFILES += 0003-Include-correct-sys-ethernet.h.patch
PATCHFILES += 0004-Build-only-stub-LUA-pdns-recursor-implementation.-Do.patch
PATCHFILES += 0005-Use-correct-namespace-for-timegm.patch
PATCHFILES += 0006-Use-also-llber-with-lldap.patch

WORKSRC = $(WORKDIR)/$(NAME)-$(VERSION)

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

LICENSE = $(FILEDIR)/LICENSE
PACKAGING_PLATFORMS +=  solaris10-i386 solaris10-sparc

GARCOMPILER = GNU
NORUNPATH = 1

REINPLACEMENTS += usrlocaletc
REINPLACE_MATCH_usrlocaletc = /usr/local/etc
REINPLACE_WITH_usrlocaletc = /etc$(prefix)/pdns
REINPLACE_FILES_usrlocaletc = pdns/pdns.conf-dist

REINPLACEMENTS += usrlocallib
REINPLACE_MATCH_usrlocallib = /usr/local/lib
REINPLACE_WITH_usrlocallib = $(prefix)/lib/pdns
REINPLACE_FILES_usrlocallib = pdns/pdns.conf-dist

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/$(prefix)/pdns
CONFIGURE_ARGS += --libdir=$(prefix)/lib/pdns
CONFIGURE_ARGS += --disable-recursor
CONFIGURE_ARGS += --with-lua=no
CONFIGURE_ARGS += --with-boost=/opt/csw/gxx
CONFIGURE_ARGS += --with-mysql=$(prefix)
CONFIGURE_ARGS += --with-mysql-lib=$(prefix)/lib
CONFIGURE_ARGS += --with-mysql-includes=$(prefix)/include
CONFIGURE_ARGS += --with-modules="ldap geo gmysql"

# Prepend Boost 1.49 installation in paths so we pick up the correct one
EXTRA_INC = /opt/csw/gxx/include
LDFLAGS += -L/opt/csw/gxx/lib

# PowerDNS does not have any "test" target
SKIPTEST = 1

PACKAGES = CSWpdns
CATALOGNAME_CSWpdns = powerdns
SPKG_DESC_CSWpdns = PowerDNS
RUNTIME_DEP_PKGS_CSWpdns += CSWlibz1
RUNTIME_DEP_PKGS_CSWpdns += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpdns += CSWlibmysqlclient15
RUNTIME_DEP_PKGS_CSWpdns += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWpdns += CSWlibboost-prog-opts1-49-0-gxx
RUNTIME_DEP_PKGS_CSWpdns += CSWlibboost-s13n1-49-0-gxx
RUNTIME_DEP_PKGS_CSWpdns += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWpdns += CSWlibldap-r2-4-2
BUILD_DEP_PKGS  = CSWmysql-dev CSWboostdevel

# These are not errors!
CHECKPKG_OVERRIDES_CSWpdns += catalogname-does-not-match-pkgname|pkgname=CSWpdns|catalogname=powerdns|expected-catalogname=pdns

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
