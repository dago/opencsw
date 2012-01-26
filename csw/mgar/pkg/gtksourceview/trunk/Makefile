NAME = gtksourceview
VERSION = 2.9.3
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = A text widget with features typical of a source code editor
define BLURB
	GtkSourceView is a text widget that extends the standard gtk+ 2.x
	text widget GtkTextView.

	It improves GtkTextView by implementing syntax highlighting and other
	features typical of a source code editor.
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWgtksourceview CSWgtksourceviewdev CSWgtksourceviewdoc
CATALOGNAME_CSWgtksourceview = gtksourceview
CATALOGNAME_CSWgtksourceviewdev = gtksourceview_devel
CATALOGNAME_CSWgtksourceviewdoc = gtksourceview_doc

SPKG_DESC_CSWgtksourceview += A text widget with features typical of a source code editor
SPKG_DESC_CSWgtksourceviewdev += A text widget with features typical of a source code editor - developer package
SPKG_DESC_CSWgtksourceviewdoc += A text widget with features typical of a source code editor - documentation

RUNTIME_DEP_PKGS_CSWgtksourceview += CSWfconfig CSWftype2 CSWgconf2 CSWggettextrt 
RUNTIME_DEP_PKGS_CSWgtksourceview += CSWglib2 CSWgtk2 CSWlibatk CSWlibcairo
RUNTIME_DEP_PKGS_CSWgtksourceview += CSWlibxml2 CSWpango CSWlibxext
RUNTIME_DEP_PKGS_CSWgtksourceviewdev += CSWgtksourceview
RUNTIME_DEP_PKGS_CSWgtksourceviewdoc += CSWgtksourceview

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/GtkSourceView

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

#NOISAEXEC = 1
#NOISALIST = 1
# gconf-2 not 64-bit yet
#BUILD64 = 1

PKGFILES_CSWgtksourceviewdev = $(PKGFILES_DEVEL)
PKGFILES_CSWgtksourceviewdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWgtksourceviewdoc = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

# Test fails due to:
# Xlib:  extension "Generic Event Extension" missing on display ":0.0".
#
#TEST_TARGET = check
TEST_TARGET = 

STRIP_LIBTOOL = 1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
