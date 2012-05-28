NAME = nagios-plugins
VERSION = 1.4.15
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Plugins for nagios
define BLURB
   Plugins for Nagios
endef

MASTER_SITES = http://surfnet.dl.sourceforge.net/sourceforge/nagiosplug/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES += CSWnagiosp
SPKG_CATALOG_NAME_CSWnagiosp = nagios_plugins

PATCHFILES += check_procs.c.diff
PATCHFILES += subst.in.diff
PATCHFILES += pst3.c.diff
PATCHFILES += 0004-Use-32-bit-pst3-on-Solaris.patch

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
CONFIGURE_ARGS += --with-perl=/opt/csw/bin/perl

CFLAGS += -I /opt/csw/postgresql/include/
EXTRA_INC = /opt/csw/postgresql/include
EXTRA_LIB += /opt/csw/postgresql/lib

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

RUNTIME_DEP_PKGS_CSWnagiosp += CSWlibintl8 CSWlibpq5
RUNTIME_DEP_PKGS_CSWnagiosp += CSWlibmysqlclient15 CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWnagiosp += CSWlibz1 CSWperl CSWliblber2-4-2 CSWlibldap2-4-2

BUILD_DEP_PKGS_CSWnagiosp += CSWmysql-dev
BUILD_DEP_PKGS_CSWnagiosp += CSWpostgresql-dev
BUILD_DEP_PKGS_CSWnagiosp += CSWlibz-dev
BUILD_DEP_PKGS_CSWnagiosp += CSWlibnet-dev

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
	@$(foreach PLUGIN,$(ROOT_PLUGINS),ginstall -m 744 $(WORKSRC)/plugins-root/$(PLUGIN) $(PLUGINDEST);)
	@tar cf $(WORKSRC)/contrib.tar $(WORKSRC)/contrib/
	@ginstall -m 755 -d $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/contrib.tar $(DOCDEST)
	@$(MAKECOOKIE)

post-merge:
	@rm $(PKGROOT)$(libdir)/charset.alias
	@$(MAKECOOKIE)

