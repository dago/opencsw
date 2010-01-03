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

REQUIRED_PKGS_CSWgtksourceview += CSWfconfig CSWftype2 CSWgconf2 CSWggettextrt 
REQUIRED_PKGS_CSWgtksourceview += CSWglib2 CSWgtk2 CSWlibatk CSWlibcairo
REQUIRED_PKGS_CSWgtksourceview += CSWlibxml2 CSWpango CSWlibxext
REQUIRED_PKGS_CSWgtksourceviewdev += CSWgtksourceview
REQUIRED_PKGS_CSWgtksourceviewdoc += CSWgtksourceview

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/GtkSourceView

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
#This is ugly, should be EXTRA_LINKER_FLAGS, but due to libtool it doesn't work
EXTRA_LD_FLAGS_isa-i386    = -L/usr/openwin/lib -lXext
EXTRA_LD_FLAGS_isa-sparcv8 = -L/usr/openwin/lib -lXext
EXTRA_LD_FLAGS_isa-amd64   = -L/usr/openwin/lib/amd64 -lXext
EXTRA_LD_FLAGS_isa-sparcv9 = -L/usr/openwin/lib/sparcv9 -lXext
EXTRA_LD_FLAGS += $(EXTRA_LD_FLAGS_$(MODULATION))

#NO_ISAEXEC = 1
#NOISALIST = 1
# gconf-2 not 64-bit yet
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

STRIP_LIBTOOL = 1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
