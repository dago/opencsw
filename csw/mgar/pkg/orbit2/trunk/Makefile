GARNAME = ORBit2
GARVERSION = 2.14.17
CATEGORIES = lib

DESCRIPTION = ORBit 2.x CORBA tools and libs
define BLURB
  ORBit2 is a CORBA 2.4-compliant Object Request Broker (ORB) featuring
  mature C, C++ and Python bindings.
endef

MASTER_SITES = $(GNOME_MIRROR)

SPKG_SOURCEURL = http://projects.gnome.org/ORBit2/

DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)
STRIP_LIBTOOL = 1

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
NO_ISAEXEC = 1

TEST_TARGET = check

include gar/category.mk
