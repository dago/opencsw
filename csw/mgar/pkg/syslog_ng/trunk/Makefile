# $Id$

NAME = syslog-ng
VERSION = 3.3.3
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = A powerful syslogd replacement
define BLURB
  Syslog New Generation is a powerful replacement for the standard syslogd. It
  can filter messages based on content using regular expressions and forward
  logs using TCP.
endef

MASTER_SITES = http://www.balabit.com/downloads/files/$(NAME)/open-source-edition/$(VERSION)/source/
DISTFILES  = $(NAME)_$(VERSION).tar.gz
DISTFILES += $(NAME).conf.CSW
DISTFILES += cswsyslog_ng
DISTFILES += CSWsyslogng.preinstall
DISTFILES += CSWsyslogng.postremove
DISTFILES += CSWsyslogng.cswreleasenotes

SPKG_SOURCEURL = http://www.balabit.com/network-security/syslog-ng/opensource-logging-system/
INITSMF = /etc/opt/csw/init\.d/cswsyslog_ng
SAMPLECONF = /etc/opt/csw/syslog-ng\.conf\.CSW


# shared /opt/csw support:
localstatedir = /var/opt/csw
sysconfdir = /etc/opt/csw

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-dynamic-linking
CONFIGURE_ARGS += --enable-spoof-source=no
CONFIGURE_ARGS += --enable-tcp-wrapper

GARCOMPILER = GNU
TEST_SCRIPTS =

# The configure script finds -lwrap but doesn't actually use it.
# We need to be more pushy.
EXTRA_LDFLAGS = -L/opt/csw/lib -lwrap -lsocket

PACKAGES = CSWsyslogng
SPKG_DESC_CSWsyslogng = $(DESCRIPTION)
CATALOGNAME_CSWsyslogng = syslog_ng
RUNTIME_DEP_PKGS_CSWsyslogng += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWsyslogng += CSWglib2
RUNTIME_DEP_PKGS_CSWsyslogng += CSWlibevtlog0
RUNTIME_DEP_PKGS_CSWsyslogng += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsyslogng += CSWlibpcre0
RUNTIME_DEP_PKGS_CSWsyslogng += CSWosslrt
RUNTIME_DEP_PKGS_CSWsyslogng += CSWtcpwrap

BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWgcc4core
BUILD_DEP_PKGS += CSWggettext
BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWpkgconfig

CHECKPKG_OVERRIDES_CSWsyslogng-dev += catalogname-does-not-match-pkgname|pkgname=CSWsyslogng-dev|catalogname=syslog_ng_dev|expected-catalogname=syslogng_dev
CHECKPKG_OVERRIDES_CSWsyslogng += catalogname-does-not-match-pkgname|pkgname=CSWsyslogng|catalogname=syslog_ng|expected-catalogname=syslogng

# A reference to /usr/share/lib/zoneinfo
CHECKPKG_OVERRIDES_CSWsyslogng += file-with-bad-content|/usr/share|root/opt/csw/lib/libsyslog-ng.so.0.0.0

# Not splitting the syslog-ng libraries.  There are no known packages linking
# to syslog's shared objects.
CHECKPKG_OVERRIDES_CSWsyslogng += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWsyslogng += shared-lib-pkgname-mismatch

# Missing TLS symbols
EXTRA_LINKER_FLAGS = -lgnutls

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw
	ginstall -m 444 $(WORKDIR)/$(NAME).conf.CSW \
		$(DESTDIR)/etc/opt/csw/$(NAME).conf.CSW
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswsyslog_ng \
		$(DESTDIR)/etc/opt/csw/init.d/cswsyslog_ng
	ginstall -m 755 -d $(DESTDIR)$(localstatedir)/run
	@$(MAKECOOKIE)

include gar/category.mk
