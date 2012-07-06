# $Id$

NAME = tex_metauml_man
VERSION = 0.2.5
GARTYPE = v2
CATEGORIES = xtra

DESCRIPTION = Manual for the MetaPost library for typesetting UML diagrams using a human-friendly textual notation
define BLURB
  The manual for MetaUML, the GNU GPL MetaPost library for typesetting UML
  diagrams, using a human-friendly textual notation.
endef

DISTNAME		=	metauml_manual
WORKSRC			=	$(WORKDIR)/$(DISTNAME)2
PATCHDIR		=	$(WORKSRC)
MASTER_SITES	=	$(SF_MIRRORS)
SF_PROJ			=	metauml
DISTFILES		=	$(DISTNAME)_src_$(VERSION).tgz
DISTFILES		+=	fdl-1.3.txt

CONFIGURE_SCRIPTS	=
TEST_SCRIPTS		=
BUILD_SCRIPTS		=	custom
INSTALL_SCRIPTS		=	custom

PACKAGES								=	CSWtex-metauml-man
SPKG_DESC_CSWtex-metauml-man			=	$(DESCRIPTION)
CATALOG_NAMEtex-metauml-man				=	tex_metauml_man
OBSOLETED_BY_CSWtex-metauml-man			=	CSWtexmetaumlman
CATALOGNAME_CSWtexmetaumlman			=	tex_metaumlman_stub
CHECKPKG_OVERRIDES_CSWtexmetaumlman		+=	action-class-only-in-pkginfo|none
CHECKPKG_OVERRIDES_CSWtexmetaumlman		+=	license-missing|/opt/csw/share/doc/tex_metaumlman_stub/license
BUILD_DEP_PKGS_CSWtex-metauml-man		+=	CSWtetex
RUNTIME_DEP_PKGS_CSWtex-metauml-man		+=	CSWtetex
CHECKPKG_OVERRIDES_CSWtex-metauml-man	+=	surplus-dependency|CSWtetex
BUILD_DEP_PKGS_CSWtex-metauml-man		+=	CSWtex-metauml
RUNTIME_DEP_PKGS_CSWtex-metauml-man		+=	CSWtex-metauml
CHECKPKG_OVERRIDES_CSWtex-metauml-man	+=	surplus-dependency|CSWtex-metauml
ARCHALL_CSWtex-metauml-man				=	1
LICENSE_CSWtex-metauml-man				=	fdl-1.3.txt

include gar/category.mk

build-custom: $(WORKSRC)/metauml_manual.pdf

$(WORKSRC)/fig/activity.1: $(WORKSRC)/fig/activity.mp
	cd $(WORKSRC)/fig && mpost activity.mp

$(WORKSRC)/fig/activity_diagrams.1: $(WORKSRC)/fig/activity_diagrams.mp
	cd $(WORKSRC)/fig && mpost activity_diagrams.mp

$(WORKSRC)/fig/appetizer.1: $(WORKSRC)/fig/appetizer.mp
	cd $(WORKSRC)/fig && mpost appetizer.mp

$(WORKSRC)/fig/boxes_vs_util.1: $(WORKSRC)/fig/boxes_vs_util.mp
	cd $(WORKSRC)/fig && mpost boxes_vs_util.mp

$(WORKSRC)/fig/class.1: $(WORKSRC)/fig/class.mp
	cd $(WORKSRC)/fig && mpost class.mp

$(WORKSRC)/fig/class_association.1: $(WORKSRC)/fig/class_association.mp
	cd $(WORKSRC)/fig && mpost class_association.mp

$(WORKSRC)/fig/class_customization.1: $(WORKSRC)/fig/class_customization.mp
	cd $(WORKSRC)/fig && mpost class_customization.mp

$(WORKSRC)/fig/class_customization2.1: $(WORKSRC)/fig/class_customization2.mp
	cd $(WORKSRC)/fig && mpost class_customization2.mp

$(WORKSRC)/fig/class_diagrams.1: $(WORKSRC)/fig/class_diagrams.mp
	cd $(WORKSRC)/fig && mpost class_diagrams.mp

$(WORKSRC)/fig/class_templates.1: $(WORKSRC)/fig/class_templates.mp
	cd $(WORKSRC)/fig && mpost class_templates.mp

$(WORKSRC)/fig/cliparts.1: $(WORKSRC)/fig/cliparts.mp
	cd $(WORKSRC)/fig && mpost cliparts.mp

$(WORKSRC)/fig/component.1: $(WORKSRC)/fig/component.mp
	cd $(WORKSRC)/fig && mpost component.mp

$(WORKSRC)/fig/group.1: $(WORKSRC)/fig/group.mp
	cd $(WORKSRC)/fig && mpost group.mp

$(WORKSRC)/fig/how-links-work.1: $(WORKSRC)/fig/how-links-work.mp
	cd $(WORKSRC)/fig && mpost how-links-work.mp

$(WORKSRC)/fig/instance.1: $(WORKSRC)/fig/instance.mp
	cd $(WORKSRC)/fig && mpost instance.mp

$(WORKSRC)/fig/note.1: $(WORKSRC)/fig/note.mp
	cd $(WORKSRC)/fig && mpost note.mp

$(WORKSRC)/fig/object_stack.1: $(WORKSRC)/fig/object_stack.mp
	cd $(WORKSRC)/fig && mpost object_stack.mp

$(WORKSRC)/fig/package.1: $(WORKSRC)/fig/package.mp
	cd $(WORKSRC)/fig && mpost package.mp

$(WORKSRC)/fig/paths.1: $(WORKSRC)/fig/paths.mp
	cd $(WORKSRC)/fig && mpost paths.mp

$(WORKSRC)/fig/paths_man.1: $(WORKSRC)/fig/paths_man.mp
	cd $(WORKSRC)/fig && mpost paths_man.mp

$(WORKSRC)/fig/picture_info.1: $(WORKSRC)/fig/picture_info.mp
	cd $(WORKSRC)/fig && mpost picture_info.mp

$(WORKSRC)/fig/picture_stack.1: $(WORKSRC)/fig/picture_stack.mp
	cd $(WORKSRC)/fig && mpost picture_stack.mp

$(WORKSRC)/fig/positioning.1: $(WORKSRC)/fig/positioning.mp
	cd $(WORKSRC)/fig && mpost positioning.mp

$(WORKSRC)/fig/properties.1: $(WORKSRC)/fig/properties.mp
	cd $(WORKSRC)/fig && mpost properties.mp

$(WORKSRC)/fig/state.1: $(WORKSRC)/fig/state.mp
	cd $(WORKSRC)/fig && mpost state.mp

$(WORKSRC)/fig/statemachine_diagrams.1: $(WORKSRC)/fig/statemachine_diagrams.mp
	cd $(WORKSRC)/fig && mpost statemachine_diagrams.mp

$(WORKSRC)/fig/test_activity.1: $(WORKSRC)/fig/test_activity.mp
	cd $(WORKSRC)/fig && mpost test_activity.mp

$(WORKSRC)/fig/test_class.1: $(WORKSRC)/fig/test_class.mp
	cd $(WORKSRC)/fig && mpost test_class.mp

$(WORKSRC)/fig/test_class_qual_assoc.1: $(WORKSRC)/fig/test_class_qual_assoc.mp
	cd $(WORKSRC)/fig && mpost test_class_qual_assoc.mp

$(WORKSRC)/fig/test_class_templates.1: $(WORKSRC)/fig/test_class_templates.mp
	cd $(WORKSRC)/fig && mpost test_class_templates.mp

$(WORKSRC)/fig/test_component.1: $(WORKSRC)/fig/test_component.mp
	cd $(WORKSRC)/fig && mpost test_component.mp

$(WORKSRC)/fig/test_font.1: $(WORKSRC)/fig/test_font.mp
	cd $(WORKSRC)/fig && mpost test_font.mp

$(WORKSRC)/fig/test_group.1: $(WORKSRC)/fig/test_group.mp
	cd $(WORKSRC)/fig && mpost test_group.mp

$(WORKSRC)/fig/test_instance.1: $(WORKSRC)/fig/test_instance.mp
	cd $(WORKSRC)/fig && mpost test_instance.mp

$(WORKSRC)/fig/test_lars_issues.1: $(WORKSRC)/fig/test_lars_issues.mp
	cd $(WORKSRC)/fig && mpost test_lars_issues.mp

$(WORKSRC)/fig/test_lowlevel.1: $(WORKSRC)/fig/test_lowlevel.mp
	cd $(WORKSRC)/fig && mpost test_lowlevel.mp

$(WORKSRC)/fig/test_note.1: $(WORKSRC)/fig/test_note.mp
	cd $(WORKSRC)/fig && mpost test_note.mp

$(WORKSRC)/fig/test_package.1: $(WORKSRC)/fig/test_package.mp
	cd $(WORKSRC)/fig && mpost test_package.mp

$(WORKSRC)/fig/test_paths.1: $(WORKSRC)/fig/test_paths.mp
	cd $(WORKSRC)/fig && mpost test_paths.mp

$(WORKSRC)/fig/test_picture.1: $(WORKSRC)/fig/test_picture.mp
	cd $(WORKSRC)/fig && mpost test_picture.mp

$(WORKSRC)/fig/test_picture_stack.1: $(WORKSRC)/fig/test_picture_stack.mp
	cd $(WORKSRC)/fig && mpost test_picture_stack.mp

$(WORKSRC)/fig/test_picture_tex_rendering.1: $(WORKSRC)/fig/test_picture_tex_rendering.mp
	cd $(WORKSRC)/fig && mpost test_picture_tex_rendering.mp

$(WORKSRC)/fig/test_positioning.1: $(WORKSRC)/fig/test_positioning.mp
	cd $(WORKSRC)/fig && mpost test_positioning.mp

$(WORKSRC)/fig/test_skins.1: $(WORKSRC)/fig/test_skins.mp
	cd $(WORKSRC)/fig && mpost test_skins.mp

$(WORKSRC)/fig/test_skins_global_defaults.1: $(WORKSRC)/fig/test_skins_global_defaults.mp
	cd $(WORKSRC)/fig && mpost test_skins_global_defaults.mp

$(WORKSRC)/fig/test_state.1: $(WORKSRC)/fig/test_state.mp
	cd $(WORKSRC)/fig && mpost test_state.mp

$(WORKSRC)/fig/test_usecase.1: $(WORKSRC)/fig/test_usecase.mp
	cd $(WORKSRC)/fig && mpost test_usecase.mp

$(WORKSRC)/fig/usecase.1: $(WORKSRC)/fig/usecase.mp
	cd $(WORKSRC)/fig && mpost usecase.mp

$(WORKSRC)/fig/usecase_diagrams.1: $(WORKSRC)/fig/usecase_diagrams.mp
	cd $(WORKSRC)/fig && mpost usecase_diagrams.mp

$(WORKSRC)/metauml_manual.pdf:	\
								$(WORKSRC)/metauml_manual.tex \
								$(WORKSRC)/gnu-fdl.tex \
								$(WORKSRC)/macro.tex \
								$(WORKSRC)/test_suite.tex \
								$(WORKSRC)/fig/activity.1 \
								$(WORKSRC)/fig/activity_diagrams.1 \
								$(WORKSRC)/fig/appetizer.1 \
								$(WORKSRC)/fig/boxes_vs_util.1 \
								$(WORKSRC)/fig/class.1 \
								$(WORKSRC)/fig/class_association.1 \
								$(WORKSRC)/fig/class_customization.1 \
								$(WORKSRC)/fig/class_customization2.1 \
								$(WORKSRC)/fig/class_diagrams.1 \
								$(WORKSRC)/fig/class_templates.1 \
								$(WORKSRC)/fig/cliparts.1 \
								$(WORKSRC)/fig/component.1 \
								$(WORKSRC)/fig/group.1 \
								$(WORKSRC)/fig/how-links-work.1 \
								$(WORKSRC)/fig/instance.1 \
								$(WORKSRC)/fig/note.1 \
								$(WORKSRC)/fig/object_stack.1 \
								$(WORKSRC)/fig/package.1 \
								$(WORKSRC)/fig/paths.1 \
								$(WORKSRC)/fig/paths_man.1 \
								$(WORKSRC)/fig/picture_info.1 \
								$(WORKSRC)/fig/picture_stack.1 \
								$(WORKSRC)/fig/positioning.1 \
								$(WORKSRC)/fig/properties.1 \
								$(WORKSRC)/fig/state.1 \
								$(WORKSRC)/fig/statemachine_diagrams.1 \
								$(WORKSRC)/fig/test_activity.1 \
								$(WORKSRC)/fig/test_class.1 \
								$(WORKSRC)/fig/test_class_qual_assoc.1 \
								$(WORKSRC)/fig/test_class_templates.1 \
								$(WORKSRC)/fig/test_component.1 \
								$(WORKSRC)/fig/test_font.1 \
								$(WORKSRC)/fig/test_group.1 \
								$(WORKSRC)/fig/test_instance.1 \
								$(WORKSRC)/fig/test_lars_issues.1 \
								$(WORKSRC)/fig/test_lowlevel.1 \
								$(WORKSRC)/fig/test_note.1 \
								$(WORKSRC)/fig/test_package.1 \
								$(WORKSRC)/fig/test_paths.1 \
								$(WORKSRC)/fig/test_picture.1 \
								$(WORKSRC)/fig/test_picture_stack.1 \
								$(WORKSRC)/fig/test_picture_tex_rendering.1 \
								$(WORKSRC)/fig/test_positioning.1 \
								$(WORKSRC)/fig/test_skins.1 \
								$(WORKSRC)/fig/test_skins_global_defaults.1 \
								$(WORKSRC)/fig/test_state.1 \
								$(WORKSRC)/fig/test_usecase.1 \
								$(WORKSRC)/fig/usecase.1 \
								$(WORKSRC)/fig/usecase_diagrams.1
	cd $(WORKSRC) && pdflatex '\nonstopmode\input{metauml_manual.tex}'
	cd $(WORKSRC) && pdflatex '\nonstopmode\input{metauml_manual.tex}'
	$(MAKECOOKIE)

install-custom: pkgdoc = $(texmflocaldir)/doc/metapost/$(NAME)
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdoc)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/metauml_manual.pdf $(DESTDIR)/$(pkgdoc)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdoc)/examples
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/fig/*.mp $(DESTDIR)/$(pkgdoc)/examples
	$(MAKECOOKIE)
