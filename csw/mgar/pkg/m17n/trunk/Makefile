# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = m17n
VERSION = 1.6.3
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

MASTER_SITES = http://www.m17n.org/m17n-lib-download/

DISTNAME	=	$(NAME)-lib-$(VERSION)
DISTFILES	=	$(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU
EXTRA_LINKER_FLAGS	=	-lintl
CONFIGURE_ARGS	+=	\
					--without-included-gettext \
					--with-libintl-prefix=/opt/csw
BUILD_DEP_PKGS		=	\
						CSWfconfig \
						CSWfribidi \
						CSWlibbz2-dev \
						CSWlibdatrie-dev \
						CSWlibexpat-dev \
						CSWlibfreetype-dev \
						CSWlibiconv-dev \
						CSWlibthaidevel \
						CSWlibotf-dev \
						CSWlibxft2devel \
						CSWlibxml2-dev \
						CSWlibxrenderdevel \
						CSWlibz-dev

PACKAGES							+=	CSWlibm17n0
SPKG_DESC_CSWlibm17n0				+=	$(DESCRIPTION) - runtime.
PKGFILES_CSWlibm17n0				+=	$(call pkgfiles_lib,libm17n-core.so.0.4.0) $(call pkgfiles_lib,libm17n-flt.so.0.4.0) $(call pkgfiles_lib,libm17n-gui.so.0.4.0) $(call pkgfiles_lib,libm17n.so.0.4.0) $(call pkgfiles_lib,m17n/1.0/libm17n-X.so) $(call pkgfiles_lib,m17n/1.0/libm17n-gd.so) $(call pkgfiles_lib,m17n/1.0/libmimx-anthy.so) $(call pkgfiles_lib,m17n/1.0/libmimx-ispell.so)
OBSOLETED_BY_CSWlibm17n0 			+=	CSWlibm17n
RUNTIME_DEP_PKGS_CSWlibm17n0		+=	\
										CSWfconfig \
										CSWfribidi \
										CSWlibbz2-1-0 \
										CSWlibdatrie1 \
										CSWlibexpat1 \
										CSWlibfreetype6 \
										CSWlibgcc-s1 \
										CSWlibiconv2 \
										CSWlibintl8 \
										CSWlibotf0 \
										CSWlibthai \
										CSWlibxft2 \
										CSWlibxml2-2 \
										CSWlibxrender \
										CSWlibz1

PACKAGES							+=	CSWlibm17n-dev
SPKG_DESC_CSWlibm17n-dev			+=	$(DESCRIPTION) - development.
PKGFILES_CSWlibm17n-dev				=	$(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibm17n-dev		+=	\
										CSWlibm17n0
OBSOLETED_BY_CSWlibm17n-dev			+=	CSWlibm17ndevel

PACKAGES							+=	CSWlibm17n-utils
SPKG_DESC_CSWlibm17n-utils			+=	$(DESCRIPTION) - utilities.
OBSOLETED_BY_CSWlibm17n-utils		+=	CSWlibm17n
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	\
										CSWlibm17n0

include gar/category.mk

