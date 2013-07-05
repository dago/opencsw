# $Id$

NAME = duff
VERSION = 0.5.2
GARTYPE = v2

DESCRIPTION = Duplicate file finder
define BLURB
  Duff is a command-line utility for quickly finding duplicates in a given set of
  files.  It attempts to be usably fast and uses the SHA family of message
  digests as a part of the comparisons.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
VENDOR_URL = http://duff.sourceforge.net/

RUNTIME_DEP_PKGS += CSWlibintl8
PATCHFILES += 0001-add-missing-include.patch

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

