# $Id: Makefile 16916 2012-01-26 13:25:13Z dmichelsen $
NAME = gedit
VERSION = 2.30.4
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = The official GNOME text editor
define BLURB
endef

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGES += CSWgedit
RUNTIME_DEP_PKGS_CSWgedit += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgedit += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWgedit += CSWperl

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
