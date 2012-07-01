NAME = nagios-plugins
VERSION = 1.4.15
CATEGORIES = apps
GARTYPE = v2

SPKG_DESC_CSWnagios-plugins = Plugins for nagios
define BLURB
   Plugins for Nagios
endef

MASTER_SITES = http://surfnet.dl.sourceforge.net/sourceforge/nagiosplug/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES 				= CSWnagios-plugins
SPKG_CATALOG_NAME_CSWnagios-plugins 	= nagios_plugins

OBSOLETED_BY_CSWnagios-plugins	= CSWnagiosp
SPKG_CATALOG_NAME_CSWnagiosp 	= nagiosp_stub

#PATCHFILES      += 0001-disable-cflags-detection-for-pst3.patch
#PATCHFILES      += 0002-changed-paths-in-hardcoded-examples.patch
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
CONFIGURE_ARGS  += --libexecdir=$(prefix)/libexec/nagios-plugins
CONFIGURE_ARGS += --with-perl=/opt/csw/bin/perl
CONFIGURE_ARGS += --with-openssl=/opt/csw
# http://184.82.236.176/?p=4
#CONFIGURE_ARGS += --with-ps-command="/usr/bin/ps -eo 's uid pid ppid vsz rss pcpu etime comm args'"
#CONFIGURE_ARGS += --with-ps-format="%s %d %d %d %d %d %f %s %s %n"
#CONFIGURE_ARGS += --with-ps-cols=10
#CONFIGURE_ARGS += --with-ps-varlist="procstat,&procuid,&procpid,&procppid,&procvsz,&procrss,&procpcpu,procetime,procprog,&pos"
#
CONFIGURE_ARGS += --with-trusted-path=/usr/bin:/usr/sbin:/opt/csw/bin:/opt/csw/sbin:$(prefix)/libexec/nagios-plugins
CONFIGURE_ARGS += --with-ping6-command="/usr/sbin/ping -a inet6 -s %s 56 %d"

libexecdir 	?= $(prefix)/libexec/nagios-plugins

CFLAGS += -I /opt/csw/postgresql/include/
EXTRA_INC = /opt/csw/postgresql/include
EXTRA_LIB += /opt/csw/postgresql/lib

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWlibintl8 CSWlibpq5
RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWlibmysqlclient18 CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWlibz1 CSWperl CSWliblber2-4-2 CSWlibldap2-4-2

BUILD_DEP_PKGS_CSWnagios-plugins += CSWmysql-dev
BUILD_DEP_PKGS_CSWnagios-plugins += CSWpostgresql-dev
BUILD_DEP_PKGS_CSWnagios-plugins += CSWlibz-dev
BUILD_DEP_PKGS_CSWnagios-plugins += CSWlibnet-dev

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
	@tar cf $(WORKSRC)/contrib.tar $(WORKSRC)/contrib/
	@ginstall -m 755 -d $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/contrib.tar $(DOCDEST)
	@$(MAKECOOKIE)

post-merge:
	@rm $(PKGROOT)$(libdir)/charset.alias
	@$(MAKECOOKIE)

