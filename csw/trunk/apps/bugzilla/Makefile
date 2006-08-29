GARNAME = bugzilla
GARVERSION = 2.22
CATEGORIES = apps

DESCRIPTION = Integrated SCM and Project Management
define BLURB
	Trac is an enhanced wiki and issue tracking system for software development
	projects. Trac uses a minimalistic approach to web-based software project
	management. Our mission; to help developers write great software while
	staying out of the way. Trac should impose as little as possible on a team's
	established development process and policies.
endef

MASTER_SITES = ftp://ftp.mozilla.org/pub/mozilla.org/webtools/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWbugzilla,prototype)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS =
TEST_SCRIPTS =

include ../category.mk

