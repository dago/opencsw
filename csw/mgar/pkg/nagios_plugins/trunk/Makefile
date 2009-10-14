GARNAME = nagios-plugins
GARVERSION = 1.4.14
CATEGORIES = apps

DESCRIPTION = plugins for nagios
define BLURB
  Long description
endef

MASTER_SITES = http://surfnet.dl.sourceforge.net/sourceforge/nagiosplug/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

DISTFILES += CSWnagiosp.prototype

PATCHFILES += check_procs.c.diff
PATCHFILES += subst.in.diff
PATCHFILES += pst3.c.diff

PACKAGES = CSWnagiosp
CATALOGNAME_CSWnagiosp = nagios_plugins

REQUIRED_PKGS_CSWnagiosp  = CSWggettextrt CSWiconv CSWlibnet CSWlibpq 
REQUIRED_PKGS_CSWnagiosp += CSWmysql5rt CSWoldaprt CSWosslrt CSWsasl
REQUIRED_PKGS_CSWnagiosp += CSWzlib CSWperl

NOISALIST = 1

CFLAGS += -I /opt/csw/postgresql/include/

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mysql-dir=/opt/csw/mysql5/bin
CONFIGURE_ARGS += --with-pg-dir=/opt/csw/postgresql/include/
CONFIGURE_ARGS += --disable-largefile
CONFIGURE_ARGS += --with-perl=/opt/csw/bin/perl
CONFIGURE_ARGS += --libexecdir=$(prefix)/libexec/nagios-plugins

libexecdir ?= $(prefix)/libexec/nagios-plugins

# Extra libs
EXTRA_LIB += /opt/csw/mysql5/lib/mysql
EXTRA_LIB += /opt/csw/postgresql/lib

# Extra includes
EXTRA_INC = /opt/csw/postgresql/include

TEST_TARGET = 

include gar/category.mk

DOCS = BUGS ChangeLog FAQ README REQUIREMENTS SUPPORT COPYING
DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
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
