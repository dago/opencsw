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

PACKAGES += CSWlibcppunit1-12-1-gxx
SPKG_DESC_CSWlibcppunit1-12-1-gxx = C++ port of JUnit, libcppunit-1.12.so.1
PKGFILES_CSWlibcppunit1-12-1-gxx += $(call pkgfiles_lib,libcppunit-1.12.so.1)
RUNTIME_DEP_PKGS_CSWlibcppunit1-12-1-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibcppunit1-12-1-gxx += CSWlibstdc++6

PACKAGES += CSWcppunit-gxx-dev
SPKG_DESC_CSWcppunit-gxx-dev = Development files C++ port of JUnit
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWcppunit-gxx-dev += CSWlibcppunit1-12-1-gxx
RUNTIME_DEP_PKGS_CSWcppunit-gxx-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcppunit-gxx-dev += CSWlibstdc++6

# This is just an example
CHECKPKG_OVERRIDES_CSWcppunit-gxx-dev += file-with-bad-content|/usr/local|root/opt/csw/gxx/share/doc/cppunit/money_example.html

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
prefix = $(BUILD_PREFIX)/gxx
GARCOMPILER = GNU

BUILD64 = 1

include gar/category.mk

post-patch-modulated:
	-cd $(WORKSRC) && autoreconf -fi
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)$(BUILD_PREFIX)/share/aclocal
	ln -s $(sharedstatedir)/aclocal/cppunit.m4 $(DESTDIR)$(BUILD_PREFIX)/share/aclocal/cppunit.m4
	@$(MAKECOOKIE)
