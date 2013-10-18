# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libmetalink
VERSION = 0.1.2
GARTYPE = v2

DESCRIPTION = A library to add Metalink functionality

MASTER_SITES = https://launchpad.net/libmetalink/trunk/packagingfix/+download/
DISTFILES += $(DISTNAME).tar.bz2

# Important bzr revisions after release of 0.1.2 from
#   https://code.launchpad.net/~metalink-dev/libmetalink/trunk
PATCHFILES += 0153-bzr-commit-153.patch
PATCHFILES += 0154-bzr-commit-154.patch

# Use patch until this is fixed:
#   https://bugs.launchpad.net/libmetalink/+bug/1241633
PATCHFILES += 0001-Do-not-use-Wall-unconditionally.patch

# Use patch until this is fixed:
#   https://bugs.launchpad.net/libmetalink/+bug/1241635
PATCHFILES += 0002-Add-definition-of-INT32_MIN.patch

# Use patch until this is fixed:
#   https://bugs.launchpad.net/libmetalink/+bug/1241639
PATCHFILES += 0003-Use-pkgconfig-for-expat-libs.patch

PACKAGES += CSWlibmetalink3
SPKG_DESC_CSWlibmetalink3 = A library to add Metalink functionality, libmetalink.so.3
PKGFILES_CSWlibmetalink3 += $(call pkgfiles_lib,libmetalink.so.3)
RUNTIME_DEP_PKGS_CSWlibmetalink3 += CSWlibexpat1

PACKAGES += CSWlibmetalink-dev
SPKG_DESC_CSWlibmetalink-dev = Development files for libmetalink.so.3
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibmetalink-dev += CSWlibmetalink3

BUILD64 = 1

include gar/category.mk

