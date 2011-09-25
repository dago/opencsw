# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xcdroast
VERSION = 0.98alpha16
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = A GUI wrapper for cdrtools
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
MASTER_SITES += http://www.xcdroast.org/xcdr098/patches/
DISTFILES  = $(DISTNAME).tar.gz

# The upstream patches have different patch levels, convert to git patches below
#PATCHFILES += cdda2wav_version.patch
##PATCHFILES += change_norwegian_locale.txt
#PATCHFILES += fix_cddb_hidden_tracks.patch
#PATCHFILES += io_compile.patch
#PATCHFILES += parse_version.patch

PATCHFILES += 0001-Upstream-patch-parse-version.patch
PATCHFILES += 0002-Upstream-patch-io-compile.patch
PATCHFILES += 0003-Upstream-patch-cdda2wav-version.patch
PATCHFILES += 0004-Upstream-patch-fix-cddb-hidden-tracks.patch

BUILD_DEP_PKGS += CSWgdkpixbuf

PACKAGES += CSWxcdroast
SPKG_DESC_CSWxcdroast = A GUI wrapper for cdrtools

RUNTIME_DEP_PKGS_CSWxcdroast += CSWglib
RUNTIME_DEP_PKGS_CSWxcdroast += CSWlibintl8
RUNTIME_DEP_PKGS_CSWxcdroast += CSWgtk
RUNTIME_DEP_PKGS_CSWxcdroast += CSWgdkpixbuf

# There are lots of examples with /usr/local and /export/home
CHECKPKG_OVERRIDES_CSWxcdroast += file-with-bad-content

include gar/category.mk

