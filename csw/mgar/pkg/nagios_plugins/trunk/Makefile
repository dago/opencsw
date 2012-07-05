# $Id$
#
NAME = nagios-plugins
VERSION = 1.4.15
CATEGORIES = apps
GARTYPE = v2

SPKG_DESC_CSWnagios-plugins = Plugins for nagios
define BLURB
   Plugins for Nagios
endef

SF_PROJ = nagiosplug
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES 			= CSWnagios-plugins
CATALOG_NAME_CSWnagios-plugins 	= nagios_plugins

OBSOLETED_BY_CSWnagios-plugins	= CSWnagiosp
CATALOG_NAME_CSWnagiosp 	= nagiosp_stub

PATCHFILES 	+= 0004-Use-32-bit-pst3-on-Solaris.patch

REINPLACE_USRLOCAL += contrib/*
REINPLACE_USRLOCAL += plugins/*
REINPLACE_USRLOCAL += plugins-scripts/*
REINPLACE_USRLOCAL += ChangeLog
REINPLACE_USRLOCAL += README

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=/opt/csw
CONFIGURE_ARGS += --with-trusted-path=/bin:/sbin:/usr/bin:/usr/sbin:/opt/csw/bin:/opt/csw/sbin
CONFIGURE_ARGS += --with-mysql-dir=/opt/csw
CONFIGURE_ARGS += --with-pg-dir=/opt/csw/postgresql/include/
CONFIGURE_ARGS += --disable-largefile
CONFIGURE_ARGS += --libexecdir=$(prefix)/libexec/nagios-plugins
CONFIGURE_ARGS += --with-perl=/opt/csw/bin/perl
CONFIGURE_ARGS += --with-openssl=/opt/csw
CONFIGURE_ARGS += --with-trusted-path=/usr/bin:/usr/sbin:/opt/csw/bin:/opt/csw/sbin:$(prefix)/libexec/nagios-plugins
CONFIGURE_ARGS += --with-ping6-command="/usr/sbin/ping -A inet6 -s %s 56 %d"
CONFIGURE_ARGS += --with-snmpget-command=/opt/csw/bin/snmpget
CONFIGURE_ARGS += --with-snmpgetnext-command=/opt/csw/bin/snmpgetnext

libexecdir 	?= $(prefix)/libexec/nagios-plugins

EXTRA_INC += /opt/csw/postgresql/include
EXTRA_LIB += /opt/csw/postgresql/lib

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWlibintl8 CSWlibpq5
RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWlibmysqlclient18 CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWlibz1 CSWperl CSWliblber2-4-2 CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWnetsnmp

# Add this override for now
CHECKPKG_OVERRIDES_CSWnagios-plugins += surplus-dependency|CSWnetsnmp

BUILD_DEP_PKGS	+= CSWmysql-dev
BUILD_DEP_PKGS	+= CSWpostgresql-dev
BUILD_DEP_PKGS	+= CSWlibz-dev
BUILD_DEP_PKGS	+= CSWlibnet-dev

TEST_TARGET = 

include gar/category.mk

DOCS = BUGS ChangeLog FAQ README REQUIREMENTS SUPPORT COPYING
DOCDEST = $(DESTDIR)$(docdir)/$(NAME)
ROOT_PLUGINS = check_dhcp check_icmp pst3
PLUGINDEST = $(DESTDIR)$(libexecdir)

post-install-modulated:
	@ginstall -m 755 -d $(DOCDEST)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@ginstall -m 755 -d $(PLUGINDEST)
	@$(foreach PLUGIN,$(ROOT_PLUGINS),ginstall -m 4755 $(WORKSRC)/plugins-root/$(PLUGIN) $(PLUGINDEST);)
	@( cd $(WORKSRC) ; tar cf contrib.tar contrib ; gzip contrib.tar)
	@ginstall -m 755 -d $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/contrib.tar.gz $(DOCDEST)
	@$(MAKECOOKIE)

post-merge:
	@rm $(PKGROOT)$(libdir)/charset.alias
	@$(MAKECOOKIE)

