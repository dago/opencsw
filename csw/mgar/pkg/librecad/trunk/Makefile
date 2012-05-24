# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = LibreCAD
VERSION = 1.0.2
GIT_VERSION = 216dc66b2a
GARTYPE = v2
CATEGORIES = gnome

DESCRIPTION = libreCAD - based on QCAD 2.0
define BLURB
  LibreCAD is a free Open Source CAD application for Windows, Apple and Linux. Support and documentation is free from our large, dedicated community of users, contributors and developers
endef

LICENSE += LICENSE
LICENSE += gpl-2.0.txt
LICENSE += gpl-2.0greater.txt
LICENSE += LICENSE_Apache2.txt
LICENSE += LICENSE_GPLv3.txt

# git clone https://github.com/LibreCAD/LibreCAD.git
# https://github.com/LibreCAD/LibreCAD/tarball/master
MASTER_SITES = 
# DISTFILES  = $(DISTNAME).tar.gz
GIT_REPOS = http://github.com/LibreCAD/LibreCAD.git
GIT_USE_PROXY = 1
# GIT_TREEISH_LibreCAD.git = $(GIT_VERSION)

GARCOMPILER = GNU
prefix = $(BUILD_PREFIX)/gxx
PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

PATCHFILES += 0000-adjust-for-csw-environment.patch
PATCHFILES += 0000-add-csw-settings.patch

BUILD_DEP_PKGS += CSWqt4-gxx-dev
BUILD_DEP_PKGS += CSWmuparser-dev
BUILD_DEP_PKGS += CSWboost-gcc-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS = custom

configure-custom: 
	cd $(WORKSRC) && $(bindir)/qmake $(call tolower,$(NAME)).pro

include gar/category.mk

