# $Id$

NAME = scons
VERSION = 2.3.0
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = A next-generation build tool
define BLURB
  SCons is an Open Source software construction tool - that is,
  a next-generation build tool. Think of SCons as an improved,
  cross-platform substitute for the classic Make utility with
  integrated functionality similar to autoconf/automake and compiler
  caches such as ccache. In short, SCons is an easier, more
  reliable and faster way to build software.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES += $(NAME)-$(VERSION).tar.gz

# We have only one package and that is archall, choose sparc
# We need libserf on Solaris 9 for subversion and that requires a current scons
PACKAGING_PLATFORMS = solaris9-sparc

VENDOR_URL = http://www.scons.org/

PACKAGES += CSWscons
SPKG_DESC_CSWscons = A next-generation build tool
# PKGFILES is catchall
ARCHALL_CSWscons = 1
CHECKPKG_OVERRIDES_CSWscons += file-with-bad-content

CONFIGURE_SCRIPTS =
TEST_SCRIPTS = 
EXTRA_PAX_ARGS = -s ",\./opt/csw/man,./opt/csw/share/man,"

EXTRA_MERGE_EXCLUDE_FILES = .*\.py[co]

include gar/category.mk
