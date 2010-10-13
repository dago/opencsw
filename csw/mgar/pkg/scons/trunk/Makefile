GARNAME = scons
GARVERSION = 1.3.1
CATEGORIES = python

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
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
SPKG_SOURCEURL = http://www.scons.org/
LICENSE = LICENSE.txt
CONFIGURE_SCRIPTS =
TEST_SCRIPTS = 
EXTRA_PAX_ARGS = -s ",\./opt/csw/man,./opt/csw/share/man,"
ARCHALL = 1
EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/$(GARNAME)-$(GARVERSION)/SCons/.*\.py[co]
include gar/category.mk
