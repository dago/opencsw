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

RUNTIME_DEP_PKGS	+=	CSWlibatk1-0-0
RUNTIME_DEP_PKGS	+=	CSWlibcairo2
RUNTIME_DEP_PKGS	+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS	+=	CSWlibgconf2-4
RUNTIME_DEP_PKGS	+=	CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgio2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgsf1-114
RUNTIME_DEP_PKGS	+=	CSWlibgthread2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibintl8
RUNTIME_DEP_PKGS	+=	CSWlibxml2-2
RUNTIME_DEP_PKGS	+=	CSWpango

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(SGNAME)-(\d+(?:\.\d+)*).tar.gz

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
