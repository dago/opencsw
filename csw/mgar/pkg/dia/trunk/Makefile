# $Id$
GARNAME = dia
GARVERSION = 0.97
CATEGORIES = apps

DESCRIPTION = A GTK+ based diagram creation program
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

RUNTIME_DEP_PKGS_CSWdia += CSWlibxslt
RUNTIME_DEP_PKGS_CSWdia += CSWlibatk
RUNTIME_DEP_PKGS_CSWdia += CSWggettextrt
RUNTIME_DEP_PKGS_CSWdia += CSWpng
RUNTIME_DEP_PKGS_CSWdia += CSWlibxml2
RUNTIME_DEP_PKGS_CSWdia += CSWfconfig
RUNTIME_DEP_PKGS_CSWdia += CSWglib2
RUNTIME_DEP_PKGS_CSWdia += CSWftype2
RUNTIME_DEP_PKGS_CSWdia += CSWpango
RUNTIME_DEP_PKGS_CSWdia += CSWzlib
RUNTIME_DEP_PKGS_CSWdia += CSWlibart
RUNTIME_DEP_PKGS_CSWdia += CSWgtk2
RUNTIME_DEP_PKGS_CSWdia += CSWlibcairo
RUNTIME_DEP_PKGS_CSWdia += CSWiconv

include gar/category.mk

# For GNU gettext like msgmerge
PATH := /opt/csw/gnu:$(PATH)
