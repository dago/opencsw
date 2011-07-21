# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = logrotate
VERSION = 3.8.0
CATEGORIES = apps

DESCRIPTION = rotates, compresses, and mails system logs

define BLURB
   The logrotate utility is designed to simplify the administration of log files on a system which generates a lot of log files.
   Logrotate allows for the automatic rotation compression, removal and mailing of log files.
   Logrotate can be set to handle a log file daily, weekly, monthly or when the log file gets to a certain size. 
endef

SPKG_SOURCEURL = https://fedorahosted.org/logrotate/
MASTER_SITES = https://fedorahosted.org/releases/l/o/logrotate/

PATCHFILES  = 001-makefu.patch
PATCHFILES += 002-strndup.patch
PATCHFILES += 003-test.patch
PATCHFILES += 004-alloca.patch
PATCHFILES += 005-gzippath.patch
PATCHFILES += 006-mbrtowc_empty.patch
PATCHFILES += 007-warn-unreached.patch

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += 001-makefu.patch
DISTFILES += 002-strndup.patch
DISTFILES += 003-test.patch
DISTFILES += 005-gzippath.patch
DISTFILES += 006-mbrtowc_empty.patch
DISTFILES += 007-warn-unreached.patch

RUNTIME_DEP_PKGS = CSWlibpopt
BUILD_DEP_PKGS   = $(RUNTIME_DEP_PKGS)

CONFIGURE_SCRIPTS =
TEST_TARGET = test

# "optimize"
NOISALIST = 1

# Don't ask, it doesn't work otherwise.
export EXTRA_CFLAGS = -I$(includedir)
export EXTRA_LDFLAGS = -L$(libdir)
export PREFIX = $(DESTDIR)
export BASEDIR = $(prefix)
export MANDIR = $(mandir)

include gar/category.mk

# This is a hack, as I have no idea what's going wrong.
pre-test-modulated:
        @( cd $(WORKSRC) ; \
                rm -f .depend )

pre-install-modulated:
        @( cd $(WORKSRC) ; \
                rm -f .depend )

pre-build-modulated:
        @( cd $(WORKSRC) ; \
                rm -f .depend )
