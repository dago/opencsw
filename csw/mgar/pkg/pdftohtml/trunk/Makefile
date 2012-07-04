# $Id$

NAME = pdftohtml
VERSION = 0.40a
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Converts files from PDF into HTML
define BLURB
  Pdftohtml is a tool based on the Xpdf package which translates pdf
  documents into html format.
endef

MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES		=	$(DISTNAME).tar.gz
DISTFILES		+=	COPYING
PATCHFILES		+=	0001-Silent-write-strings-warnings.patch
PATCHFILES		+=	0002-Fix-paths.patch

BUILD_DEP_PKGS		+=	CSWhelp2man

RUNTIME_DEP_PKGS	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS	+=	CSWlibstdc++6
RUNTIME_DEP_PKGS	+=	CSWxpdf
RUNTIME_DEP_PKGS	+=	CSWgsfonts

CHECKPKG_OVERRIDES_CSWpdftohtml	+=	surplus-dependency|CSWxpdf
CHECKPKG_OVERRIDES_CSWpdftohtml	+=	surplus-dependency|CSWgsfonts
CHECKPKG_OVERRIDES_CSWpdftohtml	+=	file-with-bad-content|/usr/share|root/opt/csw/bin/pdftohtml

GARCOMPILER			=	GNU
CONFIGURE_SCRIPTS	=
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

include gar/category.mk

post-build-modulated:
	cd $(WORKSRC)/src && help2man --no-discard-stderr --help-option=-h --version-option=-v --no-info --output=pdftohtml.1 ./pdftohtml
	$(MAKECOOKIE)

install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(bindir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/src/pdftohtml $(DESTDIR)/$(bindir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(mandir)/man1
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/src/pdftohtml.1 $(DESTDIR)/$(mandir)/man1
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
