# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = inkscape
VERSION = 0.48.4
GARTYPE = v2

DESCRIPTION = Open source scalable vector graphics editor

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

GARCOMPILER = GNU

PATCHFILES += 0000-color-profile.cpp-Add-required-headers.patch
PATCHFILES += 0000-desktop-widget.h-Remove-stray-comma.patch
PATCHFILES += 0000-sp-ellipse.cpp-resolve-overload-ambiguity.patch
PATCHFILES += 0000-fixed_point.h-Resolved-ambiguity.patch
PATCHFILES += 0000-lpe-lattice.cpp-resolve-overload-ambiguity.patch
PATCHFILES += 0000-round.cpp-resolve-overload-ambiguity.patch
PATCHFILES += 0000-svg-length.cpp-resolve-overload-ambiguity.patch

BUILD_DEP_PKGS += CSWlibwpg-dev
BUILD_DEP_PKGS += CSWpm-xml-parser
BUILD_DEP_PKGS += CSWlibgc-dev
BUILD_DEP_PKGS += CSWlibgtkmm-dev
BUILD_DEP_PKGS += CSWliblcms2-dev
BUILD_DEP_PKGS += CSWlibpangomm-dev
BUILD_DEP_PKGS += CSWlibcairomm-dev
BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWlibatk-dev
BUILD_DEP_PKGS += CSWlibatkmm-dev
BUILD_DEP_PKGS += CSWgsl-dev
BUILD_DEP_PKGS += CSWimagemagick-dev


CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-silent-rules

EXTRA_CONFIGURE_EXPORTS += XGETTEXT MSGMERGE MSGFMT
CONFIGURE_ENV_XGETTEXT = $(bindir)/gxgettext
CONFIGURE_ENV_MSGMERGE = $(bindir)/gmsgmerge
CONFIGURE_ENV_MSGFMT = $(bindir)/gmsgfmt

#EXTRA_CONFIGURE_EXPORTS += PROTOC
#CONFIGURE_ENV_PROTOC = $(prefix)/gxx/bin/protoc

# Use this until GCC boost is moved to /opt/csw
EXTRA_INC += $(prefix)/gxx/include
EXTRA_LIB += $(prefix)/gxx/lib

include gar/category.mk

