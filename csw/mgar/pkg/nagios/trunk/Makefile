GARNAME = nagios
GARVERSION = 3.2.0
CATEGORIES = apps

DESCRIPTION = nagios network monitoring base package (no plugins)
define BLURB
  Nagios is a powerful, enterprise-class host, service, application, and network monitoring program. Designed to be fast, flexible, and rock-solid stable. Nagios runs on *NIX hosts and can monitor Windows, Linux/Unix/BSD, Netware, and network devices.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
#DISTFILES += $(call admfiles,CSWnagios,checkinstall preinstall preremove prototype )
DISTFILES += CSWnagios.checkinstall CSWnagios.preinstall CSWnagios.preremove CSWnagios.prototype
DISTFILES += cswnagios

PATCHFILES = patch.diff	# cgi/cmd.c - GNU macro __attribute__ unknown to compiler
			# http://article.gmane.org/gmane.network.nagios.devel/4726
			# (Error 2)
PATCHFILES += configure.diff	# configure
PATCHFILES += install-opts.diff	# sets in every Makefile.in "INSTALL_OPT="" (empty)
				# necessary, so ginstall doesn't get -o and -g options

PACKAGES = CSWnagios
CATALOGNAME = nagios

REQUIRED_PKGS_CSWnagios  = CSWapache2 CSWgd CSWglib2 CSWiconv CSWjpeg CSWlibtoolrt CSWggettextrt
REQUIRED_PKGS_CSWnagios += CSWosslrt CSWperl CSWpng CSWzlib CSWnagiosp CSWap2modphp5 CSWcswclassutils

SPKG_CLASSES = none cswpreserveconf cswinitsmf

NOISALIST = 1

prefix = $(BUILD_PREFIX)/nagios
libexecdir = $(BUILD_PREFIX)/libexec/nagios-plugins

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --prefix=$(prefix)
CONFIGURE_ARGS += --exec-prefix=$(exec_prefix)
CONFIGURE_ARGS += --with-command-user=nagios
CONFIGURE_ARGS += --with-command-group=nagios
CONFIGURE_ARGS += --with-httpd-conf=$(sysconfdir)
CONFIGURE_ARGS += --with-gd-lib-dir=$(BUILD_PREFIX)/lib
CONFIGURE_ARGS += --with-gd-lib-inc=$(BUILD_PREFIX)/inc
CONFIGURE_ARGS += --enable-embedded-perl

EXTRA_LIB = $(BUILD_PREFIX)/lib
EXTRA_INC = $(BUILD_PREFIX)/include

BUILD_ARGS = all

ENABLE_CHECK = 0

TEST_TARGET = none

INSTALL_ARGS += install-init
#INSTALL_ARGS += install-config
INSTALL_ARGS += install-commandmode

LD_OPTIONS += -R/opt/csw/lib
LD_OPTIONS -= -R/opt/csw/nagios/lib

include gar/category.mk

DOCS = Changelog INSTALLING README UPGRADING
DOCDEST = $(DESTDIR)$(BUILD_PREFIX)/share/doc/nagios
HTTPD_CONF = $(DESTDIR)$(sysconfdir)
CFGDIR = $(prefix)/etc

post-install-modulated:
	@ginstall -m 755 -d $(DOCDEST)
	@ginstall -m 755 -d $(HTTPD_CONF)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@ginstall -m 644 $(WORKSRC)/LICENSE $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/sample-config/httpd.conf $(HTTPD_CONF)/httpd-nagios.conf
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswnagios $(DESTDIR)/etc/opt/csw/init.d/cswnagios
	@ginstall -m 775 -d $(DESTDIR)$(CFGDIR)
	@ginstall -m 775 -d $(DESTDIR)$(CFGDIR)/objects
	@ginstall -b -m 664 $(WORKSRC)/sample-config/nagios.cfg $(DESTDIR)$(CFGDIR)/nagios.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/cgi.cfg $(DESTDIR)$(CFGDIR)/cgi.cfg.CSW
	@ginstall -b -m 660 $(WORKSRC)/sample-config/resource.cfg $(DESTDIR)$(CFGDIR)/resource.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/templates.cfg $(DESTDIR)$(CFGDIR)/objects/templates.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/commands.cfg $(DESTDIR)$(CFGDIR)/objects/commands.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/contacts.cfg $(DESTDIR)$(CFGDIR)/objects/contacts.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/timeperiods.cfg $(DESTDIR)$(CFGDIR)/objects/timeperiods.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/localhost.cfg $(DESTDIR)$(CFGDIR)/objects/localhost.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/windows.cfg $(DESTDIR)$(CFGDIR)/objects/windows.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/printer.cfg $(DESTDIR)$(CFGDIR)/objects/printer.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/switch.cfg $(DESTDIR)$(CFGDIR)/objects/switch.cfg.CSW
	@$(MAKECOOKIE)
