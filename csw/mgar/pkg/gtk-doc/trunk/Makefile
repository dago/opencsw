NAME = gtk-doc
VERSION = 1.11
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = GTK-Doc is used to document C code.
define BLURB
	GTK-Doc is used to document C code. It is typically used to document the
	public API of libraries, such as the GTK+ and GNOME libraries. But it can
	also be used to document application code. 
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWgtk-doc.postinstall
DISTFILES += CSWgtk-doc.postremove
CATALOGNAME_CSWgtk-doc = gtk_doc

BUILD_DEP_PKGS += CSWsgmlcommon CSWxmlcommon CSWdocbookxsl
BUILD_DEP_PKGS += CSWopenjade CSWgnomedocutils

RUNTIME_DEP_PKGS += CSWperl CSWpython CSWsgmlcommon CSWxmlcommon
RUNTIME_DEP_PKGS += CSWdocbookxsl CSWopenjade CSWgnomedocutils

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-xml-catalog=/opt/csw/etc/xml/catalog
CONFIGURE_ARGS += --disable-scrollkeeper

# xmllint test fail on buildfarm due to proxy requirement
# some other tests fail due to gtk-doc not installed (doh!)
#TEST_TARGET = check
TEST_TARGET =

include gar/category.mk
