# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gtkspell
VERSION = 2.0.16
GARTYPE = v2
GARCOMPILER = SOS12U3

DESCRIPTION = Spell checking for GtkTextView
define BLURB
  GtkSpell provides word-processor-style highlighting and replacement of misspelled words in a GtkTextView widget.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES  = CSWlibgtkspell0
OBSOLETED_BY_CSWlibgtkspell0 += CSWgtkspell
CATALOGNAME_CSWgtkspell = gtkspell_stub
SPKG_DESC_CSWlibgtkspell0 = $(DESCRIPTION), libgtkspell.so.0
PKGFILES_CSWlibgtkspell0 = $(call pkgfiles_lib,libgtkspell.so.0)
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibenchant1
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibgtk-x11-2-0-0
# Dependencies due to `ld -z ignore` issue on sparc, remove once resolved
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibpangoft2-1-0-0
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgtkspell0 += CSWlibpangocairo1-0-0
CHECKPKG_OVERRIDES_CSWlibgtkspell0 += surplus-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWlibgtkspell0 += surplus-dependency|CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWlibgtkspell0 += surplus-dependency|CSWlibpangoft2-1-0-0
CHECKPKG_OVERRIDES_CSWlibgtkspell0 += surplus-dependency|CSWlibcairo2
CHECKPKG_OVERRIDES_CSWlibgtkspell0 += surplus-dependency|CSWlibpangocairo1-0-0
CHECKPKG_OVERRIDES_CSWlibgtkspell0 += surplus-dependency|CSWlibgio2-0-0
CHECKPKG_OVERRIDES_CSWlibgtkspell0 += surplus-dependency|CSWlibgdk-x11-2-0-0
CHECKPKG_OVERRIDES_CSWlibgtkspell0 += surplus-dependency|CSWlibatk1-0-0
CHECKPKG_OVERRIDES_CSWlibgtkspell0 += surplus-dependency|CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWlibgtkspell0 += surplus-dependency|CSWlibgdk-pixbuf2-0-0
CHECKPKG_OVERRIDES_CSWlibgtkspell0 += surplus-dependency|CSWlibpango1-0-0

PACKAGES += CSWlibgtkspell-dev
SPKG_DESC_CSWlibgtkspell-dev = $(DESCRIPTION), development files
PKGFILES_CSWlibgtkspell-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgtkspell-dev += CSWlibgtkspell0

PACKAGES += CSWgtkspell-doc
ARCHALL_CSWgtkspell-doc = 1
SPKG_DESC_CSWgtkspell-doc = $(DESCRIPTION), documentation
PKGFILES_CSWgtkspell-doc = $(sharedstatedir)/gtk-doc.*

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
