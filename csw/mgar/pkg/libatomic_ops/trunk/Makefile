# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = libatomic_ops
MAJOR = 7.2
MINOR = d
VERSION = $(MAJOR)$(MINOR)
DISTNAME = $(NAME)-$(MAJOR)

DESCRIPTION = Portable library for atomic operations

VENDOR_URL = http://www.hpl.hp.com/research/linux/atomic_ops/

MASTER_SITES += http://www.hpl.hp.com/research/linux/atomic_ops/download/
DISTFILES += $(DISTNAME).tar.gz

PACKAGES += CSWlibatomic-ops
SPKG_DESC_CSWlibatomic-ops = Portable library for atomic operations
# PKGFILES is catchall

# This is because of the static libs
CHECKPKG_OVERRIDES_CSWlibatomic-ops += discouraged-path-in-pkgmap

GARCOMPILER = GCC4

BUILD64 = 1

# The static lib is what we want
MERGE_EXCLUDE_STATICLIBS =

include gar/category.mk
