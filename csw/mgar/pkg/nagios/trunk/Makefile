GARNAME = nagios
GARVERSION = 3.0.6
CATEGORIES = apps

DESCRIPTION = nagios network monitoring base package (no plugins)
define BLURB
  Nagios is a powerful, enterprise-class host, service, application, and network monitoring program. Designed to be fast, flexible, and rock-solid stable. Nagios runs on *NIX hosts and can monitor Windows, Linux/Unix/BSD, Netware, and network devices.
endef

MASTER_SITES = http://kent.dl.sourceforge.net/sourceforge/nagios/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
#DISTFILES += $(call admfiles,CSWnagios)
DISTFILES += $(call admfiles,CSWnagios,prototype checkinstall preinstall preremove postinstall depend)
DISTFILES += nagios nagios.xml svc-nagios

PATCHFILES = patch.diff	# cgi/cmd.c - GNU macro __attribute__ unknown to compiler
			# http://article.gmane.org/gmane.network.nagios.devel/4726
			# (Error 2)
PATCHFILES += configure.diff	# configure.in
				# http://unix.derkeiler.com/Mailing-Lists/SunManagers/2004-11/0424.html
				# -lsunmath is needed in configure for checking of libgd
PATCHFILES += install-opts.diff	# sets in every Makefile.in "INSTALL_OPT="" (empty)
				# necessary, so ginstall doesn't get -o and -g options
PATCHFILES += webconf.diff	# global Makefile.in
				# nagios httpd-config is renamed to httpd-nagios.conf
PATCHFILES += doc.diff	# Makefile.in - copies READMes ... to /opt/csw/share/doc/nagios/

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --prefix=/opt/csw/nagios
CONFIGURE_ARGS += --exec-prefix=/opt/csw/nagios
CONFIGURE_ARGS += --with-command-user=nagios
CONFIGURE_ARGS += --with-command-group=nagios
CONFIGURE_ARGS += --with-httpd-conf=/opt/csw/nagios/etc
CONFIGURE_ARGS += --enable-embedded-perl

#prefix ?= /opt/csw/nagios
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
INSTALL_ARGS += install-webconf
INSTALL_ARGS += install-commandmode
INSTALL_ARGS += install-docs
include gar/category.mk
