# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = feh
VERSION = 2.9.3
GARTYPE = v2

DESCRIPTION = X11 image viewer aimed mostly at console users

VENDOR_URL = http://feh.finalrewind.org/
MASTER_SITES = http://feh.finalrewind.org/
DISTFILES  = $(DISTNAME).tar.bz2

PATCHFILES += 0001-config.mk-adjustments-prefix-compilation.patch

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS =

# Test turned off for now. Error: "Can't locate Test/Command.pm in @INC"
TEST_SCRIPTS =
# TEST_TARGET = test

GARCOMPILER = GNU

RUNTIME_DEP_PKGS_CSWfeh += CSWlibimlib2-1
RUNTIME_DEP_PKGS_CSWfeh += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWfeh += CSWlibgiblib1
RUNTIME_DEP_PKGS_CSWfeh += CSWlibcurl4

include gar/category.mk
