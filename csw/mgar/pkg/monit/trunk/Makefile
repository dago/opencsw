# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = monit
VERSION = 5.3.1
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Utility for monitoring and managing daemons or similar programs
define BLURB
  Long description
endef

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

VENDOR_URL = http://mmonit.com/monit/
MASTER_SITES = http://mmonit.com/monit/dist/
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES += 0001-Drop-some-build-flags-that-get-hard-coded-by-configu.patch

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

