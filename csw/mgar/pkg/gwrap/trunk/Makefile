# $Id$

NAME = gwrap
VERSION = 1.3.4
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A tool for exporting C libraries into Scheme interpreters
define BLURB
  A tool for exporting C libraries into Scheme interpreters
endef

DISTNAME		=	g-wrap-$(VERSION)
MASTER_SITES	=	http://www.gnucash.org/pub/g-wrap/source/
DISTFILES		=	$(DISTNAME).tar.gz
PATCHFILES		+=	0001-Remove-unused-variable.patch
PATCHFILES		+=	0002-Inhibit-unused-but-set-variable.patch
PATCHFILES		+=	0003-Correct-shell.patch

LICENSE			=	COPYING.LIB

BUILD_DEP_PKGS	+=	CSWglib
BUILD_DEP_PKGS	+=	CSWgtk
BUILD_DEP_PKGS	+=	CSWslib

GARCOMPILER		=	GNU

CONFIGURE_ARGS	=	$(DIRPATHS)

PACKAGES							+=	CSWgwrap-dev
CATALOGNAME_CSWgwrap-dev			=	gwrap_dev
SPKG_DESC_CSWgwrap-dev				+=	$(DESCRIPTION), development files
OBSOLETED_BY_CSWgwrap-dev			=	CSWgwrap
PKGFILES_CSWgwrap-dev				+=	/opt/csw/lib/libgw-glib.so
PKGFILES_CSWgwrap-dev				+=	$(PKGFILES_DEVEL)
PKGFILES_CSWgwrap-dev				+=	/opt/csw/share/info/.*
RUNTIME_DEP_PKGS_CSWgwrap-dev		+=	CSWlibgw-glib0
CHECKPKG_OVERRIDES_CSWgwrap-dev 	+= surplus-dependency|CSWlibgw-glib0
RUNTIME_DEP_PKGS_CSWgwrap-dev		+=	CSWlibgw-standard0
CHECKPKG_OVERRIDES_CSWgwrap-dev 	+= surplus-dependency|CSWlibgw-standard0
RUNTIME_DEP_PKGS_CSWgwrap-dev		+=	CSWlibgw-wct0
CHECKPKG_OVERRIDES_CSWgwrap-dev 	+= surplus-dependency|CSWlibgw-wct0
RUNTIME_DEP_PKGS_CSWgwrap-dev		+=	CSWlibgwrap-glib1
CHECKPKG_OVERRIDES_CSWgwrap-dev 	+= surplus-dependency|CSWlibgwrap-glib1
RUNTIME_DEP_PKGS_CSWgwrap-dev		+=	CSWlibgwrap-wct1
CHECKPKG_OVERRIDES_CSWgwrap-dev 	+= surplus-dependency|CSWlibgwrap-wct1
ARCHALL_CSWgwrap-dev				=	1
CHECKPKG_OVERRIDES_CSWgwrap-dev		+=	archall-devel-package

PACKAGES							+=	CSWlibgw-glib0
CATALOGNAME_CSWlibgw-glib0			=	libgw_glib0
OBSOLETED_BY_CSWlibgw-glib0			=	CSWgwrap
PKGFILES_CSWlibgw-glib0				+=	$(call baseisadirs,$(libdir),libgw-glib\.so\.0\.0\.0)
PKGFILES_CSWlibgw-glib0				+=	$(call baseisadirs,$(libdir),libgw-glib\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgw-glib0			+=	$(DESCRIPTION), libgw-glib.so.0
RUNTIME_DEP_PKGS_CSWlibgw-glib0		+=	CSWglib
RUNTIME_DEP_PKGS_CSWlibgw-glib0		+=	CSWguilelib12

PACKAGES							+=	CSWlibgw-standard0
CATALOGNAME_CSWlibgw-standard0		=	libgw_standard0
OBSOLETED_BY_CSWlibgw-standard0		=	CSWgwrap
PKGFILES_CSWlibgw-standard0			+=	$(call baseisadirs,$(libdir),libgw-standard\.so\.0\.0\.0)
PKGFILES_CSWlibgw-standard0			+=	$(call baseisadirs,$(libdir),libgw-standard\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgw-standard0		+=	$(DESCRIPTION), libgw-standard.so.0
RUNTIME_DEP_PKGS_CSWlibgw-standard0	+=	CSWguilelib12

PACKAGES							+=	CSWlibgw-wct0
CATALOGNAME_CSWlibgw-wct0			=	libgw_wct0
OBSOLETED_BY_CSWlibgw-wct0			=	CSWgwrap
PKGFILES_CSWlibgw-wct0				+=	$(call baseisadirs,$(libdir),libgw-wct\.so\.0\.0\.0)
PKGFILES_CSWlibgw-wct0				+=	$(call baseisadirs,$(libdir),libgw-wct\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgw-wct0				+=	$(DESCRIPTION), libgw-wct.so.0
RUNTIME_DEP_PKGS_CSWlibgw-wct0		+=	CSWguilelib12
RUNTIME_DEP_PKGS_CSWlibgw-wct0		+=	CSWlibgwrap-wct1

PACKAGES							+=	CSWlibgwrap-glib1
CATALOGNAME_CSWlibgwrap-glib1		=	libgwrap_glib1
OBSOLETED_BY_CSWlibgwrap-glib1		=	CSWgwrap
PKGFILES_CSWlibgwrap-glib1			+=	$(call baseisadirs,$(libdir),libgwrap-glib\.so\.1\.0\.0)
PKGFILES_CSWlibgwrap-glib1			+=	$(call baseisadirs,$(libdir),libgwrap-glib\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibgwrap-glib1			+=	$(DESCRIPTION), libgwrap-glib.so.1
RUNTIME_DEP_PKGS_CSWlibgwrap-glib1	+=	CSWguilelib12

PACKAGES							+=	CSWlibgwrap-wct1
CATALOGNAME_CSWlibgwrap-wct1		=	libgwrap_wct1
OBSOLETED_BY_CSWlibgwrap-wct1		=	CSWgwrap
PKGFILES_CSWlibgwrap-wct1			+=	$(call baseisadirs,$(libdir),libgwrap-wct\.so\.1\.0\.0)
PKGFILES_CSWlibgwrap-wct1			+=	$(call baseisadirs,$(libdir),libgwrap-wct\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibgwrap-wct1			+=	$(DESCRIPTION), libgwrap-wct.so.1
RUNTIME_DEP_PKGS_CSWlibgwrap-wct1	+=	CSWguilelib12

include gar/category.mk

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
