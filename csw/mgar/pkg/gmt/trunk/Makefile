# Copyright 2011 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = gmt
VERSION = 4.5.7
CATEGORIES = apps
DESCRIPTION = Generic Mapping Tools
define BLURB
  GMT is an open source collection of ~60 tools for manipulating geographic and Cartesian data sets (including filtering, trend fitting, gridding, projecting, etc.) and producing Encapsulated PostScript File (EPS) illustrations ranging from simple x-y plots via contour maps to artificially illuminated surfaces and 3-D perspective views. GMT supports ~30 map projections and transformations and comes with support data such as GSHHS coastlines, rivers, and political boundaries. GMT is developed and maintained by Paul Wessel and Walter H. F. Smith with help from a global set of volunteers, and is supported by the National Science Foundation. It is released under the GNU General Public License. 
endef

SPKG_SOURCEURL = http://gmt.soest.hawaii.edu/
MASTER_SITES += ftp://ftp.soest.hawaii.edu/gmt4/

DISTFILES += $(NAME)-$(VERSION).tar.bz2
UFILES_REGEX = GMT(\d+(?:\.\d+)*)_(.*).tar.bz2

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWnetcdf-dev CSWnetcdf

PACKAGES += CSWgmt
CATALOGNAME_CSWgmt = gmt
SPKG_DESC_CSWgmt = Generic Mapping Tools
RUNTIME_DEP_PKGS_CSWgmt += CSWlibnetcdf7
RUNTIME_DEP_PKGS_CSWgmt += CSWsunmath

PACKAGES += CSWgmt-doc
CATALOGNAME_CSWgmt-doc = gmt_doc
SPKG_DESC_CSWgmt-doc = Documentation for GMT
PKGFILES_CSWgmt-doc += /opt/csw/share/doc/gmt
PKGFILES_CSWgmt-doc += /opt/csw/share/doc/gmt/.*
ARCHALL_CSWgmt-doc = 1


## GMT Includes no unit tests
TEST_SCRIPTS =

## GMT still doesn't use the GNU convention for unpacked tarballs
DISTNAME = GMT$(VERSION)

## Tell the build process where to find NETCDF for 32 and 64-bit builds
NETCDF_LIBDIR=/opt/csw/lib/$(MM_LIBDIR)
## Tell the build process where to find libsunmath and libm
SUNMATH_LIBDIR=/opt/csw/lib/$(MM_LIBDIR)

## Banish the unversioned shared objects to their own tree
# The merge step moves things into the proper ISA-specific directory
#libdir     = $(exec_prefix)/lib/gmt
libdir_install = $(exec_prefix)/lib/gmt
EXTRA_LDFLAGS += -R $(libdir)/$(MM_LIBDIR)

## GMT spews a number of directories into share
datadir = /opt/csw/share/gmt

## $(GMT_LIBS) gets passed to ./configure as LIBS
## src/Makefile doesn't use LDFLAGS so we hijack $(LIBS) to fix the RUNPATH
## We could also use LD_OPTS, but that would require reverse-engineering the
## output of ./configure for yet another variable
GMT_LIBS += -R$(libdir)/$(MM_LIBDIR)
## GMT wants to use libsunmath and libm, but the ./configure script isn't
## able to figure out where those libs actually live
## The -L must come before the -l statements
GMT_LIBS += -L$(SUNMATH_LIBDIR) -lsunmath -lm

## Arguments passed to the ./configure script. Configure ignores the various
## environment variables so we have to pass CFLAGS and friends
CONFIGURE_ARGS += NETCDF_LIB=$(NETCDF_LIBDIR)
CONFIGURE_ARGS += CFLAGS="$(CFLAGS)"
CONFIGURE_ARGS += LDFLAGS="$(LDFLAGS)"
CONFIGURE_ARGS += CXXFLAGS="$(CXXFLAGS)"
CONFIGURE_ARGS += LIBS="$(GMT_LIBS)"
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-mex
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --enable-netcdf=/opt/csw


## Attempt to build this 64-bit
BUILD64 = 1

GARCOMPILER = GCC4

INSTALL_ARGS = install-all

LICENSE = LICENSE.TXT

CHECKPKG_OVERRIDES_CSWgmt-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/gmt/html/GMT_Docs/node257.html

include gar/category.mk

# This post-install-modulated step must come after we "include gar/category.mk"
post-install-modulated:
	@echo Creating architecture symlinks
	ln -s $(ISA_DEFAULT) $(DESTDIR)/opt/csw/lib/gmt/32
	ln -s $(ISA_DEFAULT64) $(DESTDIR)/opt/csw/lib/gmt/64
	@$(MAKECOOKIE)

# TODO: post-merge, search for anything in /opt/csw/bin/64 that isn't a 
# binary and nuke it so that things like shell scripts don't get ISAEXEC'd
