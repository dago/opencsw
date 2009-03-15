GARNAME = gtk-doc
GARVERSION = 1.11
CATEGORIES = gnome

DESCRIPTION = GTK-Doc is used to document C code.
define BLURB
	GTK-Doc is used to document C code. It is typically used to document the
	public API of libraries, such as the GTK+ and GNOME libraries. But it can
	also be used to document application code. 
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWgtkdoc, )

PREREQUISITE_PKGS += CSWsgmlcommon CSWxmlcommon CSWdocbookxsl CSWscrollkeeper
PREREQUISITE_PKGS += CSWopenjade

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-xml-catalog=/opt/csw/etc/xml/catalog

#TEST_TARGET = check
TEST_TARGET =

include gar/category.mk
