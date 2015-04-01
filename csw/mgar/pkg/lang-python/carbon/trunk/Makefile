# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = carbon
VERSION = 0.9.13
CATEGORIES = python

DESCRIPTION = Backend data caching and persistence daemon for Graphite

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWpy-carbon
SPKG_DESC_CSWpy-carbon = Backend data caching and persistence daemon for Graphite
# PKGFILES is catchall
ARCHALL_CSWpy-carbon = 1

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk

post-extract:
	-cd $(WORKSRC) && mv setup.cfg setup.cfg.orig
	@$(MAKECOOKIE)
