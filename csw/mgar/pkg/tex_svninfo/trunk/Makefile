# $Id$

NAME = tex_svninfo
VERSION = 0.7.4
GARTYPE = v2
CATEGORIES = xtra

DESCRIPTION = Extract the information provided by the SVN revision control system from TeX documents
define BLURB
  This package is used to extract the revision and file information provided
  by the subversion revision control system.
endef

DISTNAME		=	svninfo
MASTER_SITES	=	http://mirror.ctan.org/macros/latex/contrib/
DISTFILES		=	$(DISTNAME).zip
# taken from http://www.latex-project.org/lppl.txt
DISTFILES		+=	README.CSW
DISTFILES		+=	COPYING
PATCHFILES		+=	0001-Adapt-build.patch

BUILD_DEP_PKGS		+=	CSWtetex

RUNTIME_DEP_PKGS	+=	CSWtetex

PACKAGES					=	CSWtex-svninfo
SPKG_DESC_CSWtex-svninfo	=	$(DESCRIPTION)
CATALOGNAME_CSWtex-svninfo	=	tex_svninfo
OBSOLETED_BY_CSWtex-svninfo	=	CSWtexsvninfo
CATALOGNAME_CSWtexsvninfo	=	tex_svninfo_stub
ARCHALL_CSWtex-svninfo		=	1
CHECKPKG_OVERRIDES_CSWtex-svninfo += surplus-dependency|CSWtetex

CONFIGURE_SCRIPTS	=
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

include gar/category.mk

install-custom: pkgdocdir = $(docdir)/$(NAME)
install-custom: GNUinstall = ginstall
install-custom: TEXDIR = $(texmflocaldir)
install-custom: CONTRIB = $(TEXDIR)/tex/latex/$(BASE)
install-custom: DOCDIR  = $(TEXDIR)/doc/latex/styles
install-custom:
	$(GNUinstall) --directory $(DESTDIR)/$(CONTRIB)
	$(GNUinstall) $(WORKSRC)/svninfo.cfg $(WORKSRC)/svninfo.sty $(DESTDIR)/$(CONTRIB)
	$(GNUinstall) --directory $(DESTDIR)/$(DOCDIR)
	$(GNUinstall) $(WORKSRC)/svninfo.dvi $(WORKSRC)/svninfo.ps $(WORKSRC)/svninfo.pdf $(DESTDIR)/$(DOCDIR)
	$(MAKECOOKIE)
