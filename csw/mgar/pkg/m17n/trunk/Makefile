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
						CSWlibbz2-dev \
						CSWlibdatrie-dev \
						CSWlibexpat-dev \
						CSWlibfreetype-dev \
						CSWlibfribidi-dev \
						CSWlibiconv-dev \
						CSWlibthai-dev \
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
										CSWlibbz2-1-0 \
										CSWlibdatrie1 \
										CSWlibexpat1 \
										CSWlibfreetype6 \
										CSWlibfribidi0 \
										CSWlibgcc-s1 \
										CSWlibiconv2 \
										CSWlibintl8 \
										CSWlibotf0 \
										CSWlibthai0 \
										CSWlibxft2 \
										CSWlibxml2-2 \
										CSWlibxrender \
										CSWlibz1
# added this overrides because checkpkg evaluates them incorrectly,
# e.g. libthai0 doesn't exist and how the heck it determines that it
# depends on libgs2?
# Remark: checkpkg doesn't support multi-line macro-commands...
CHECKPKG_OVERRIDES_CSWlibm17n0		+=	missing-dependency|CSWlibm17n-utils
CHECKPKG_OVERRIDES_CSWlibm17n0		+=	missing-dependency|CSWlibgd2
CHECKPKG_OVERRIDES_CSWlibm17n0		+=	missing-dependency|CSWlibotf-utils
CHECKPKG_OVERRIDES_CSWlibm17n0		+=	surplus-dependency|CSWlibdatrie1
CHECKPKG_OVERRIDES_CSWlibm17n0		+=	surplus-dependency|CSWlibexpat1
CHECKPKG_OVERRIDES_CSWlibm17n0		+=	surplus-dependency|CSWlibthai0
CHECKPKG_OVERRIDES_CSWlibm17n0		+=	surplus-dependency|CSWlibotf0
CHECKPKG_OVERRIDES_CSWlibm17n0		+=	surplus-dependency|CSWlibfribidi0
CHECKPKG_OVERRIDES_CSWlibm17n0		+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libm17n-core.so.0.4.0|soname=libm17n-core.so.0|pkgname=CSWlibm17n0|expected=CSWlibm17n-core0
CHECKPKG_OVERRIDES_CSWlibm17n0		+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libm17n-flt.so.0.4.0|soname=libm17n-flt.so.0|pkgname=CSWlibm17n0|expected=CSWlibm17n-flt0
CHECKPKG_OVERRIDES_CSWlibm17n0		+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libm17n-gui.so.0.4.0|soname=libm17n-gui.so.0|pkgname=CSWlibm17n0|expected=CSWlibm17n-gui0

PACKAGES							+=	CSWlibm17n-dev
SPKG_DESC_CSWlibm17n-dev			+=	$(DESCRIPTION) - development.
PKGFILES_CSWlibm17n-dev				=	$(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibm17n-dev		+=	\
										CSWlibm17n0
OBSOLETED_BY_CSWlibm17n-dev			+=	CSWlibm17ndevel
CHECKPKG_OVERRIDES_CSWlibm17n-dev	+=	file-with-bad-content|/usr/local|root/opt/csw/bin/m17n-config
# why this? especially when the package is declared architecture neutral
CHECKPKG_OVERRIDES_CSWlibm17n-dev 	+= 	archall-devel-package
ARCHALL_CSWlibm17n-dev				=	1

PACKAGES							+=	CSWlibm17n-utils
SPKG_DESC_CSWlibm17n-utils			+=	$(DESCRIPTION) - utilities.
OBSOLETED_BY_CSWlibm17n-utils		+=	CSWlibm17n
RUNTIME_DEP_PKGS_CSWlibm17n-utils	+=	\
										CSWlibm17n0

# added this overrides because checkpkg evaluates them incorrectly,
# i.e., doesn't use transitivity:
# Remark: checkpkg doesn't support multi-line macro-commands...
CHECKPKG_OVERRIDES_CSWlibm17n-utils	+=	missing-dependency|CSWlibthai0
CHECKPKG_OVERRIDES_CSWlibm17n-utils	+=	missing-dependency|CSWlibbz2-1-0
CHECKPKG_OVERRIDES_CSWlibm17n-utils	+=	missing-dependency|CSWlibfribidi0
CHECKPKG_OVERRIDES_CSWlibm17n-utils	+=	missing-dependency|CSWlibiconv2
CHECKPKG_OVERRIDES_CSWlibm17n-utils	+=	missing-dependency|CSWlibotf-utils
CHECKPKG_OVERRIDES_CSWlibm17n-utils	+=	missing-dependency|CSWlibz1
CHECKPKG_OVERRIDES_CSWlibm17n-utils	+=	missing-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWlibm17n-utils	+=	missing-dependency|CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWlibm17n-utils	+=	missing-dependency|CSWlibgd2
CHECKPKG_OVERRIDES_CSWlibm17n-utils	+=	missing-dependency|CSWlibxml2-2
CHECKPKG_OVERRIDES_CSWlibm17n-utils	+=	missing-dependency|CSWfconfig

include gar/category.mk

# this is private and not available publicly yet
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
