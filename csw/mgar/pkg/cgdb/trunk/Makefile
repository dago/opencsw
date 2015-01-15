# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = cgdb
VERSION = 0.6.8
GARTYPE = v2

DESCRIPTION = The curses debugger

MASTER_SITES = http://cgdb.me/files/
DISTFILES += $(DISTNAME).tar.gz

PACKAGES += CSWcgdb
SPKG_DESC_CSWcgdb = The curses debugger
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWcgdb += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWcgdb += CSWlibreadline6

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ncurses=$(prefix)

include gar/category.mk

