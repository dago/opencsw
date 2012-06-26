# $Id$

NAME = tex_dirtree
VERSION = 0.2
GARTYPE = v2
CATEGORIES = xtra

DESCRIPTION = Draws Windows Explorer style trees for Plain TeX and LaTeX
define BLURB
  The dirtree package provide a TeX macro to typeset directory trees like
  in windows explorator.
endef

DISTNAME		=	dirtree
MASTER_SITES	=	http://mirror.ctan.org/macros/generic/
DISTFILES		=	$(DISTNAME).zip

RUNTIME_DEP_PKGS	+=	CSWtetex

PACKAGES					=	CSWtex-dirtree
SPKG_DESC_CSWtex-dirtree	=	$(DESCRIPTION)
CATALOGNAME_CSWtex-dirtree	=	tex_dirtree
OBSOLETED_BY_CSWtex-dirtree	=	CSWtexdirtree
CATALOGNAME_CSWtexdirtree	=	tex_dirtree_stub
ARCHALL_CSWtex-dirtree		=	1

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

include gar/category.mk

texdir	=	$(texmflocaldir)/tex/latex/dirtree
texmf	=	\
			$(WORKSRC)/dirtree.sty \
			$(WORKSRC)/dirtree.tex

build-custom:	\
				$(texmf) \
				doc
	$(MAKECOOKIE)

$(texmf):	\
			$(WORKSRC)/dirtree.ins \
			$(WORKSRC)/dirtree.dtx
	cd $(WORKSRC) && latex dirtree.ins

doc:	\
		$(WORKSRC)/dirtree.dvi \
		$(WORKSRC)/dirtree.ps \
		$(WORKSRC)/dirtree.pdf
	: $@ done

$(WORKSRC)/dirtree.dvi:	\
						$(texmf)
	cd $(WORKSRC) && latex dirtree.dtx
	cd $(WORKSRC) && makeindex -s gind.ist dirtree
	cd $(WORKSRC) && makeindex -s gglo.ist -o dirtree.gls dirtree.glo
	cd $(WORKSRC) && latex dirtree.dtx

$(WORKSRC)/dirtree.ps:	\
						$(WORKSRC)/dirtree.dvi
	cd $(WORKSRC) && dvips dirtree

$(WORKSRC)/dirtree.pdf:	\
						$(WORKSRC)/dirtree.ps
	cd $(WORKSRC) && ps2pdf dirtree.ps dirtree.pdf

install-custom: pkgdocdir = $(docdir)/$(NAME)
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(texdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/dirtree.sty $(DESTDIR)/$(texdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/dirtree.tex $(DESTDIR)/$(texdir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/dirtree.dvi $(DESTDIR)/$(pkgdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/dirtree.ps $(DESTDIR)/$(pkgdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/dirtree.pdf $(DESTDIR)/$(pkgdocdir)
	$(MAKECOOKIE)
