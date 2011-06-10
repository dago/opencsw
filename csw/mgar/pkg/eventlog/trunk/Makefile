# $Id$

NAME = eventlog
VERSION = 0.2.12
CATEGORIES = lib

DESCRIPTION = Replacement of the simple syslog() API providing structure to messages.
define BLURB
	The EventLog library aims to be a replacement of the simple syslog() API
	provided on UNIX systems. The major difference between EventLog and syslog
	is that EventLog tries to add structure to messages.
	Where you had a simple non-structrured string in syslog() you have a
	combination of description and tag/value pairs.
	EventLog provides an interface to build, format and output an event record.
	The exact format and output method can be customized by the administrator
	via a configuration file.
endef

MASTER_SITES = http://www.balabit.com/downloads/files/eventlog/0.2/
DISTFILES  = $(NAME)_$(VERSION).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS += CSWgcc4corert

GARCOMPILER = GNU
TEST_SCRIPTS =

OBSOLETED_BY_CSWeventlog-dev = CSWeventlog

PACKAGES = CSWlibevtlog0
CATALOGNAME_CSWlibevtlog0 = libevtlog0
PKGFILES_CSWlibevtlog0 += $(call baseisadirs,$(libdir),libevtlog\.so\.0\.0\.0)
PKGFILES_CSWlibevtlog0 += $(call baseisadirs,$(libdir),libevtlog\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibevtlog0 += Replacement of the simple syslog() API providing structure to messages., libevtlog.so.0
RUNTIME_DEP_PKGS_CSWeventlog += CSWlibevtlog0
PACKAGES += CSWeventlog-dev
PKGFILES_CSWeventlog-dev += $(PKGFILES_DEV)
CATALOGNAME_CSWeventlog-dev = eventlog_dev
SPKG_DESC_CSWeventlog-dev = $(DESCRIPTION) - development files
RUNTIME_DEP_PKGS_CSWeventlog-dev += CSWlibevtlog0

include gar/category.mk
