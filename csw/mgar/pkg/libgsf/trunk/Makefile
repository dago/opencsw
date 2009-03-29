GARNAME = libgsf
GARVERSION = 1.14.11
CATEGORIES = gnome

DESCRIPTION = GNOME Structured File Library
define BLURB
	The GNOME Structured File Library (GSF) is an I/O abstraction for
	reading/writing compound files. GSF is released under the GNU Lesser
	General Public License (GNU LGPL), which allows for flexible licensing of
	client applications. 
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PREREQUISITE_PKGS += CSWgnulinks CSWgtk-doc CSWglib2devel CSWlibxml2devel

REQUIRED_PKGS += CSWbonobo2 CSWbzip2 CSWgconf2 CSWggettextrt CSWglib2
REQUIRED_PKGS += CSWgnomevfs2 CSWlibxml2 CSWorbit2 CSWzlib CSWiconv

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz


#NPATH = /opt/csw/gnu:$(PATH)

CONFIGURE_ARGS = $(DIRPATHS)
#CONFIGURE_ARGS = "PATH=$(NPATH)" $(DIRPATHS)
#CONFIGURE_ARGS += --enable-gtk-doc=no
#CONFIGURE_ARGS += --disable-man-gtk-doc

TEST_TARGET = check

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-configure-$(MODULATION):
	@(echo "~~~ Fixing Libtool ~~~")
	@$(FILEDIR)/fixme.sh $(WORKSRC)
	$(DONADA)

post-install-isa-sparcv8:
	@cp -p $(FILEDIR)/libgsf-1.so.1.9.1.s $(INSTALLISADIR)$(libdir)/libgsf-1.so.1.9.1
	@cp -p $(FILEDIR)/libgsf-gnome-1.so.1.9.1.s $(INSTALLISADIR)$(libdir)/libgsf-gnome-1.so.1.9.1
	@ln -s libgsf-1.so.1.9.1 $(INSTALLISADIR)$(libdir)/libgsf-1.so.1
	@ln -s libgsf-gnome-1.so.1.9.1 $(INSTALLISADIR)$(libdir)/libgsf-gnome-1.so.1

post-install-isa-i386:
	@cp -p $(FILEDIR)/libgsf-1.so.1.9.1.i $(INSTALLISADIR)$(libdir)/libgsf-1.so.1.9.1
	@cp -p $(FILEDIR)/libgsf-gnome-1.so.1.9.1.i $(INSTALLISADIR)$(libdir)/libgsf-gnome-1.so.1.9.1
	@ln -s libgsf-1.so.1.9.1 $(INSTALLISADIR)$(libdir)/libgsf-1.so.1
	@ln -s libgsf-gnome-1.so.1.9.1 $(INSTALLISADIR)$(libdir)/libgsf-gnome-1.so.1
