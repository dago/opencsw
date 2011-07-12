# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libexplain
VERSION = 0.44.D001
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Explains unix system call errors
define BLURB
endef

PATCHFILES += 0001-Shield-ptrace-defines.patch
PATCHFILES += 0002-Include-stdarg.h-for-va_list.patch
PATCHFILES += 0003-Do-not-return-anything-in-void-functions.patch
PATCHFILES += 0004-Use-fallback-for-AI_NUMERICSERV.patch
PATCHFILES += 0005-Solaris-does-not-have-O_NOFOLLOW.patch
PATCHFILES += 0006-Fix-typo-of-stat-struct-member.patch
PATCHFILES += 0007-Need-headers-for-major-minor.patch
PATCHFILES += 0008-inttypes.h-is-needed-for-int-_t.patch
PATCHFILES += 0009-Use-necessary-mnttab.h.patch
PATCHFILES += 0010-Include-sys-types.h-for-size_t.patch

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

BUILD64 = 1

include gar/category.mk

