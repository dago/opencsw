GARNAME = nagios
GARVERSION = 3.0.6
CATEGORIES = apps

DESCRIPTION = nagios network monitoring base package (no plugins)
define BLURB
  Nagios is a powerful, enterprise-class host, service, application, and network monitoring program. Designed to be fast, flexible, and rock-solid stable. Nagios runs on *NIX hosts and can monitor Windows, Linux/Unix/BSD, Netware, and network devices.
endef

MASTER_SITES =$(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWnagios,checkinstall preinstall preremove prototype )
DISTFILES += cswnagios

PATCHFILES = patch.diff	# cgi/cmd.c - GNU macro __attribute__ unknown to compiler
			# http://article.gmane.org/gmane.network.nagios.devel/4726
			# (Error 2)
PATCHFILES += configure.diff	# configure.in
				# http://unix.derkeiler.com/Mailing-Lists/SunManagers/2004-11/0424.html
				# -lsunmath is needed in configure for checking of libgd
PATCHFILES += install-opts.diff	# sets in every Makefile.in "INSTALL_OPT="" (empty)
				# necessary, so ginstall doesn't get -o and -g options

REQUIRED_PKGS_CSWnagios  = CSWapache CSWgd CSWglib2 CSWiconv CSWjpeg CSWlibtoolrt CSWggettextrt
REQUIRED_PKGS_CSWnagios += CSWosslrt CSWperl CSWpng CSWzlib CSWnagiosp CSWnrpeplugin CSWcswclassutils

SPKG_CLASSES = none cswinitsmf

PROTOTYPE_FILTER  = awk '$$$$3 ~ /\/init.d\/cswnagios$$$$/ { $$$$2 = "cswinitsmf" } { print }'

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --prefix=/opt/csw/nagios
CONFIGURE_ARGS += --exec-prefix=/opt/csw/nagios
CONFIGURE_ARGS += --with-command-user=nagios
CONFIGURE_ARGS += --with-command-group=nagios
CONFIGURE_ARGS += --with-httpd-conf=/opt/csw/nagios/etc
CONFIGURE_ARGS += --enable-embedded-perl

sysconfdir ?= $(prefix)/nagios/etc
localstatedir ?= $(prefix)/nagios/var
bindir ?= $(prefix)/nagios/bin
sbindir ?= $(prefix)/nagios/sbin
libexecdir ?= $(prefix)/libexec/nagios-plugins
datadir ?= $(prefix)/nagios/share

EXTRA_LIB = /opt/csw/lib

BUILD_ARGS = all

TEST_TARGET = none

INSTALL_ARGS += install-init
INSTALL_ARGS += install-config
INSTALL_ARGS += install-commandmode

include gar/category.mk

DOCS = Changelog INSTALLING README UPGRADING
DOCDEST = $(DESTDIR)$(prefix)/share/doc/nagios
HTTPD_CONF = $(DESTDIR)$(sysconfdir)

post-install-modulated:
	@echo $(DOCDEST)
	@ginstall -m 755 -d  $(DOCDEST)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@ginstall -m 644 $(WORKSRC)/LICENSE $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/sample-config/httpd.conf $(HTTPD_CONF)/httpd-nagios.conf
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswnagios $(DESTDIR)/etc/opt/csw/init.d/cswnagios
	@$(MAKECOOKIE)

