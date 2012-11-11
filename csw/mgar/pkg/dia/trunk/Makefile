# $Id$
NAME = dia
VERSION = 0.97
GARTYPE = v2

DESCRIPTION = A GTK+ based diagram creation program
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PATCHFILES = 0001-Make-sure-for-loop-is-not-empty.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://live.gnome.org/Dia

CONFIGURE_ARGS = $(DIRPATHS)

# Tests for i386 fail in /Dia/Objects/Istar - goal/Copy with
#   g_str_hash (100) + 16
TEST_TARGET ?= check

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
