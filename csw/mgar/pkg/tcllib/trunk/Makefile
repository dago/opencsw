# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tcllib
VERSION = 1.13
GARTYPE = v2
CATEGORIES = lang
ARCHALL_CSWtcllib = 1
LICENSE = license.terms

DESCRIPTION = Standard Tcl library, collection of common utility functions and modules
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES = 0001-csw-path-changes.patch 0002-renamed-conflicting-man-pages.patch

# comment contains "/usr/share/misc/magic.mime"
CHECKPKG_OVERRIDES_CSWtcllib += file-with-bad-content|/usr/share|root/opt/csw/lib/tcllib1.13/fumagic/filetypes.tcl
CHECKPKG_OVERRIDES_CSWtcllib += file-with-bad-content|/usr/share|root/opt/csw/lib/tcllib1.13/fumagic/mimetypes.tcl

# list of shells containing "/usr/local/bin/bash" and others
CHECKPKG_OVERRIDES_CSWtcllib += file-with-bad-content|/usr/local|root/opt/csw/lib/tcllib1.13/fumagic/filetypes.tcl
CHECKPKG_OVERRIDES_CSWtcllib += file-with-bad-content|/usr/local|root/opt/csw/lib/tcllib1.13/fumagic/mimetypes.tcl

# comment contains "/usr/share/misc/file/magic"
CHECKPKG_OVERRIDES_CSWtcllib += file-with-bad-content|/usr/share|root/opt/csw/lib/tcllib1.13/fumagic/cfront.tcl

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE=./configure --prefix=/opt/csw

include gar/category.mk

