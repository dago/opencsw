# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = fluxbox
VERSION = 1.3.2
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Brief description
define BLURB
  Long description
endef

VENDOR_URL = http://fluxbox.org/
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

EXTRA_CPPFLAGS = -features=extensions -D__FUNCTION__=__func__
EXTRA_LINKER_FLAGS = -norunpath

PATCHFILES += 0001-Use-gwhoami-from-CSWcoreutils.patch

CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS_CSWfluxbox += CSWcoreutils
RUNTIME_DEP_PKGS_CSWfluxbox += CSWimlib2
RUNTIME_DEP_PKGS_CSWfluxbox += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWfluxbox += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWfluxbox += CSWlibfribidi0
RUNTIME_DEP_PKGS_CSWfluxbox += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWfluxbox += CSWlibxft2
RUNTIME_DEP_PKGS_CSWfluxbox += CSWlibxrender
RUNTIME_DEP_PKGS_CSWfluxbox += CSWlibz1
RUNTIME_DEP_PKGS_CSWfluxbox += CSWxpm
CHECKPKG_OVERRIDES_CSWfluxbox += file-with-bad-content|/usr/share|root/opt/csw/share/man/man5/fluxbox-style.5
CHECKPKG_OVERRIDES_CSWfluxbox += file-with-bad-content|/usr/share|root/opt/csw/bin/fluxbox-generate_menu
CHECKPKG_OVERRIDES_CSWfluxbox += file-with-bad-content|/usr/local|root/opt/csw/bin/fluxbox-generate_menu
CHECKPKG_OVERRIDES_CSWfluxbox += file-with-bad-content|/usr/local|root/opt/csw/bin/fbsetbg
CHECKPKG_OVERRIDES_CSWfluxbox += surplus-dependency|CSWcoreutils

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
