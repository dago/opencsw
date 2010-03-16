GARNAME = freeglut
GARVERSION = 2.6.0
CATEGORIES = lib

DESCRIPTION = OpenSourced alternative to the OpenGL Utility Toolkit
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = 0001-Add-support-for-Sun.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://freeglut.sourceforge.net/

DEP_PKGS = CSWmesa

# If we put the include into CPPFLAGS it is too ear√ly in the commandline
# and the installed headers take precedence over the newly built.
CPPFLAGS =
EXTRA_CFLAGS = -I/opt/csw/include

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# Drop after CSWmesa has been rebuild against CSW X11
# Drats, doesn't work here. Wait for CSWmesa
# EXTRA_LINKER_FLAGS = /usr/openwin/lib/libXext.so

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

TEST_TARGET = check

include gar/category.mk
