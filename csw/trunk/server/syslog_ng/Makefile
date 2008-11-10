GARNAME = syslog-ng
GARVERSION = 2.0.9
CATEGORIES = server

DESCRIPTION = A powerful syslogd replacement
define BLURB
  Syslog New Generation is a powerful replacement for the standard syslogd. It
  can filter messages based on content using regular expressions and forward
  logs using TCP.
endef

MASTER_SITES = http://www.balabit.com/downloads/files/syslog-ng/sources/stable/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsyslogng, postinstall)
DISTFILES += syslog-ng.conf.CSW
DISTFILES += cswsyslog_ng

PREREQUISITE_PKGS = CSWeventlog

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
	ginstall -m 755 files/cswsyslog_ng $(DESTDIR)/opt/csw/init.d/cswsyslog_ng

include ../category.mk
