# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = mailman
VERSION = 2.1.15

DESCRIPTION = Mailman mailing list software

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tgz

PACKAGES += CSWmailman
SPKG_DESC_CSWmailman = Mailman mailing list software
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWmailman += CSWpython
RUNTIME_DEP_PKGS_CSWmailman += CSWperl

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --without-permcheck

# There is no testsuite
TEST_SCRIPTS =

PYCOMPILE = 1

include gar/category.mk

