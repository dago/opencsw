NAME = libIDL
VERSION = 0.8.14
CATEGORIES = lib

DESCRIPTION = Library for handling CORBA IDL
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)

RUNTIME_DEP_PKGS = CSWggettextrt CSWglib2

SPKG_SOURCEURL = http://projects.gnome.org/$(NAME)/

DISTFILES = $(NAME)-$(VERSION).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)
STRIP_LIBTOOL = 1

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
NOISAEXEC = 1

TEST_TARGET = check

PACKAGES = CSWlibidl

CPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CPP
CXXCPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CXXCPP

include gar/category.mk
