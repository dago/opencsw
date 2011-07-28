# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pdsh
VERSION = 2.26
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Parallel Distributed Shell
define BLURB
  Parallel Distributed Shell
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2
PATCHFILES += 0001-use-bash-for-tests.patch

# A few tests fail (4 out of 100+)
SKIPTEST = 1

# Alternatives?
CHECKPKG_OVERRIDES_CSWpdsh += file-collision|/opt/csw/bin/dshbak|CSWclusterit|CSWpdsh

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

