# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = wmctrl
VERSION = 1.07
GARTYPE = v2

DESCRIPTION = Command-line tool to interact with the X Window Manager
define BLURB
  wmctrl provides command line access to almost all the features
  defined in the EWMH specification. It can be used, for example, to
  get information about the window manager, to get a detailed list of
  desktops and managed windows, to switch and resize desktops, to make
  windows full-screen, always-above or sticky, and to activate, close,
  move, resize, maximize and minimize them.
endef

MASTER_SITES = http://tomas.styblo.name/wmctrl/dist/
DISTFILES  = $(DISTNAME).tar.gz
LICENSE = COPYING

RUNTIME_DEP_PKGS_CSWwmctrl += CSWlibglib2-0-0 CSWlibintl8

PATCHFILES += 0001-remove-gcc-specific-flags.patch
CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
