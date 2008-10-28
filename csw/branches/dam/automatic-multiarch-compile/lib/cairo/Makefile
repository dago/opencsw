GARNAME = cairo
GARVERSION = 1.8.0
CATEGORIES = lib

DESCRIPTION = The Cairo 2D Graphics Library
define BLURB
  Cairo is a 2D graphics library with support for multiple output devices.
  Currently supported output targets include the X Window System, Quartz,
  Win32, image buffers, PostScript, PDF, and SVG file output.
endef

MASTER_SITES = http://www.cairographics.org/releases/
SOURCEFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES  = $(SOURCEFILES)
DISTFILES += $(call admfiles,CSWlibcairo,depend)

CONFIGURE_ARGS  = $(DIRPATHS)

BUILD64 = 1

MERGE_SCRIPTS_isa-i386-pkgversion-0.25.4 = copy-only
MERGE_DIRS_isa-i386-pkgversion-0.25.4 = $(libdir)
MERGE_SCRIPTS_isa-amd64-pkgversion-0.25.4 = copy-relocated-only
MERGE_DIRS_isa-amd64-pkgversion-0.25.4 = $(libdir)

include ../category.mk
