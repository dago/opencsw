GARNAME = syslog-ng
GARVERSION = 2.0.10
CATEGORIES = server

DESCRIPTION = A powerful syslogd replacement
define BLURB
  Syslog New Generation is a powerful replacement for the standard syslogd. It
  can filter messages based on content using regular expressions and forward
  logs using TCP.
endef

MASTER_SITES = http://www.balabit.com/downloads/files/syslog-ng/open-source-edition/$(GARVERSION)/source/
DISTFILES  = $(GARNAME)_$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsyslogng, postinstall depend prototype)
DISTFILES += syslog-ng.conf.CSW
DISTFILES += cswsyslog_ng

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.balabit.com/network-security/syslog-ng/
SPKG_CLASSES = none cswinitsmf

PREREQUISITE_PKGS  = CSWeventlog
PREREQUISITE_PKGS += CSWggettext
PREREQUISITE_PKGS += CSWglib2
PREREQUISITE_PKGS += CSWtcpwrap

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-dynamic-linking
CONFIGURE_ARGS += --enable-spoof-source=no

GARCOMPILER = GNU
#TEST_TARGET = check
TEST_SCRIPTS =

# adding configuration file
post-install:
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -m 444 $(WORKDIR)/syslog-ng.conf.CSW $(DESTDIR)$(sysconfdir)/syslog-ng.conf.CSW
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 files/cswsyslog_ng $(DESTDIR)/etc/opt/csw/init.d/cswsyslog_ng

include gar/category.mk
