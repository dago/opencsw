GARNAME = syslog-ng
GARVERSION = 3.0.4
CATEGORIES = server

DESCRIPTION = A powerful syslogd replacement
define BLURB
  Syslog New Generation is a powerful replacement for the standard syslogd. It
  can filter messages based on content using regular expressions and forward
  logs using TCP.
endef

MASTER_SITES = http://www.balabit.com/network-security/syslog-ng/opensource-logging-system/
DISTFILES  = $(GARNAME)_$(GARVERSION).tar.gz
DISTFILES += $(GARNAME).conf.CSW
DISTFILES += cswsyslog_ng
DISTFILES += CSWsyslogng.preinstall
DISTFILES += CSWsyslogng.postremove

CATALOGNAME = syslog_ng

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWsyslogng

SPKG_SOURCEURL = http://www.balabit.com/network-security/$(GARNAME)/

SPKG_CLASSES = none cswcpsampleconf cswinitsmf
PROTOTYPE_FILTER  = awk ' \
    $$$$3 ~ /\/init.d\/cswsyslog_ng$$$$/ { $$$$2 = "cswinitsmf" } \
    $$$$3 ~ /\/syslog-ng\.conf\.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
    { print }'

PREREQUISITE_PKGS  = CSWeventlog
PREREQUISITE_PKGS += CSWggettext
PREREQUISITE_PKGS += CSWglib2
PREREQUISITE_PKGS += CSWglib2devel
PREREQUISITE_PKGS += CSWtcpwrap
PREREQUISITE_PKGS += CSWpkgconfig
PREREQUISITE_PKGS += CSWgcc4core

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-dynamic-linking
CONFIGURE_ARGS += --enable-spoof-source=no
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw

REQUIRED_PKGS  = CSWgcc4corert
REQUIRED_PKGS += CSWeventlog
REQUIRED_PKGS += CSWosslrt
REQUIRED_PKGS += CSWzlib
REQUIRED_PKGS += CSWpcrert
REQUIRED_PKGS += CSWggettextrt
REQUIRED_PKGS += CSWglib2
REQUIRED_PKGS += CSWtcpwrap
REQUIRED_PKGS += CSWcswclassutils

GARCOMPILER = GNU
TEST_SCRIPTS =

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw
	ginstall -m 444 $(WORKDIR)/$(GARNAME).conf.CSW \
		$(DESTDIR)/etc/opt/csw/$(GARNAME).conf.CSW
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswsyslog_ng \
		$(DESTDIR)/etc/opt/csw/init.d/cswsyslog_ng

include gar/category.mk
