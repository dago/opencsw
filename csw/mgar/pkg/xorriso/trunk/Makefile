# $Id$
NAME = xorriso
VERSION = 1.1.4
CATEGORIES = utils

DESCRIPTION = ISO 9660 Rock Ridge Filesystem Manipulator
define BLURB
  xorriso copies file objects from POSIX compliant filesystems into Rock Ridge enhanced
  ISO 9660 filesystems and allows session-wise manipulation of such filesystems.
  It can load the management information of existing ISO images and it writes the
  session results to optical media or to filesystem objects.
  Vice versa xorriso is able to copy file objects out of ISO 9660 filesystems.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWlibreadline-dev

RUNTIME_DEP_PKGS_CSWxorriso += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWxorriso += CSWbzip2
RUNTIME_DEP_PKGS_CSWxorriso += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWxorriso += CSWlibz1

include gar/category.mk
