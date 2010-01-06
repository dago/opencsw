GARNAME = scons
GARVERSION = 1.2.0
CATEGORIES = devel

DESCRIPTION = A next-generation build tool
define BLURB
  SCons is an Open Source software construction tool - that is,
  a next-generation build tool. Think of SCons as an improved,
  cross-platform substitute for the classic Make utility with
  integrated functionality similar to autoconf/automake and compiler
  caches such as ccache. In short, SCons is an easier, more
  reliable and faster way to build software.
endef

SF_PROJ = scons
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.scons.org/

LICENSE = LICENSE.txt

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS = --root=$(DESTDIR)

EXTRA_PAX_ARGS = -s ",\./opt/csw/man,./opt/csw/share/man,"

ARCHALL = 1

include gar/category.mk
