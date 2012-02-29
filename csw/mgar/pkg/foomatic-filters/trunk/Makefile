# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = foomatic-filters
VERSION = 4.0.12
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Cups printer driver for non postscript printers
define BLURB
  Foomatic is a database-driven system for integrating free software printer drivers with common spoolers under Unix. It supports CUPS, LPRng, LPD, GNUlpr, Solaris LP, PPR, PDQ, CPS, and direct printing with every free software printer driver known to us and every printer known to work with these drivers.
endef

MASTER_SITES = http://www.openprinting.org/download/foomatic/
DISTFILES  = $(DISTNAME).tar.gz
# GARCOMPILER = GNU
GARCOMPILER = SOS12U3

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc
PATCHFILES += 0001-sanitize-data-type-process.c.patch

PACKAGES = CSWfoomatic-filters
OBSOLETED_BY_CSWfoomatic-filters = CSWfoomaticfilters CSWhpijs
SPKG_DESC_CSWfoomatic-filters = $(DESCRIPTION) foomatic
RUNTIME_DEP_PKGS_CSWfoomatic-filters += CSWlibdbus1-3

CHECKPKG_OVERRIDES_CSWfoomatic-filters += file-with-bad-content|/usr/local|root/opt/csw/bin/foomatic-rip
CHECKPKG_OVERRIDES_CSWfoomatic-filters += file-with-bad-content|/usr/local|root/opt/csw/lib/cups/backend/beh
CHECKPKG_OVERRIDES_CSWfoomatic-filters += file-with-bad-content|/usr/local|root/etc/opt/csw/foomatic/filter.conf
CHECKPKG_OVERRIDES_CSWfoomatic-filters += file-with-bad-content|/usr/local|root/etc/opt/csw/foomatic/filter.conf.sample
CHECKPKG_OVERRIDES_CSWfoomatic-filters += file-with-bad-content|/usr/share|root/opt/csw/bin/foomatic-rip

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

