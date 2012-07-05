# $Id$

NAME = tex_metauml_lop
VERSION = 1.0
GARTYPE = v2
CATEGORIES = xtra

DESCRIPTION = MetaUML Library of Patterns
define BLURB
  MetaUML Library of Patterns (UML for LaTeX/MetaPost)
endef

DISTNAME		=	metauml_lop
WORKSRC			=	$(WORKDIR)
PATCHDIR		=	$(WORKSRC)
MASTER_SITES	=	$(SF_MIRRORS)
SF_PROJ			=	metauml
DISTFILES		=	lop-release.tgz
DISTFILES		+=	COPYING
DISTFILES		+=	README.CSW
PATCHFILES		+=	0001-Adapt-build-Solaris.patch

PACKAGES								=	CSWtex-metauml-lop
SPKG_DESC_CSWtex-metauml-lop			=	$(DESCRIPTION)
CATALOG_NAMEtex-metauml-lop				=	tex_metauml_lop
BUILD_DEP_PKGS_CSWtex-metauml-lop		+=	CSWtetex
RUNTIME_DEP_PKGS_CSWtex-metauml-lop		+=	CSWtetex
CHECKPKG_OVERRIDES_CSWtex-metauml-lop	+=	surplus-dependency|CSWtetex
BUILD_DEP_PKGS_CSWtex-metauml-lop		+=	CSWtex-metauml
RUNTIME_DEP_PKGS_CSWtex-metauml-lop		+=	CSWtex-metauml
CHECKPKG_OVERRIDES_CSWtex-metauml-lop	+=	surplus-dependency|CSWtex-metauml
BUILD_DEP_PKGS_CSWtex-metauml-lop		+=	CSWxpdf
BUILD_DEP_PKGS_CSWtex-metauml-lop		+=	CSWnetpbm
ARCHALL_CSWtex-metauml-lop				=	1

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

include gar/category.mk

build-custom:
	cd $(WORKSRC) && ./lop
	$(MAKECOOKIE)

install-custom: pkgdoc = $(texmflocaldir)/doc/metapost/$(NAME)
install-custom: pkgmp = $(texmflocaldir)/metapost/$(NAME)
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdoc)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/lop.pdf $(DESTDIR)/$(pkgdoc)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdoc)/html
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/lop.html $(WORKSRC)/*.jpg $(DESTDIR)/$(pkgdoc)/html
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgmp)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/*.mp $(DESTDIR)/$(pkgmp)
	$(MAKECOOKIE)
