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
DISTFILES  = $(DISTNAME).tar.gz

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

