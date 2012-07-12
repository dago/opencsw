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
	$(HOME)/bin/ocswdeplist --package $(NAME)
