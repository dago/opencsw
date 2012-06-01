# $Id$
#
NAME = auctex
VERSION = 11.86
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = A much enhanced TeX/LaTeX mode for Emacs
define BLURB
  AUCTeX is an integrated environment for editing LaTeX, ConTeXt,
  docTeX, Texinfo, and TeX files.
endef

MASTER_SITES	=	http://ftp.gnu.org/pub/gnu/auctex/
DISTFILES		=	$(DISTNAME).tar.gz
DISTFILES		+=	README.CSW
DISTFILES		+=	CSWauctex.postinstall

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-texmf-dir=/opt/csw/share/texmf-local
# this is needed to avoid incorrect interaction with CSWemacssitestart
# installed during the packaging:
CONFIGURE_ARGS	+=	--with-auctexstartfile=/opt/csw/share/emacs/site-lisp/auctex.el
CONFIGURE_ARGS	+=	--with-previewstartfile=/opt/csw/share/emacs/site-lisp/preview-latex.el

BUILD_SCRIPTS	=	nominal
BUILD_SCRIPTS	+=	extradist
BUILD_SCRIPTS	+=	html-docs
BUILD_SCRIPTS	+=	preview-latex.dvi
BUILD_SCRIPTS	+=	preview-latex.ps
BUILD_SCRIPTS	+=	preview-latex.pdf

SKIPTEST		=	1
ARCHALL			=	1

BUILD_DEP_PKGS		=	CSWemacs
BUILD_DEP_PKGS		+=	CSWtetex
BUILD_DEP_PKGS		+=	CSWtexinfo

RUNTIME_DEP_PKGS	=	CSWemacs
RUNTIME_DEP_PKGS	+=	CSWtetex
RUNTIME_DEP_PKGS	+=	CSWgs

include gar/category.mk

build-nominal:
	$(MAKE) -C $(WORKSRC)
	$(MAKECOOKIE)

build-extradist:
	$(MAKE) -C $(WORKSRC)/doc $(subst build-,,$@)
	$(MAKECOOKIE)

build-html-docs:
	$(MAKE) -C $(WORKSRC)/doc $(subst build-,,$@)
	$(MAKECOOKIE)

build-preview-latex.dvi:
	$(MAKE) -C $(WORKSRC)/doc $(subst build-,,$@)
	$(MAKECOOKIE)

build-preview-latex.ps:
	$(MAKE) -C $(WORKSRC)/doc $(subst build-,,$@)
	$(MAKECOOKIE)

build-preview-latex.pdf:
	$(MAKE) -C $(WORKSRC)/doc $(subst build-,,$@)
	$(MAKECOOKIE)

post-install-modulated:
	@echo "executing $@"
	: miscelaneous formats for all the generated documentation
	ginstall $(WORKSRC)/doc/auctex.dvi $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/auctex.ps $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/auctex.pdf $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/preview-latex.dvi $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/preview-latex.ps $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/preview-latex.pdf $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/tex-ref.dvi $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/tex-ref.ps $(DESTDIR)$(docdir)/auctex
	gtar --directory=$(WORKSRC)/doc --create --file=- html | gtar --directory=$(DESTDIR)/$(docdir)/auctex --extract --file=-
	ginstall -d $(DESTDIR)$(docdir)/auctex/examples
	ginstall $(WORKSRC)/preview/circ.tex $(DESTDIR)$(docdir)/auctex/examples
	$(MAKECOOKIE)
