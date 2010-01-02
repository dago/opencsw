GARNAME = gtksourceview
GARVERSION = 2.9.3
CATEGORIES = gnome

DESCRIPTION = A text widget with features typical of a source code editor
define BLURB
	GtkSourceView is a text widget that extends the standard gtk+ 2.x
	text widget GtkTextView.

	It improves GtkTextView by implementing syntax highlighting and other
	features typical of a source code editor.
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTNAME  = $(GARNAME)-$(GARVERSION)

PACKAGES = CSWgtksourceview CSWgtksourceviewdev CSWgtksourceviewdoc
CATALOGNAME_CSWgtksourceview = gtksourceview
CATALOGNAME_CSWgtksourceviewdev = gtksourceview_devel
CATALOGNAME_CSWgtksourceviewdoc = gtksourceview_doc

SPKG_DESC_CSWgtksourceview += A text widget with features typical of a source code editor
SPKG_DESC_CSWgtksourceviewdev += A text widget with features typical of a source code editor - developer package
SPKG_DESC_CSWgtksourceviewdoc += A text widget with features typical of a source code editor - documentation

REQUIRED_PKGS_CSWgtksourceview += CSWfconfig CSWftype2 CSWgconf2 CSWggettextrt CSWglib2
REQUIRED_PKGS_CSWgtksourceview += CSWgtk2 CSWlibatk CSWlibcairo CSWlibxml2 CSWpango
REQUIRED_PKGS_CSWgtksourceviewdev += CSWgtksourceview
REQUIRED_PKGS_CSWgtksourceviewdoc += CSWgtksourceview

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/GtkSourceView

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

#NO_ISAEXEC = 1
#NOISALIST = 1
#BUILD64 = 1

PKGFILES_CSWgtksourceviewdev = $(PKGFILES_DEVEL)
PKGFILES_CSWgtksourceviewdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWgtksourceviewdoc = 1

CONFIGURE_ARGS = $(DIRPATHS)

# Test fails due to:
# Xlib:  extension "Generic Event Extension" missing on display ":0.0".
#
#TEST_TARGET = check
TEST_TARGET = 

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
