# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pidentd
VERSION = 3.0.19
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Portable ident daemon
define BLURB
endef

MASTER_SITES = ftp://ftp.stack.nl/pub/users/johans/pidentd/
DISTFILES  = $(DISTNAME).tar.gz

PATCHDIRLEVEL = 0

# From ftp://ftp.stack.nl/pub/users/johans/pidentd/
PATCHFILES += pidentd-3.0.19-ipv6-20080101.diff.gz

# From http://www.vlakno.cz/~rdivacky/pidentd.diff
PATCHFILES += pidentd.diff

# We need a specific version for each release
PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

VENDOR_URL = http://www.lysator.liu.se/~pen/pidentd/

LICENSE = README

PACKAGES += CSWpidentd
SPKG_DESC_CSWmypkg = Portable ident daemon
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpidentd += CSWlibssl0-9-8

REINPLACEMENTS += ignoreisa
REINPLACE_MATCH_ignoreisa = ISA="
REINPLACE_WITH_ignoreisa = ISA="IGNORE
REINPLACE_FILES_ignoreisa += configure

BUILD64 = 1
ISAEXEC = 1

# There is no testsuite
TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS += mandir
INSTALL_OVERRIDE_VAR_mandir = $(DESTDIR)$(mandir)
INSTALL_OVERRIDE_VARS += sbindir
INSTALL_OVERRIDE_VAR_sbindir = $(DESTDIR)$(sbindir)

include gar/category.mk

