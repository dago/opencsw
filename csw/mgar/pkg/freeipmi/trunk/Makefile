# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = freeipmi
VERSION = 1.2.5

DESCRIPTION = IPMI software based on the IPMI v1.5/2.0 specification

MASTER_SITES = $(GNU_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

# This should better be detected during autoconf time
PATCHFILES += 0001-Add-missing-sighandler_t-on-Solaris.patch

VEMNDOR_URL = http://www.gnu.org/software/freeipmi/index.html

GARCOMPILER = GCC4

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

