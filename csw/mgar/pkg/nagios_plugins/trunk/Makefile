NAME = nagios-plugins
VERSION = 1.4.15
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = plugins for nagios
define BLURB
  Long description
endef

MASTER_SITES = http://surfnet.dl.sourceforge.net/sourceforge/nagiosplug/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += check_procs.c.diff
PATCHFILES += subst.in.diff
PATCHFILES += pst3.c.diff
PATCHFILES += 0004-Use-32-bit-pst3-on-Solaris.patch

PACKAGES = CSWnagiosp
CATALOGNAME_CSWnagiosp = nagios_plugins

RUNTIME_DEP_PKGS_CSWnagiosp  = CSWggettextrt CSWlibcharset1 CSWlibiconv2 CSWlibnet1 CSWlibpq5
RUNTIME_DEP_PKGS_CSWnagiosp += CSWlibmysqlclient15 CSWoldaprt CSWlibssl1-0-0 CSWsasl
RUNTIME_DEP_PKGS_CSWnagiosp += CSWlibz1 CSWperl

BUILD_DEP_PKGS_CSWnagiosp += CSWmysql-dev
BUILD_DEP_PKGS_CSWnagiosp += CSWpostgresql-dev
BUILD_DEP_PKGS_CSWnagiosp += CSWlibz-dev
BUILD_DEP_PKGS_CSWnagiosp += CSWlibnet-dev
BUILD_DEP_PKGS_CSWnagiosp += CSWlibiconv-dev

NOISALIST = 1

CFLAGS += -I /opt/csw/postgresql/include/

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=/opt/csw
CONFIGURE_ARGS += --with-trusted-path=/bin:/sbin:/usr/bin:/usr/sbin:/opt/csw/bin:/opt/csw/sbin
CONFIGURE_ARGS += --with-mysql-dir=/opt/csw
CONFIGURE_ARGS += --with-pg-dir=/opt/csw/postgresql/include/
CONFIGURE_ARGS += --disable-largefile
CONFIGURE_ARGS += --with-perl=/opt/csw/bin/perl
CONFIGURE_ARGS += --libexecdir=$(prefix)/libexec/nagios-plugins

libexecdir ?= $(prefix)/libexec/nagios-plugins

# Extra libs
EXTRA_LIB += /opt/csw/postgresql/lib

# Extra includes
EXTRA_INC = /opt/csw/postgresql/include

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
