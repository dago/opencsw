# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = logrotate
VERSION = 3.8.3 apps
GARTYPE = v2

DESCRIPTION = Rotates, compresses, and mails system logs

define BLURB
   The logrotate utility is designed to simplify the administration of log files on a system which generates a lot of log files.
   Logrotate allows for the automatic rotation compression, removal and mailing of log files.
   Logrotate can be set to handle a log file daily, weekly, monthly or when the log file gets to a certain size. 
endef

SPKG_SOURCEURL = https://fedorahosted.org/logrotate/
MASTER_SITES = https://fedorahosted.org/releases/l/o/logrotate/01-default-locations.patch
PATCHFILES += 0001-make-this-overridable.patch

DISTFILES  = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS = CSWlibpopt0
BUILD_DEP_PKGS   = CSWlibpopt-dev

CONFIGURE_SCRIPTS =
# TEST_ENV_PATH = $(prefix)/gnu:$(PATH)
# TEST_TARGET = test
# Currently tests are failing. The reason being that setfacl doesn't seem to work on ZFS
# I don't know how to disable specific tests, so I'm disabling them all
TEST_TARGET = 

BUILD64 = 1
ISAEXEC = 1

include gar/category.mk

EXTRA_INSTALL_EXPORTS = PREFIX BASEDIR MANDIR BINDIR
INSTALL_ENV_PREFIX = $(DESTDIR)
INSTALL_ENV_BASEDIR = $(prefix)
INSTALL_ENV_MANDIR = $(mandir)
INSTALL_ENV_BINDIR = $(sbindir)

EXTRA_BUILD_EXPORTS = EXTRA_CFLAGS EXTRA_CPPFLAGS EXTRA_LDFLAGS
BUILD_ENV_EXTRA_CFLAGS =$(CFLAGS)
BUILD_ENV_EXTRA_CPPFLAGS = $(CPPFLAGS)
BUILD_ENV_EXTRA_LDFLAGS = $(LDFLAGS MANDIR = $(mandir)


# This is a hack, as I have no idea what's going wrong.
pre-test-modulated:
	@( cd $(WORKSRC) ; \
		rm -f .depend )

pre-install-modulated:
	@( cd $(WORKSRC) ; \
		rm -f .depend )

pre-build-modulated:
	@( cd $(WORKSRC) ; \

