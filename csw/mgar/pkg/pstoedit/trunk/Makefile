# $Id$

NAME = pstoedit
VERSION = 3.60
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Translates PostScript and PDF files to editable vector graphics converter
define BLURB
  translates PostScript and PDF graphics into other vector formats.
endef

MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES		=	$(DISTNAME).tar.gz

BUILD_DEP_PKGS		+=	CSWimagemagick-dev
BUILD_DEP_PKGS		+=	CSWlibgd-dev
BUILD_DEP_PKGS		+=	CSWplotutils-dev
BUILD_DEP_PKGS		+=	CSWbison

GARCOMPILER			=	GNU

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-libplot
CONFIGURE_ARGS	+=	--without-emf
CONFIGURE_ARGS	+=	--without-swf

LICENSE			=	copying

PACKAGES								+=	CSWpstoedit
CATALOGNAME_CSWpstoedit					=	pstoedit
SPKG_DESC_CSWpstoedit					=	$(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWpstoedit			+=	CSWlibpstoedit0
RUNTIME_DEP_PKGS_CSWpstoedit			+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpstoedit			+=	CSWlibgd2
RUNTIME_DEP_PKGS_CSWpstoedit			+=	CSWlibmagick++5
RUNTIME_DEP_PKGS_CSWpstoedit			+=	CSWlibmagickcore5
RUNTIME_DEP_PKGS_CSWpstoedit			+=	CSWlibplotter2
RUNTIME_DEP_PKGS_CSWpstoedit			+=	CSWlibstdc++6

PACKAGES								+=	CSWlibpstoedit0
CATALOGNAME_CSWlibpstoedit0				=	libpstoedit0
PKGFILES_CSWlibpstoedit0				+=	$(call baseisadirs,$(libdir),libpstoedit\.so\.0\.0\.0)
PKGFILES_CSWlibpstoedit0				+=	$(call baseisadirs,$(libdir),libpstoedit\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibpstoedit0				+=	$(DESCRIPTION), libpstoedit.so.0
OBSOLETED_BY_CSWlibpstoedit0			=	CSWpstoeditrt
CATALOGNAME_CSWpstoeditrt				=	pstoedit_rt_stub
RUNTIME_DEP_PKGS_CSWlibpstoedit0		+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibpstoedit0		+=	CSWlibgd2
RUNTIME_DEP_PKGS_CSWlibpstoedit0		+=	CSWlibstdc++6

PACKAGES								+=	CSWpstoedit-dev
CATALOGNAME_CSWpstoedit-dev				=	pstoedit_dev
SPKG_DESC_CSWpstoedit-dev				+=	$(DESCRIPTION), development files
PKGFILES_CSWpstoedit-dev				+=	/opt/csw/lib/libpstoedit.so
PKGFILES_CSWpstoedit-dev				+=	$(PKGFILES_DEVEL)
ARCHALL_CSWpstoedit-dev					=	1
CHECKPKG_OVERRIDES_CSWpstoedit-dev		+=	archall-devel-package
OBSOLETED_BY_CSWpstoedit-dev			=	CSWpstoeditdevel
CATALOGNAME_CSWpstoeditdevel			=	pstoedit_devel_stub
RUNTIME_DEP_PKGS_CSWpstoedit-dev		+=	CSWlibpstoedit0

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/php5/bin:$(PATH)

openmpList	=	\
				Makefile \
				config/Makefile \
				msdev/Makefile \
				misc/swffonts/Makefile \
				misc/Makefile \
				m4/Makefile \
				othersrc/gsdllinc/Makefile \
				othersrc/Makefile \
				contrib/java/java2/Makefile \
				contrib/java/Makefile \
				contrib/java/java1/Makefile \
				contrib/Makefile \
				contrib/cairo/Makefile \
				src/Makefile \
				examples/Makefile \
				doc/Makefile \
				os2/Makefile

post-configure-modulated:
	cd $(WORKSRC) && sed --in-place --expression='s/ -xopenmp//' $(openmpList)
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
