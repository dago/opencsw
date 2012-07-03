# $Id$

NAME = tex_metauml
VERSION = 0.2.5
GARTYPE = v2
CATEGORIES = xtra

DESCRIPTION = MetaPost library for typesetting UML diagrams using a human-friendly textual notation
define BLURB
  MetaUML is a GNU GPL MetaPost library for typesetting UML diagrams, using a human-friendly textual notation.
endef

DISTNAME		=	metauml_lib_$(VERSION)
WORKSRC			=	$(WORKDIR)/metauml_lib
PATCHDIR		=	$(WORKSRC)
MASTER_SITES	=	$(SF_MIRRORS)
SF_PROJ			=	metauml
DISTFILES		=	$(DISTNAME).tgz

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
LICENCE_CSWtex-metauml				=	License

include gar/category.mk

install-custom: pkgtexmf = $(texmflocaldir)/metapost/metauml
install-custom: pkgdoc = $(docdir)/$(NAME)
install-custom: source = $(WORKSRC)/thrunk
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_activity.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_base.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_behavioral_common.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_class.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_class_assoc.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_class_clipart.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_class_relations.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_defaults.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_instance.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_links.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_note.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_package.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_package_relations.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_paths.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_skin_simple.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_state.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_stereotype.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_templates.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_usecase.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/metauml_usecase_clipart.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/util_commons.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/util_group.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/util_infrastructure.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/util_log.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/util_margins.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/util_object.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/util_picture.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/util_picture_stack.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/util_positioning.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/util_shade.mp $(DESTDIR)/$(pkgtexmf)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdoc)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/version.txt $(DESTDIR)/$(pkgdoc)
	$(MAKECOOKIE)
