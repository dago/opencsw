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
PATCHFILES		+=	0002-Fix-slib-scriPATCHFILES		+=	0003-Adapt-to-Guile-2.patch
PATCHFILES		+=	0004-Force-libraries-directory.patch

PACKAGES					=	CSWslib
CATALOGNAME_CSWslib			=	slib
SPKG_DESC_CSWslib			=	$(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWslib	+=	CSWguile
CHECKPKG_OVERRIDES_CSWslib	+=	surplus-dependency|CSWguile
RUNTIME_DEP_PKGS_CSWslib	+=	CSWscm
CHECKPKG_OVERRIDES_CSWslib	+=	surplus-dependency|CSWscm
ARCHALL_CSWslib	ng.patch

ARCHALL			=	1

EXTRA_CONFIGURE_ENV	=	PATH=$(prefix)/gnu:$(PATH)
CONFIGURE_ARGS		=	$(DIRPATHS)

TEST_SCRIPTS		=

EXTRA_INSTALL_ENV	=	PATH=$(prefix)/gnu:$(PATH)

include 