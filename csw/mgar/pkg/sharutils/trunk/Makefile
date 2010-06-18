# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# There is a problem with the test suite, which is affected by the presence of
# .git directories in $(WORKSRC).  A temporary workaround might be to use gar
# at r10011.

GARNAME = sharutils
GARVERSION = 4.9
CATEGORIES = utils
DESCRIPTION = Makes so-called shell archives out of many files
define BLURB
endef
SPKG_SOURCEURL = http://www.gnu.org/software/sharutils/
MASTER_SITES = ftp://ftp.gnu.org/gnu/sharutils/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
TEST_TARGET = check
CONFIGURE_ARGS = $(DIRPATHS)
# Apparently, 64 bit builds are frown upon:
# http://lists.opencsw.org/pipermail/pkgsubmissions/2010-June/000907.html
# BUILD64 = 1

# To make the test use gmd5sum
MD5SUM = gmd5sum
RUNTIME_DEP_PKGS_CSWsharutils += CSWggettextrt
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWsharutils) CSWcoreutils
export MD5SUM
include gar/category.mk

post-merge:
	rm $(PKGROOT)$(libdir)/charset.alias
	@$(MAKECOOKIE)
