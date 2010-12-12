NAME = libgsf
VERSION = 1.14.11
CATEGORIES = gnome

DESCRIPTION = GNOME Structured File Library
define BLURB
	The GNOME Structured File Library (GSF) is an I/O abstraction for
	reading/writing compound files. GSF is released under the GNU Lesser
	General Public License (GNU LGPL), which allows for flexible licensing of
	client applications. 
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

BUILD_DEP_PKGS += CSWgnulinks CSWgtk-doc CSWglib2devel CSWlibxml2devel

RUNTIME_DEP_PKGS += CSWbonobo2 CSWbzip2 CSWgconf2 CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS += CSWgnomevfs2 CSWlibxml2 CSWorbit2 CSWzlib

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_LD_OPTIONS = -L../gsf/.libs -L../../gsf/.libs

CONFIGURE_ARGS = $(DIRPATHS)
#CONFIGURE_ARGS = "PATH=$(NPATH)" $(DIRPATHS)
#CONFIGURE_ARGS += --enable-gtk-doc=no
#CONFIGURE_ARGS += --disable-man-gtk-doc

TEST_TARGET = check

# Missing 64-bit libs:
# libgnomevfs-2.so libgconf-2.so libbonobo-2.so libbonobo-activation.so
#BUILD64 = 1

STRIP_LIBTOOL = 1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-install-isa-sparcv8:
	@cp -p $(FILEDIR)/libgsf-1.so.1.9.1.s $(INSTALLISADIR)$(libdir)/libgsf-1.so.1
	@cp -p $(FILEDIR)/libgsf-gnome-1.so.1.9.1.s $(INSTALLISADIR)$(libdir)/libgsf-gnome-1.so.1

post-install-isa-i386:
	@cp -p $(FILEDIR)/libgsf-1.so.1.9.1.i $(INSTALLISADIR)$(libdir)/libgsf-1.so.1
	@cp -p $(FILEDIR)/libgsf-gnome-1.so.1.9.1.i $(INSTALLISADIR)$(libdir)/libgsf-gnome-1.so.1
