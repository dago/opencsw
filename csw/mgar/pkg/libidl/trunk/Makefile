GARNAME = libIDL
GARVERSION = 0.8.13
CATEGORIES = lib

DESCRIPTION = Library for handling CORBA IDL
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)

REQUIRED_PKGS = CSWggettextrt CSWglib2

SPKG_SOURCEURL = http://projects.gnome.org/$(GARNAME)/

DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)
STRIP_LIBTOOL = 1

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
NO_ISAEXEC = 1

TEST_TARGET = check

PACKAGES = CSWlibidl

include gar/category.mk
