# $Id$

NAME = slib
VERSION = 3b3
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A portable Scheme library
define BLURB
  SLIB is a portable Scheme library which SCM uses
endef

MASTER_SITES	=	http://groups.csail.mit.edu/mac/ftpdir/scm/
DISTFILES		=	$(DISTNAME).tar.gz
PATCHFILES		=	0001-Fix-configure-shebang.patch
PATCHFILES		+=	0002-Fix-slib-script-shebang.patch

ARCHALL			=	1

EXTRA_CONFIGURE_ENV	=	PATH=$(prefix)/gnu:$(PATH)
CONFIGURE_ARGS		=	$(DIRPATHS)

TEST_SCRIPTS		=

EXTRA_INSTALL_ENV	=	PATH=$(prefix)/gnu:$(PATH)

include gar/category.mk

