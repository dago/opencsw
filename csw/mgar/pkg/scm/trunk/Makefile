# $Id$

NAME = scm
VERSION = 5e7
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = The Algorithmic Language Scheme
define BLURB
  SCM conforms to Revised^5 Report on the Algorithmic Language Scheme
  and the IEEE P1178 specification.  SCM is written in C and runs under
  Amiga, Atari-ST, MacOS, MS-DOS, OS/2, NOS/VE, Unicos, VMS, Windows,
  Unix, and similar systems.
endef

WORKSRC			=	$(WORKDIR)/$(NAME)
PATCHDIR		=	$(WORKSRC)
MASTER_SITES	=	http://groups.csail.mit.edu/mac/ftpdir/scm/
DISTFILES		=	$(DISTNAME).zip
PATCHFILES		=	0001-Fix-configure-shebang.patch

GARCOMPILER			=	GNU
EXTRA_CONFIGURE_ENV	=	PATH=$(prefix)/gnu:$(PATH)
CONFIGURE_ARGS		=	$(DIRPATHS)

BUILD_SCRIPTS	=	custom

include gar/category.mk

build-custom:
	cd $(WORKSRC) && $(MAKE) scmlit
	$(MAKECOOKIE)
