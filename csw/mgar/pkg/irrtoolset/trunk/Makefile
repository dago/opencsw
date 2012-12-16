# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = irrtoolset
VERSION = 5.0.0
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = ftp://ftp.isc.org/isc/IRRToolSet/IRRToolSet-5.0.0/
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

PATCHFILES += 0001-Add-missing-this-in-src-normalform-Stack.hh.patch
PATCHFILES += 0002-Added-gnulib-strcasestr-module.patch
PATCHFILES += 0003-Added-references-to-Makefile.am-and-configure.ac.patch

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC); autoreconf -fi
	@$(MAKECOOKIE)
