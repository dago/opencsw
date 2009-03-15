GARNAME = gtk-doc
GARVERSION = 1.11
CATEGORIES = gnome

DESCRIPTION = Brief description
define BLURB
  Long description
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
