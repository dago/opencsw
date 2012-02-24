# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
# ! The kernel modules need to be installed manually
# ! Fill stub with useful information

NAME = oss
VERSION = 4.2
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://www.4front-tech.com/developer/sources/stable/cddl/
DISTNAME = $(NAME)-v$(VERSION)-build2006-src-cddl
DISTFILES += $(DISTNAME).tar.bz2

# stdint.h is not on Solaris 9
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWmypkg
SPKG_DESC_CSWmypkg = My package
PKGFILES_CSWmypkg += $(call pkgfiles_lib,libabc.so.1)
PKGFILES_CSWmypkg += $(call baseisadirs,$(bindir),myexec)
PKGFILES_CSWmypkg += $(sysconfdir)/myconf

LDFLAGS =

OBJDIR = solaris
CONFIGURE_ARGS = 

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk

