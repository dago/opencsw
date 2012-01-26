# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = tre
VERSION = 0.8.0
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = Approximate regex matching library
define BLURB
endef
SPKG_SOURCEURL = http://laurikari.net/tre/
MASTER_SITES = http://laurikari.net/tre/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
BUILD64_LIBS_ONLY = 1
# agrep needs getopt_long
# TODO: Solve the getopt_long problem and build agrep.
# PATCHFILES += 0001-gnulib-import-getopt-gnu.patch
# PATCHFILES += 0002-manual-gnulib-integration-steps.patch
# EXTRA_LD_OPTIONS = -lgnugetopt
CONFIGURE_ARGS = $(DIRPATHS) --disable-agrep
PACKAGES += CSWlibtre5
SPKG_DESC_CSWlibtre5 = Approximate regex matching library (libtre.so.5)
PKGFILES_CSWlibtre5 = /opt/csw/lib/.*libtre\.so\.5.*
RUNTIME_DEP_PKGS_CSWlibtre5 += CSWlibintl8

PACKAGES += CSWtre-dev
CATALOGNAME_CSWtre-dev = tre_dev
# PKGFILES_CSWtre-dev += $(PKGFILES_DEVEL)
SPKG_DESC_CSWtre-dev = Development files for tre
RUNTIME_DEP_PKGS_CSWtre-dev += CSWlibtre5

LICENSE = LICENSE

include gar/category.mk

# pre-configure-modulated:
# 	@(cd $(WORKSRC); autoreconf -i )
# 	@$(MAKECOOKIE)
