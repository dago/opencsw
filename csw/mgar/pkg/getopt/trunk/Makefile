# $Id$
NAME = getopt
VERSION = 1.1.4
CATEGORIES = lib

DESCRIPTION = Help shell scripts parse command-line parameters
define BLURB
endef

# TBD:
# - The existing package uses ggetopt instead of getopt everywhere
# - The existing package is linked against CSWggettext and CSWlibiconv

MASTER_SITES = http://software.frodo.looijaard.name/getopt/files/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES = 0001-Include-locale.h-when-using-gettext.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWggetopt
CATALOGNAME = ggetopt

VENDOR_URL = http://software.frodo.looijaard.name/getopt/

# No scipt there...
CONFIGURE_SCRIPTS =

BUILD_OVERRIDE_VARS = prefix CC CFLAGS LIBCGETOPT
BUILD_OVERRIDE_VAR_prefix = $(prefix)
BUILD_OVERRIDE_VAR_CC = $(CC)
BUILD_OVERRIDE_VAR_CFLAGS = $(CFLAGS)
BUILD_OVERRIDE_VAR_LIBCGETOPT = 0

TEST_TARGET =

INSTALL_OVERRIDE_VARS = prefix mandir WITH_GETTEXT
INSTALL_OVERRIDE_VAR_prefix = $(prefix)
INSTALL_OVERRIDE_VAR_mandir = $(mandir)
INSTALL_OVERRIDE_VAR_WITH_GETTEXT = 1

INSTALL_ARGS = install install_doc

include gar/category.mk

# Use correct version of 'install'
PATH := /opt/csw/gnu:$(PATH)
