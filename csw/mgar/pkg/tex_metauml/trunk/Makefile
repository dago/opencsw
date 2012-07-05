# $Id$

NAME = tex_metauml
VERSION = 0.2.5
GARTYPE = v2
CATEGORIES = xtra

DESCRIPTION = MetaPost library for typesetting UML diagrams using a human-friendly textual notation
define BLURB
  MetaUML is a GNU GPL MetaPost library for typesetting UML diagrams, using a human-friendly textual notation.
endef

DISTNAME		=	metauml_lib
MASTER_SITES	=	$(SF_MIRRORS)
SF_PROJ			=	metauml
DISTFILES		=	$(DISTNAME)_$(VERSION).tgz
DISTFILES		+=	README.CSW

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

PACKAGES							=	CSWtex-metauml
SPKG_DESC_CSWtex-metauml			=	$(DESCRIPTION)
CATALOG_NAMEtex-metauml				=	tex_metauml
OBSOLETED_BY_CSWtex-metauml			=	CSWtexmetauml
CATALOGNAME_CSWtexmetauml			=	tex_metauml_stub
RUNTIME_DEP_PKGS					=	CSWtetex
CHECKPKG_OVERRIDES_CSWtex-metauml	+=	surplus-dependency|CSWtetex
ARCHALL_CSWtex-metauml				=	1
LICENSE								=	thrunk/License

include gar/category.mk

install-custom: pkgtexmf = $(texmflocaldir)/metapost/metauml
install-custom: pkgdoc = $(docdir)/$(NAME)
install-custom: source = $(WORKSRC)/thrunk
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/*.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdoc)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/version.txt $(DESTDIR)/$(pkgdoc)
	$(MAKECOOKIE)
