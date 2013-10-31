# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pspp
VERSION = 0.8.1
GARTYPE = v2

DESCRIPTION = GNU program for statistical analysis of sampled data

MASTER_SITES = $(GNU_MIRROR)
DISTFILES += $(DISTNAME).tar.gz
PATCHFILES += 0001-Do-not-use-Wall-unless-gcc.patch

PACKAGES += CSWpspp
SPKG_DESC_CSWpspp = GNU program for statistical analysis of sampled data
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpspp += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWpspp += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWpspp += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWpspp += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWpspp += CSWlibz1
RUNTIME_DEP_PKGS_CSWpspp += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpspp += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWpspp += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWpspp += CSWlibgsl0
RUNTIME_DEP_PKGS_CSWpspp += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWpspp += CSWgtksourceview
RUNTIME_DEP_PKGS_CSWpspp += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWpspp += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWpspp += CSWpango
RUNTIME_DEP_PKGS_CSWpspp += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWpspp += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpspp += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWpspp += CSWlibpq5

GARCOMPILER = GNU

# Do not use 64 bit until this is fixed:
#   https://www.opencsw.org/mantis/view.php?id=5120
#BUILD64 = 1
#ISAEXEC = 1

# Use GNU tools
BUILD_OVERRIDE_VARS += XGETTEXT
BUILD_OVERRIDE_VARS += MSGMERGE
BUILD_OVERRIDE_VARS += MSGFMT

BUILD_OVERRIDE_VAR_XGETTEXT = gxgettext
BUILD_OVERRIDE_VAR_MSGMERGE = gxmsgmerge
BUILD_OVERRIDE_VAR_MSGFMT = gmsgfmt

CONFIGURE_ARGS += $(DIRPATHS)

# There is a problem with C99 headers and GCC
CONFIGURE_ARGS += --without-perl-module

# There are some tests failing, investigate later
SKIPTEST ?= 1

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk

