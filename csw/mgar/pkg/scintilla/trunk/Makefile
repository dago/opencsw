# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = scintilla
VERSION = 2.26
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A source code editing component
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)226.tgz
DISTNAME = scintilla

LICENSE = License.txt

PACKAGES += CSWlibscintilla2
SPKG_DESC_CSWlibscintilla2 = Library source code editing component, libscintilla.so.2
PKGFILES_CSWlibscintilla2 = $(call pkgfiles_lib,libscintilla.so.2)
RUNTIME_DEP_PKGS_CSWlibscintilla2 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibscintilla2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibscintilla2 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibscintilla2 += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibscintilla2 += CSWlibatk
RUNTIME_DEP_PKGS_CSWlibscintilla2 += CSWpango
RUNTIME_DEP_PKGS_CSWlibscintilla2 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibscintilla2 += CSWglib2

PACKAGES += CSWlibscintilla-dev
SPKG_DESC_CSWlibscintilla-dev = Development files for libscintilla.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibscintilla-dev += CSWlibscintilla2
RUNTIME_DEP_PKGS_CSWlibscintilla-dev += CSWpython

WORKSRC = $(WORKDIR)/$(DISTNAME)/gtk

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

# pic13 is too small
EXTRA_CXXFLAGS = -xcode=pic32

EXTRA_LINKER_FLAGS = -norunpath

# Ugh, manual makefile.
CONFIGURE_SCRIPTS =

BUILD_OVERRIDE_VARS = CCOMP CC CONFIGFLAGS CXXFLAGS
BUILD_OVERRIDE_VAR_CCOMP = $(CC)
BUILD_OVERRIDE_VAR_CC = $(CXX)
BUILD_OVERRIDE_VAR_CONFIGFLAGS = $(shell PKG_CONFIG_PATH=$(PKG_CONFIG_PATH) $(bindir_install)/pkg-config --cflags gtk+-2.0)
BUILD_OVERRIDE_VAR_CXXFLAGS = -DGTK -DSCI_LEXER -I ../include -I ../src -I ../lexlib $(CXXFLAGS)

TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom: LINKFLAGS_GTK=$(shell PKG_CONFIG_PATH=$(PKG_CONFIG_PATH) $(bindir_install)/pkg-config --libs gtk+-2.0)
install-custom:
	mkdir -p $(DESTDIR)$(includedir)
	cp $(WORKDIR)/$(DISTNAME)/include/* $(DESTDIR)$(includedir)
	mkdir -p $(DESTDIR)$(libdir)
	cd $(WORKDIR)/$(DISTNAME)/bin && $(CXX) $(LDFLAGS) -R $(libdir) -lCstd $(LINKFLAGS_GTK) -G -z allextract -h libscintilla.so.2 scintilla.a  -o $(DESTDIR)$(libdir)/libscintilla.so.2.26
	ln -s libscintilla.so.2.26 $(DESTDIR)$(libdir)/libscintilla.so.2
	ln -s libscintilla.so.2.26 $(DESTDIR)$(libdir)/libscintilla.so
	@$(MAKECOOKIE)

