# $Id$

NAME = tex_pdftricks
VERSION = 1.16
GARTYPE = v2
CATEGORIES = xtra

DESCRIPTION = A pstricks encapsulation for PDF
define BLURB
  PDFtricks -- a LaTeX package that helps to allow PSTricks code in
  a pdfTeX document.
endef

DISTNAME		=	pdftricks
# I don't like this but this is what we get...
MASTER_SITES	=	http://sarovar.org/frs/download.php/98/
VENDOR_URL		=	http://devnag.sarovar.org/
DISTFILES		=	$(DISTNAME).tar.gz
# taken from http://www.latex-project.org/lppl.txt
DISTFILES		+=	README.CSW
DISTFILES		+=	COPYING

WORKSRC				=	$(WORKDIR)/$(DISTNAME)-$(VERSION)
PATCHDIR			=	$(WORKSRC)
PATCHFILES			=	0001-Fix-shebang-bash.patch

BUILD_DEP_PKGS		+=	CSWtetex
RUNTIME_DEP_PKGS	+=	CSWtetex

PACKAGES								=	CSWtex-pdftricks
SPKG_DESC_CSWtex-pdftricks				=	$(DESCRIPTION)
CATALOGNAME_CSWtex-pdftricks			=	tex_pdftricks
OBSOLETED_BY_CSWtex-pdftricks			=	CSWtexpdftricks
CATALOGNAME_CSWtexpdftricks				=	tex_pdftricks_stub
ARCHALL_CSWtex-pdftricks				=	1
CHECKPKG_OVERRIDES_CSWtex-pdftricks		+=	surplus-dependency|CSWtetex

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

include gar/category.mk

install-custom: styles = $(texmflocaldir)/tex/latex/pdftricks
install-custom: documentation = $(texmflocaldir)/doc/generic/pdftricks
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(bindir)
	ginstall --preserve-timestamps --mode=u=rwx,go=rx $(WORKSRC)/pst2pdf $(DESTDIR)/$(bindir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(styles)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/pdftricks.sty $(DESTDIR)/$(styles)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(documentation)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/manual.pdf $(DESTDIR)/$(documentation)
	$(MAKECOOKIE)
