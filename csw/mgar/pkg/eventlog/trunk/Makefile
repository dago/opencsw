GARNAME = eventlog
GARVERSION = 0.2.5
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWeventlog,depend)

CONFIGURE_ARGS = $(DIRPATHS)

GARCOMPILER = GNU
TEST_SCRIPTS =

include gar/category.mk
