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

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU
EXTRA_LINKER_FLAGS	=	-lintl
CONFIGURE_ARGS	+=	\
					--without-included-gettext \
					--with-libintl-prefix=/opt/csw
BUILD_DEP_PKGS		=	\
						CSWggettext-dev \
						CSWlibthaidevel \
						CSWlibotf-dev
RUNTIME_DEP_PKGS	=	\
						CSWggettext \
						CSWlibthai \
						CSWlibotf
PACKAGES							+=	CSWlibn17n0
SPKG_DESC_CSWlibn17n0				+=	A multilingual text processing library for the C language - runtime.
PKGFILES_CSWlibn17n0				+=	$(call pkgfiles_lib,libm17n-core.so.0.4.0) $(call pkgfiles_lib,libm17n-flt.so.0.4.0) $(call pkgfiles_lib,libm17n-gui.so.0.4.0) $(call pkgfiles_lib,libm17n.so.0.4.0) $(call pkgfiles_lib,m17n/1.0/libm17n-X.so) $(call pkgfiles_lib,m17n/1.0/libm17n-gd.so) $(call pkgfiles_lib,m17n/1.0/libmimx-anthy.so) $(call pkgfiles_lib,m17n/1.0/libmimx-ispell.so)
PACKAGES							+=	CSWlibn17n-dev
SPKG_DESC_CSWlibn17n-dev			+=	A multilingual text processing library for the C language - development.
PKGFILES_CSWlibn17n-dev				=	$(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibn17n-dev		+=	CSWlibn17n0

PACKAGES							+=	CSWlibn17n-utils
SPKG_DESC_CSWlibn17n-utils			+=	A multilingual text processing library for the C language - utilities.
RUNTIME_DEP_PKGS_CSWlibn17n-utils	+=	CSWlibn17n0

include gar/category.mk

