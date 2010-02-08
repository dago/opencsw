GARNAME = gnome-mime-data
GARVERSION = 2.18.0
CATEGORIES = gnome

DESCRIPTION = Contains the base set of file types and applications for GNOME-2
define BLURB
endef

GNOME_PROJ = gnome-mime-data
MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTNAME  = $(GNOME_PROJ)-$(GARVERSION)

PACKAGES = CSWgmimedata CSWgmimedatadevel CSWgmimedatadoc
CATALOGNAME_CSWgmimedata = gmimedata
CATALOGNAME_CSWgmimedatadevel = gmimedata_devel
CATALOGNAME_CSWgmimedatadoc = gmimedata_doc

SPKG_DESC_CSWgmimedata += $(DESCRIPTION)
SPKG_DESC_CSWgmimedatadevel += $(DESCRIPTION) - developer package
SPKG_DESC_CSWgmimedatadoc += $(DESCRIPTION) - documentation

RUNTIME_DEP_PKGS_CSWgmimedatadevel += CSWgmimedata
RUNTIME_DEP_PKGS_CSWgmimedatadoc += CSWgmimedata

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/gmimedata

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD64 = 1

PKGFILES_CSWgmimedatadevel = $(PKGFILES_DEVEL)
PKGFILES_CSWgmimedatadoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWgmimedatadoc = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
