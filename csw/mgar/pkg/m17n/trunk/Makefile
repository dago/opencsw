# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = m17n
VERSION = 1.6.4
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A multilingual text processing library for the C language.
define BLURB
    An open source software for any Linux/Unix applications which
	realizes multilingualization of many aspects of applications.

    It represents multilingual text as an object named M-text.
	M-text is a string with attributes called text properties,
	and designed to substitute for string in C.
	Text properties carry any information required to input, display
	and edit the text.
endef

MASTEdownload.savannah.gnu.org/releases/m17nm17n-lib-download/

DISTNAME	=	$(NAME)-lib-$(VERSION)
DISTFILES	=	$(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU
EXTRA_LINKER_FLAGS	=	-lintl
CONFIGURE_ARGS	+=	\
					--without-included-gettext \
					--with-libintl-prefix=/opt/csw+=	CSWfconfig
BUILD_DEP_PKGS		+=	CSWlibbz2-dev
BUILD_DEP_PKGS		+=	CSWlibdatrie-dev
BUILD_DEP_PKGS		+=	CSWlibexpat-dev
BUILD_DEP_PKGS		+=	CSWlibfreetype-dev
BUILD_DEP_PKGS		+=	CSWlibfribidi-dev
BUILD_DEP_PKGS		+=	CSWlibiconv-dev
BUILD_DEP_PKGS		+=	CSWlibthai-dev
BUILD_DEP_PKGS		+=	CSWlibotf-dev
BUILD_DEP_PKGS		+=	CSWlibxft2devel
BUILD_DEP_PKGS		+=	CSWlibxml2-dev
BUILD_DEP_PKGS		+=	CSWlibxrenderdevel
BUILD_DEP_PKGS		+=	CSWlibz-dev

PACKAGES							+=	CSWlibm17n-utils
SPKG_DESC_CSWlibm17n-utils			+=	$(DESCRIPTION) - utilities.dRUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibm17n-core0
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibm17n-flt0
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibm17n-gui0
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibm17n0
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibthai0
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibxft2
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibgd2
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibotf-utils
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	CSWlibfribidi0

PACKAGES						+=	CSWlibm17n-core0
CATALOGNAME_CSWlibm17n-core0	=	libm17n_core0
PKGFILES_CSWlibm17n-core0		+=	$(call baseisadirs,$(libdir),libm17n-core\.so\.0\.4\.0)
PKGFILES_CSWlibm17n-core0		+=	$(call baseisadirs,$(libdir),libm17n-core\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibm17n-core0		+=	$(DESCRIPTION), libm17n-core.so.0

PACKAGES					+=	CSWlibm17n-flt0
CATALOGNAME_CSWlibm17n-flt0	=	libm17n_flt0
PKGFILES_CSWlibm17n-flt0	+=	$(call baseisadirs,$(libdir),libm17n-flt\.so\.0\.4\.0)
PKGFILES_CSWlibm17n-flt0	+=	$(call baseisadirs,$(libdir),libm17n-flt\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibm17n-flt0	+=	$(DESCRIPTION), libm17n-flt.so.0

PACKAGES					+=	CSWlibm17n-gui0
CATALOGNAME_CSWlibm17n-gui0	=	libm17n_gui0
PKGFILES_CSWlibm17n-gui0	+=	$(call baseisadirs,$(libdir),libm17n-gui\.so\.0\.4\.0)
PKGFILES_CSWlibm17n-gui0	+=	$(call baseisadirs,$(libdir),libm17n-gui\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibm17n-gui0	+=	$(DESCRIPTION), libm17n-gui.so.0

PACKAGES				+=	CSWlibm17n0
CATALOGNAME_CSWlibm17n0	=	libm17n0
PKGFILES_CSWlibm17n0	+=	$(call baseisadirs,$(libdir),libm17n\.so\.0\.4\.0)
PKGFILES_CSWlibm17n0	+=	$(call baseisadirs,$(libdir),libm17n\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibm17n0	+=	$(DESCRIPTION), libm17n.so.0d=CSWlibm17n-gui0

PACKAGES							+=	CSWlibm17n-dev
SPKG_DESC_CSWlibm17n-dev			+=	$(DESCRIPTION) - development.
PKGFILES_CSWlibm17n-dev				=	$itecture neutral
CHECKPKG_OVERRIDES_CSWlibm17n-dev 	+= 	archall-devel-package
ARCHALL_CSWliRUNTIME_DEP_PKGS_CSWlibm17n-dev		+=	CSWlibm17n0
CHECKPKG_OVERRIDES_CSWlibm17n-dev	+=	file-with-bad-content|/usr/local|root/opt/csw/bin/m17n-configibency|CSWfconfig

include gar/category.mk

# this is private and not available publicly yet
mydependencies:
	$(HOME)/bin/ocswdeplist -