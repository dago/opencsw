# $Id$

NAME = tex_devnag
VERSION = 2.15.1
GARTYPE = v2
CATEGORIES = xtra

DESCRIPTION = Support for typesetting texts in Devanagari script TeX and LaTeX
define BLURB
  The Devanāgarī for TEX (devnag) package provides a way to typeset
  high-quality Devanāgarī text with TEX. The devnag package provides
  features that support Sanskrit, Hindi, Marathi, Nepali, and other
  languages typically printed in the Devanāgarī script. The devnag
  package was released in May 1991 by Frans Velthuis for the University
  of Groningen, The Netherlands. The devnag package consists of a
  preprocessor, font files, and macros for Plain TEX and LATEX.
endef

DISTNAME		=	velthuis
# I don't like this but this is what we get...
MASTER_SITES	=	http://sarovar.org/frs/download.php/1334/
VENDOR_URL		=	http://devnag.sarovar.org/
DISTFILES		=	$(DISTNAME).zip
# taken from http://www.latex-project.org/lppl.txt
DISTFILES		+=	README.CSW
DISTFILES		+=	COPYING

PACKAGES								=	CSWtex-devnag-common
SPKG_DESC_CSWtex-devnag-common			=	$(DESCRIPTION), fonts, documentation and macros
CATALOGNAME_CSWtex-devnag-common		=	tex_devnag_common
OBSOLETED_BY_CSWtex-devnag-common		=	CSWtexvdevnagcommon
CATALOGNAME_CSWtexvdevnagcommon			=	tex_vdevnag_common_stub
ARCHALL_CSWtex-devnag-common			=	1
RUNTIME_DEP_PKGS_CSWtex-devnag-common	+=	CSWtetex

CHECKPKG_OVERRIDES_CSWtex-devnag_common	+=	surplus-dependency|CSWtetex

PACKAGES							+=	CSWtex-devnag
SPKG_DESC_CSWtex-devnag				=	$(DESCRIPTION)
CATALOGNAME_CSWtex-devnag			=	tex_devnag
OBSOLETED_BY_CSWtex-devnag			=	CSWtexvdevnag
CATALOGNAME_CSWtexvdevnag			=	tex_vdevnag_stub
PKGFILES_CSWtex-devnag				=	/opt/csw/bin/devnag
RUNTIME_DEP_PKGS_CSWtex-devnag		=	CSWtex-devnag-common
CHECKPKG_OVERRIDES_CSWtex-devnag	+=	surplus-dependency|CSWtex_devnag_common

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

GARCOMPILER			=	GNU

include gar/category.mk

binsrc	=	$(WORKSRC)/bin

build-custom:	\
				$(binsrc)/devnag
	$(MAKECOOKIE)

$(binsrc)/devnag:	\
					$(binsrc)/devnag.o

$(binsrc)/devnag.o:	\
					$(binsrc)/devnag.c

install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(bindir)
	ginstall --preserve-timestamps --mode=u=rwx,go=rx $(binsrc)/devnag $(DESTDIR)/$(bindir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(texmflocaldir)
	gtar --directory=$(WORKSRC) --create --file=- doc fonts tex | gtar --directory=$(DESTDIR)/$(texmflocaldir) --extract --file=-
	$(MAKECOOKIE)
