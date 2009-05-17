GARNAME = pnp
GARVERSION = 0.4.14
CATEGORIES = apps

DESCRIPTION = visualization of nagios performance data using RRD databases
define BLURB
  PNP is an addon to nagios which analyzes performance data provided by plugins and stores them automatically into RRD-databases
endef

SF_PROJ = pnp4nagios
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpnp, prototype )
DISTFILES += cswpnp

PATCHFILES += makefile.diff
PATCHFILES += npcd.c.diff
PATCHFILES += npcdmod.h.diff
PATCHFILES += npcdmod.c.diff
PATCHFILES += npcd.cfg-sample.in.diff
PATCHFILES += nagios_commands.cfg-sample.diff

# We define upstream file regex so we can be notifed of new upstream software release
#UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

NOISALIST = 1

datadir = /opt/csw/nagios/share/pnp
sysconfdir = $(prefix)/nagios/pnp/etc
bindir = $(prefix)/nagios/pnp/bin
libexecdir = $(prefix)/libexec/nagios-plugins
localstatedir =$(prefix)/nagios/pnp/var

REQUIRED_PKGS += CSWphp5 CSWphp5gd CSWap2modphp5 CSWrrd CSWnagios CSWcswclassutils
SPKG_CLASSES = none cswpreserveconf cswinitsmf

ENABLE_CHECK=0

#PROTOTYPE_FILTER  = awk '$$$$3 ~ /\/init.d\/cswpnp$$$$/ { $$$$2 = "cswinitsmf" } { print }'

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-perl_lib_path=/opt/csw/lib/perl/csw
CONFIGURE_ARGS += --with-perfdata-logfile=/opt/csw/nagios/pnp/var/perfdata.log
CONFIGURE_ARGS += --with-perfdata-dir=/opt/csw/nagios/pnp/share/perfdata
CONFIGURE_ARGS += --with-perfdata-spool-dir=/opt/csw/nagios/pnp/var/spool/perfdata
CONFIGURE_ARGS += --htmldir=/opt/csw/nagios/share/pnp

BUILD_ARGS = all
TEST_SCRIPTS = 

INSTALL_SCRIPTS = base-custom
INSTALL_SCRIPTS += html-custom
INSTALL_SCRIPTS += scripts-custom
INSTALL_SCRIPTS += config-custom
INSTALL_SCRIPTS += contrib-custom

include gar/category.mk

DATAROOTDIR = $(datadir)
CONTRIBDIR = /opt/csw/nagios/pnp/contrib
SYSCONFDIR = $(sysconfdir)
LIBEXECDIR = $(libexecdir)
BINDIR = $(bindir)
PERFDATA_SPOOL_DIR=/opt/csw/nagios/pnp/var/spool/perfdata/
PERFDATADIR = /opt/csw/nagios/pnp/share/perfdata

install-base-custom:
	@ginstall -m 755 -d $(DESTDIR)$(BINDIR)
	@ginstall -m 755 -d $(DESTDIR)$(PERFDATA_SPOOL_DIR)
	@ginstall -m 754 $(WORKSRC)/src/npcd $(DESTDIR)$(BINDIR)
	@ginstall -m 754 $(WORKSRC)/src/npcdmod $(DESTDIR)$(BINDIR)
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswpnp $(DESTDIR)/etc/opt/csw/init.d/cswpnp
	@$(MAKECOOKIE)

install-html-custom:
	@ginstall -m 755  -d $(DESTDIR)$(DATAROOTDIR)
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/nagios/pnp/share
	@ln -s $(DESTDIR)$(DATAROOTDIR) $(DESTDIR)/opt/csw/nagios/pnp/share/html
	@ginstall -m 755  -d $(DESTDIR)$(DATAROOTDIR)/images
	@ginstall -m 755  -d $(DESTDIR)$(DATAROOTDIR)/include
	@ginstall -m 755  -d $(DESTDIR)$(DATAROOTDIR)/include/font
	@ginstall -m 755  -d $(DESTDIR)$(DATAROOTDIR)/include/font/makefont
	@ginstall -m 755  -d $(DESTDIR)$(DATAROOTDIR)/include/js
	@ginstall -m 755  -d $(DESTDIR)$(DATAROOTDIR)/lang/
	@ginstall -m 755  -d $(DESTDIR)$(DATAROOTDIR)/templates/
	@ginstall -m 755  -d $(DESTDIR)$(DATAROOTDIR)/templates.dist/
	@ginstall -m 755  -d $(DESTDIR)$(DATAROOTDIR)/templates.special/
	for file in $(WORKSRC)/share/pnp/*.php; \
	do ginstall -m 644  $$file $(DESTDIR)$(DATAROOTDIR); done
	for file in $(WORKSRC)/share/pnp/templates.dist/*.php; \
	do ginstall -m 644  $$file $(DESTDIR)$(DATAROOTDIR)/templates.dist; done
	for file in $(WORKSRC)/share/pnp/templates.special/*.php; \
	do ginstall -m 644  $$file $(DESTDIR)$(DATAROOTDIR)/templates.special; done
	for file in $(WORKSRC)/share/pnp/lang/*.php; \
	do ginstall -m 644  $$file $(DESTDIR)$(DATAROOTDIR)/lang; done
	for file in $(WORKSRC)/share/pnp/images/*; \
	do ginstall -m 644  $$file $(DESTDIR)$(DATAROOTDIR)/images; done
	for file in $(WORKSRC)/share/pnp/include/*.*; \
	do ginstall -m 644  $$file $(DESTDIR)$(DATAROOTDIR)/include; done
	for file in $(WORKSRC)/share/pnp/include/js/*; \
	do ginstall -m 644  $$file $(DESTDIR)$(DATAROOTDIR)/include/js; done
	for file in $(WORKSRC)/share/pnp/include/font/*.php; \
	do ginstall -m 644  $$file $(DESTDIR)$(DATAROOTDIR)/include/font; done
	for file in $(WORKSRC)/share/pnp/include/font/makefont/*; \
	do ginstall -m 644  $$file $(DESTDIR)$(DATAROOTDIR)/include/font/makefont; done
	@$(MAKECOOKIE)

install-scripts-custom:
	@ginstall -m 755  -d $(DESTDIR)$(PERFDATADIR)
	@ginstall -m 755  -d $(DESTDIR)$(LIBEXECDIR)
	@ginstall -m 755  $(WORKSRC)/scripts/process_perfdata.pl $(DESTDIR)$(LIBEXECDIR)
	#@ginstall -m 755  $(WORKSRC)/scripts/pcheck_pnp_rrds.pl $(DESTDIR)$(LIBEXECDIR)
	@$(MAKECOOKIE)

install-config-custom:
	-rm -f $(DESTDIR)$(HTMLDIR)/conf/config.php
	@ginstall -m 755  -d $(DESTDIR)$(SYSCONFDIR)
	@ginstall -m 755  -d $(DESTDIR)$(SYSCONFDIR)/check_commands
	@ginstall -m 755  -d $(DESTDIR)$(SYSCONFDIR)/pages
	@ginstall -m 644  $(WORKSRC)/sample-config/pnp/pnp4nagios_release $(DESTDIR)$(SYSCONFDIR)
	@ginstall -m 644   $(WORKSRC)/sample-config/pnp/config.php $(DESTDIR)$(SYSCONFDIR)
	@ginstall -m 644   $(WORKSRC)/sample-config/pnp/background.pdf $(DESTDIR)$(SYSCONFDIR)
	-rm -f $(DESTDIR)$(HTMLDIR)/conf/config.php
	@ginstall -m 755  -d $(DESTDIR)$(SYSCONFDIR)
	@ginstall -m 755  -d $(DESTDIR)$(SYSCONFDIR)/check_commands
	@ginstall -m 755  -d $(DESTDIR)$(SYSCONFDIR)/pages
	@ginstall -m 644   $(WORKSRC)/sample-config/pnp/config.php $(DESTDIR)$(SYSCONFDIR)
	@ginstall -m 644   $(WORKSRC)/sample-config/pnp/process_perfdata.cfg-sample $(DESTDIR)$(SYSCONFDIR)/process_perfdata.cfg.CSW
	@ginstall -m 644   $(WORKSRC)/sample-config/pnp/rra.cfg-sample $(DESTDIR)$(SYSCONFDIR)/rra.cfg.CSW
	@ginstall -m 644   $(WORKSRC)/sample-config/pnp/check_commands/check_nwstat.cfg-sample $(DESTDIR)$(SYSCONFDIR)/check_commands/check_nwstat.cfg.CSW
	@ginstall -m 644   $(WORKSRC)/sample-config/pnp/pages/web_traffic.cfg-sample $(DESTDIR)$(SYSCONFDIR)/pages/web_traffic.cfg.CSW
	@ginstall -m 644   $(WORKSRC)/sample-config/pnp/npcd.cfg-sample $(DESTDIR)$(SYSCONFDIR)/npcd.cfg.CSW
	@ginstall -m 644 $(WORKSRC)/sample-config/pnp/nagios_commands.cfg-sample $(DESTDIR)$(SYSCONFDIR)/nagios_commands.cfg-sample
	@$(MAKECOOKIE)

install-contrib-custom:
	@ginstall -m 755  -d $(DESTDIR)$(CONTRIBDIR)
	@ginstall -m 755  -d $(DESTDIR)$(CONTRIBDIR)/ssi
	@ginstall -m 644 $(WORKSRC)/contrib/makeserviceextinfo.pl $(DESTDIR)$(CONTRIBDIR)
	@ginstall -m 644 $(WORKSRC)/contrib/verify_pnp_config $(DESTDIR)$(CONTRIBDIR)
	@ginstall -m 644 $(WORKSRC)/contrib/verify_pnp_config.txt $(DESTDIR)$(CONTRIBDIR)
	@ginstall -m 644 $(WORKSRC)/contrib/ssi/status-header.ssi $(DESTDIR)$(CONTRIBDIR)/ssi
	@$(MAKECOOKIE)
