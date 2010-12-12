NAME = syslog-ng
VERSION = 3.0.5
CATEGORIES = server

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
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
PACKAGES = CSWsyslogng
CATALOGNAME = syslog_ng
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

RUNTIME_DEP_PKGS += CSWeventlog
RUNTIME_DEP_PKGS += CSWosslrt
RUNTIME_DEP_PKGS += CSWzlib
RUNTIME_DEP_PKGS += CSWpcrert
RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWtcpwrap

BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWggettext
BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWgcc4core

GARCOMPILER = GNU
TEST_SCRIPTS =

# The configure script finds -lwrap but doesn't actually use it.
# We need to be more pushy.
EXTRA_LDFLAGS = -L/opt/csw/lib -lwrap -lsocket

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
