# $Id$

NAME		=	libgoffice
SGVERSION	=	0.8
SGREL		=	17
VERSION		=	$(SGVERSION).$(SGREL)
CATEGORIES	=	gnome
GARTYPE		=	v2

DESCRIPTION = Document centric objects library
define BLURB
	GOffice is a library of document centric objects and utilities building on
	top of GLib and Gtk+.
endef

SGNAME			=	goffice
MASTER_SITES	=	$(GNOME_ROOT)/$(SGNAME)/$(GNOME_SUBV)/
DISTFILES		=	$(SGNAME)-$(VERSION).tar.bz2
DISTNAME		=	$(SGNAME)-$(VERSION)

GARCOMPILER		=	GNU

BUILD_DEP_PKGS		+=	CSWintltool
BUILD_DEP_PKGS		+=	CSWlibatk-dev
BUILD_DEP_PKGS		+=	CSWlibcairo-dev
BUILD_DEP_PKGS		+=	CSWlibfreetype-dev
BUILD_DEP_PKGS		+=	CSWlibgconf-dev
BUILD_DEP_PKGS		+=	CSWlibgdk-pixbuf-dev
BUILD_DEP_PKGS		+=	CSWlibglib2-dev
BUILD_DEP_PKGS		+=	CSWlibgsf-dev
BUILD_DEP_PKGS		+=	CSWlibgsf-dev
BUILD_DEP_PKGS		+=	CSWlibgtk2-dev
BUILD_DEP_PKGS		+=	CSWlibxml2-dev
BUILD_DEP_PKGS		+=	CSWpangodevel

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

PACKAGES							+=	CSWlibgoffice-doc
CATALOGNAME_CSWlibgoffice-doc		=	libgoffice_doc
SPKG_DESC_CSWlibgoffice-doc			+=	$(DESCRIPTION), documentation
ARCHALL_CSWlibgoffice-doc			=	1
REINPLACE_USRSHARE					+=	/opt/csw/share/gtk-doc/html/goffice-0.8/*.html
REINPLACE_WHEN_USRSHARE				=	postinstall

PACKAGES	+=	CSWlibgoffice0-8-8
CATALOGNAME_CSWlibgoffice0-8-8		=	libgoffice0_8_8
SPKG_DESC_CSWlibgoffice0-8-8		+=	$(DESCRIPTION), libgoffice-0.8.so.8
PKGFILES_CSWlibgoffice0-8-8			+=	$(call baseisadirs,$(libdir),libgoffice-0\.8\.so\.8\.0\.17)
PKGFILES_CSWlibgoffice0-8-8			+=	$(call baseisadirs,$(libdir),libgoffice-0\.8\.so\.8(\.\d+)*)
PKGFILES_CSWlibgoffice0-8-8			+=	/opt/csw/lib/goffice/.*
PKGFILES_CSWlibgoffice0-8-8			+=	/opt/csw/share/goffice/.*
PKGFILES_CSWlibgoffice0-8-8			+=	/opt/csw/share/locale/.*
PKGFILES_CSWlibgoffice0-8-8			+=	/opt/csw/share/pixmaps/goffice/.*
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibgsf1-114
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgoffice0-8-8	+=	CSWpango

PACKAGES							+=	CSWlibgoffice-dev
CATALOGNAME_CSWlibgoffice-dev		=	libgoffice_dev
SPKG_DESC_CSWlibgoffice-dev			+=	$(DESCRIPTION), development files
PKGFILES_CSWlibgoffice-dev			+=	/opt/csw/lib/libgoffice-0.8.so
PKGFILES_CSWlibgoffice-dev			+=	$(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgoffice-dev	+=	CSWlibgoffice0-8-8
ARCHALL_CSWlibgoffice-dev			=	1
CHECKPKG_OVERRIDES_CSWlibgoffice-dev+=	archall-devel-package

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

post-install-modulated:
	ginstall --directory $(DESTDIR)/$(docdir)/$(NAME)
	cd $(DESTDIR)/$(docdir)/$(NAME) && ln -s ../../gtk-doc/html/$(SGNAME)-$(SGVERSION) html
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
