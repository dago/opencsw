# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = ncsa-mosaic
VERSION = 2.7b6
PACKAGES = CSWncsa-mosaic
CATALOGNAME_CSWncsa-mosaic = ncsa_mosaic
CATEGORIES = apps
GARTYPE = v2
GIT_REPOS = git://github.com/alandipert/ncsa-mosaic.git
DESCRIPTION = The web browser credited with popularizing the World Wide Web
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
define BLURB
endef
SPKG_SOURCEURL = http://github.com/alandipert/ncsa-mosaic
MASTER_SITES =
PATCHFILES += 0001-Copying-Makefile.linux-to-Makefile.sun.patch
PATCHFILES += 0002-Got-it-to-build-with-gnulib-stuff.patch
PATCHFILES += 0003-set-runtime-lib-search-path.patch
PATCHFILES += 0005-Adding-opt-csw-include-lib-for-png.h.patch
PATCHFILES += 0006-sys-inttypes.h-instead-of-stdint.h.patch
PATCHFILES += 0007-Adding-opt-csw-include-for-png.patch

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = mosaic
INSTALL_SCRIPTS = mosaic
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS_CSWncsa-mosaic += CSWlibice
RUNTIME_DEP_PKGS_CSWncsa-mosaic += CSWlibsm
RUNTIME_DEP_PKGS_CSWncsa-mosaic += CSWlibx11
RUNTIME_DEP_PKGS_CSWncsa-mosaic += CSWlibxext
RUNTIME_DEP_PKGS_CSWncsa-mosaic += CSWlibxmu
RUNTIME_DEP_PKGS_CSWncsa-mosaic += CSWlibxpm
RUNTIME_DEP_PKGS_CSWncsa-mosaic += CSWlibxt
RUNTIME_DEP_PKGS_CSWncsa-mosaic += CSWjpeg
RUNTIME_DEP_PKGS_CSWncsa-mosaic += CSWpng
RUNTIME_DEP_PKGS_CSWncsa-mosaic += CSWzlib

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWncsa-mosaic)
LICENSE = COPYRIGHT

include gar/category.mk

build-mosaic:
	(cd $(WORKSRC); gmake sun)
	@$(MAKECOOKIE)

install-mosaic:
	ginstall -m 755 -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/src/Mosaic $(DESTDIR)$(bindir)
	@$(MAKECOOKIE)
