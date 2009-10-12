GARNAME = syslog-ng
GARVERSION = 3.0.4
CATEGORIES = server

DESCRIPTION = A powerful syslogd replacement
define BLURB
  Syslog New Generation is a powerful replacement for the standard syslogd. It
  can filter messages based on content using regular expressions and forward
  logs using TCP.
endef

MASTER_SITES = http://www.balabit.com/downloads/files/$(GARNAME)/open-source-edition/$(GARVERSION)/source/
DISTFILES  = $(GARNAME)_$(GARVERSION).tar.gz
DISTFILES += $(GARNAME).conf.CSW
DISTFILES += cswsyslog_ng
DISTFILES += CSWsyslogng.preinstall
DISTFILES += CSWsyslogng.postremove
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
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

REQUIRED_PKGS  = CSWgcc4corert
REQUIRED_PKGS += CSWeventlog
REQUIRED_PKGS += CSWosslrt
REQUIRED_PKGS += CSWzlib
REQUIRED_PKGS += CSWpcrert
REQUIRED_PKGS += CSWggettextrt
REQUIRED_PKGS += CSWglib2
REQUIRED_PKGS += CSWtcpwrap
REQUIRED_PKGS += CSWcswclassutils

PREREQUISITE_PKGS  = $(REQUIRED_PKGS)
PREREQUISITE_PKGS += CSWggettext
PREREQUISITE_PKGS += CSWglib2devel
PREREQUISITE_PKGS += CSWpkgconfig
PREREQUISITE_PKGS += CSWgcc4core

GARCOMPILER = GNU
TEST_SCRIPTS =

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw
	ginstall -m 444 $(WORKDIR)/$(GARNAME).conf.CSW \
		$(DESTDIR)/etc/opt/csw/$(GARNAME).conf.CSW
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswsyslog_ng \
		$(DESTDIR)/etc/opt/csw/init.d/cswsyslog_ng
	ginstall -m 755 -d $(DESTDIR)$(localstatedir)/run
	@$(MAKECOOKIE)

include gar/category.mk
