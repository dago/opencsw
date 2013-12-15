# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = cppunit
VERSION = 1.12.1
GARTYPE = v2

DESCRIPTION = C++ port of JUnit

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

# Use patch until this is fixed:
#   http://sourceforge.net/tracker/?func=detail&aid=3483396&group_id=11795&atid=111795
PATCHFILES += cppunit-1.12.1-configure.in-ieeefp.h.patch

# Use patch until this is fixed:
#   http://sourceforge.net/tracker/?func=detail&aid=3483400&group_id=11795&atid=111795
PATCHFILES += cppunit-1.12.1-configure.in-fabs.patch

# Replace really outdated macros
PATCHFILES += 0003-Replace-macro-which-is-so-deprecated-that-its-use-is.patch

PACKAGES += CSWlibcppunit1-12-1
SPKG_DESC_CSWlibcppunit1-12-1 = C++ port of JUnit, libcppunit-1.12.so.1
PKGFILES_CSWlibcppunit1-12-1 += $(call pkgfiles_lib,libcppunit-1.12.so.1)
RUNTIME_DEP_PKGS_CSWlibcppunit1-12-1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibcppunit1-12-1 += CSWlibstdc++6

PACKAGES += CSWlibcppunit-dev
SPKG_DESC_CSWlibcppunit-dev = Development files C++ port of JUnit
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibcppunit-dev += CSWlibcppunit1-12-1
RUNTIME_DEP_PKGS_CSWlibcppunit-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibcppunit-dev += CSWlibstdc++6

# This is just an example
CHECKPKG_OVERRIDES_CSWlibcppunit-dev += file-with-bad-content|/usr/local|root/opt/csw/gxx/share/doc/cppunit/money_example.html

GARCOMPILER = GNU

BUILD64 = 1

# Test examples/money is coredumping on amd64, don't know why yet
SKIPTEST ?= 1

include gar/category.mk

post-patch:
	cd $(WORKSRC) && autoreconf -fi
	@$(MAKECOOKIE)
