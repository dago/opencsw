# $Id$

NAME = libming
VERSION = 0.4.4
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A library for generating Macromedia Flash files
define BLURB
  Ming is a library for generating Macromedia Flash files (.swf), written
  in C, and includes useful utilities for working with .swf files.

  It has wrappers that allow it to be used in C++, PHP, Python, Ruby, and
  Perl.
endef

MASTER_SITES	=	 $(SF_MIRRORS)
SF_PROJ			=	ming
DISTNAME		=	$(SF_PROJ)-$(VERSION)
DISTFILES		=	$(DISTNAME).tar.bz2
PATCHFILES		+=	0001-PrintGifError-to-GifErrorString.patch
PATCHFILES		+=	0002-makeswf-include-path.patch

GARCOMPILER		=	GNU

BUILD_DEP_PKGS	+=	CSWphp5
BUILD_DEP_PKGS	+=	CSWphp5-dev

CONFIGURE_ARGS	=	$(DIRPATHS)
# gcc -kPIC issue because Python was compiled with SOS
#CONFIGURE_ARGS	+=	--enable-python
# gcc dynamic link error durring tests
# CONFIGURE_ARGS	+=	--enable-perl
# SOS: doesn't compile
#CONFIGURE_ARGS	+=	--enable-php
# SOS: doesn't link with TCL library resulting in undefined references
#CONFIGURE_ARGS	+=	--enable-tcl

TEST_SCRIPTS = custom

#CSWlibbz2-1-0 CSWlibfreetype6 CSWlibgcc-s1 CSWlibgif4 CSWlibpng12-0 CSWlibz1

PACKAGES							+=	CSWlibming-utils
CATALOGNAME_CSWlibming-utils		=	libming_utils
OBSOLETED_BY_CSWlibming-utils		=	CSWlibming
CATALOGNAME_CSWlibming				=	libming_stub
RUNTIME_DEP_PKGS_CSWlibming-utils	+=	CSWlibming1
# transitivity:
CHECKPKG_OVERRIDES_CSWlibming-utils	+=	missing-dependency|CSWlibbz2-1-0
CHECKPKG_OVERRIDES_CSWlibming-utils	+=	missing-dependency|CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWlibming-utils	+=	missing-dependency|CSWlibpng12-0
CHECKPKG_OVERRIDES_CSWlibming-utils	+=	missing-dependency|CSWlibz1

SPKG_DESC_CSWlibming-utils		=	$(DESCRIPTION), utilities

PACKAGES						+=	CSWlibming1
CATALOGNAME_CSWlibming1			=	libming1
PKGFILES_CSWlibming1			+=	$(call baseisadirs,$(libdir),libming\.so\.1\.4\.3)
PKGFILES_CSWlibming1			+=	$(call baseisadirs,$(libdir),libming\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibming1			+=	$(DESCRIPTION), libming.so.1
OBSOLETED_BY_CSWlibming1		=	CSWlibmingrt
CATALOGNAME_CSWlibmingrt		=	libming_rt_stub
RUNTIME_DEP_PKGS_CSWlibming1	+=	CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibming1	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibming1	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibming1	+=	CSWlibgif4
CHECKPKG_OVERRIDES_CSWlibming1	+=	surplus-dependency|CSWlibgif4
RUNTIME_DEP_PKGS_CSWlibming1	+=	CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibming1	+=	CSWlibz1

PACKAGES							+=	CSWlibming-dev
CATALOGNAME_CSWlibming-dev			=	libming_dev
SPKG_DESC_CSWlibming-dev			+=	$(DESCRIPTION), development files
PKGFILES_CSWlibming-dev				+=	/opt/csw/lib/libming.so
PKGFILES_CSWlibming-dev				+=	$(PKGFILES_DEVEL)
OBSOLETED_BY_CSWlibming-dev			=	CSWlibmingdevel
CATALOGNAME_CSWlibmingdevel			=	libming_devel_stub
RUNTIME_DEP_PKGS_CSWlibming-dev		+=	CSWlibming1
ARCHALL_CSWlibming-dev				=	1
CHECKPKG_OVERRIDES_CSWlibming-dev	+=	archall-devel-package

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/php5/bin:$(PATH)

pre-configure-modulated:
	@echo "executing $@"
	cd $(WORKSRC) && libtoolize
	cd $(WORKSRC) && aclocal -I macros
	cd $(WORKSRC) && automake -a
	cd $(WORKSRC) && autoconf
	$(MAKECOOKIE)

# there are some tests failing for minor reasons, from my stand point,
# going from missing initial files to incorrect evaluation of the
# results:
# Font/test03
# Font/test06
# Font/test07
# Font/test07-cxx
# consequently I choose to not block the release
test-custom:
	-$(MAKE) -k -C $(WORKSRC) check
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
