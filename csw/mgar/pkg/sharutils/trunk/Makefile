# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# There is a problem with the test suite, which is affected by the presence of
# .git directories in $(WORKSRC).  A temporary workaround might be to use gar
# at r10011.

NAME = sharutils
VERSION = 4.11.1
CATEGORIES = utils
DESCRIPTION = Makes so-called shell archives out of many files
define BLURB
endef
SPKG_SOURCEURL = http://www.gnu.org/software/sharutils/
MASTER_SITES = ftp://ftp.gnu.org/gnu/sharutils/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
# Apparently, 64 bit builds are frown upon:
# http://lists.opencsw.org/pipermail/pkgsubmissions/2010-June/000907.html
# BUILD64 = 1

# To make the test use gmd5sum
MD5SUM = gmd5sum
export MD5SUM
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWsharutils) CSWcoreutils

RUNTIME_DEP_PKGS_CSWsharutils += CSWlibintl8

PACKAGES += CSWsharutils
SPKG_DESC_CSWsharutils = $(DESCRIPTION)
CHECKPKG_OVERRIDES_CSWsharutils += file-with-bad-content|/usr/share|root/opt/csw/share/locale/es/LC_MESSAGES/sharutils.mo

SKIPTEST ?= 1

include gar/category.mk

post-install-modulated:
	gmv $(DESTDIR)$(bindir)/uuencode $(DESTDIR)$(bindir)/uuencode-sharutils
	gmv $(DESTDIR)$(bindir)/uudecode $(DESTDIR)$(bindir)/uudecode-sharutils
	@$(MAKECOOKIE)

post-merge:
	rm $(PKGROOT)$(libdir)/charset.alias
	@$(MAKECOOKIE)
