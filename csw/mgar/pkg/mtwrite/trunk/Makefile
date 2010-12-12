# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = mtwrite
VERSION = r90214
CATEGORIES = lib

DESCRIPTION = Library to enable tar and unzip to write multiple files in parallel
define BLURB
endef

MASTER_SITES = http://www.maier-komor.de/mtwrite/
DISTFILES  = $(NAME)-$(VERSION).tgz
PATCHFILES  = 0001-Use-man3-and-skip-intermediate-lib-dir.patch
PATCHFILES += 0002-Hardcode-library-position.patch
PATCHFILES += 0003-Fix-path-in-manpage.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

LICENSE = lgpl.txt

CONFIGURE_SCRIPTS =

BUILD_OVERRIDE_VARS = CC
BUILD_OVERRIDE_VAR_CC = $(CC)

TEST_SCRIPTS =

INSTALL_OVERRIDE_DIRS = PREFIX
PREFIX=$(prefix)

include gar/category.mk
