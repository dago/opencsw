# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = rpm
VERSION = 4.10.2
GARTYPE = v2
CATEGORIES = default

DESCRIPTION = Package manager
define BLURB
 The RPM Package Manager (RPM) is a powerful command line driven package management system capable of installing, uninstalling,
 verifying, querying, and updating computer software packages. Each software package consists of an archive of files along with
 information about the package like its version, a description, and the like. There is also a library API, permitting advanced
 developers to manage such transactions from programming languages such as C or Python.
endef

MASTER_SITES = http://rpm.org/releases/rpm-4.10.x/
DISTFILES    = $(NAME)-$(VERSION).tar.bz2
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
LICENSE = COPYING

PACKAGES += CSWrpm
CATALOGNAME_CSWrpm = rpm
SPKG_DESC_CSWrpm += $(DESCRIPTION)
PACKAGES += CSWrpm-dev
CATALOGNAME_CSWrpm-dev = rpm_dev
SPKG_DESC_CSWrpm-dev += $(DESCRIPTION), development files
PKGFILES_DEVEL = /opt/csw/lib/librpm.so /opt/csw/lib/librpmbuild.so /opt/csw/lib/librpmio.so /opt/csw/lib/librpmsign.so
PKGFILES_DEVEL += /opt/csw/include/rpm/*.h
PKGFILES_CSWrpm-dev = $(PKGFILES_DEVEL)

GARCOMPILER = GCC4
BUILD_DEP_PKGS_CSWrpm	= CSWgcc4core CSWgcc4g++ CSWpython-dev CSWlibmagic-dev CSWlibmagic-data CSWlibnss-dev CSWnspr-dev
BUILD_DEP_PKGS_CSWrpm	+= CSWlibpopt-dev CSWbdb48 CSWpysqlite2 CSWzlib CSWpkgconfig CSWlibssp0
BUILD_DEP_PKGS_CSWrpm	+= CSWlibplc4 CSWlibplds4 CSWbdb48devel CSWlibsoftokn3 CSWliblzma-dev CSWlibz1

RUNTIME_DEP_PKGS_CSWrpm  = CSWpython CSWbdb48 CSWpysqlite2 CSWlibmagic-data CSWlibnss3 CSWlibnspr4 CSWzlib CSWggettext 
RUNTIME_DEP_PKGS_CSWrpm  += CSWggettext-data CSWlibgcc-s1 CSWlibssp0 CSWlibplc4 CSWlibplds4 CSWlibpopt0 CSWlibsoftokn3 CSWliblzma5
RUNTIME_DEP_PKGS_CSWrpm += CSWlibfreebl3 CSWgzip CSWstar CSWgnupg CSWlzip CSWxz CSWcurl CSWperl CSWosshclient CSWlibmagic1
RUNTIME_DEP_PKGS_CSWrpm  += CSWlibbz2-1-0 CSWlibintl8 CSWlibpython2-6-1-0 CSWlibz1
RUNTIME_DEP_PKGS_CSWrpm-dev += CSWrpm

PATCHFILES += 0001-Solaris-compile-fixes.patch 0002-rpm-default-shell-should-be-bash-instead-of-sh.patch 0003-make-sure-that-rpmquery-rpmverify-are-pointing-to-th.patch 0004-fdatasync-fix.patch

CFLAGS = -I/opt/csw/include -I/opt/csw/include/nss -I/opt/csw/include/nspr -I/opt/csw/bdb48/include -I/opt/csw/include/python2.6 -m32 -D_XPG6 -lssp -lssp_nonshared -std=gnu99 -lintl -lrt

CPPFLAGS = $(CFLAGS)

LDFLAGS = -m32 -L/opt/csw/lib -Wl,-R,/opt/csw/lib -L/opt/csw/bdb48/lib -Wl,-R,/opt/csw/bdb48/lib -Wl,-R'\$$\$$ORIGIN' -Wl,-R'\$$\$$ORIGIN/../lib' -Wl,-R'\$$\$$ORIGIN/../../lib' -lssp -lssp_nonshared -lm -lintl -lrt -z ignore -Bdirect

NORUNPATH = 1
NOISALIST = 1

CONFIGURE_ARGS  = $(DIRPATHS) --with-external-db --enable-python --without-lua --without-hackingdocs --without-selinux


# CHECKPKG 
CHECKPKG_OVERRIDES_CSWrpm += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWrpm += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWrpm += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWrpm += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWrpm += no-direct-binding
CHECKPKG_OVERRIDES_CSWrpm += soname-unused
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWlibnspr4
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWzlib
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWpysqlite2
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWlibplc4
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWlibmagic-data
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWgzip
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWlibplds4
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWcurl
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWggettext
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWggettext-data
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWlibsoftokn3
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWlibfreebl3
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWxz
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWlzip
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWgnupg
CHECKPKG_OVERRIDES_CSWrpm += surplus-dependency|CSWosshclient
CHECKPKG_OVERRIDES_CSWrpm += file-with-bad-content|/usr/share|root/opt/csw/lib/rpm/mono-find-provides
CHECKPKG_OVERRIDES_CSWrpm += file-with-bad-content|/usr/share|root/opt/csw/lib/rpm/fontconfig.prov
CHECKPKG_OVERRIDES_CSWrpm += file-with-bad-content|/usr/share|root/opt/csw/lib/rpm/mono-find-requires
CHECKPKG_OVERRIDES_CSWrpm += file-with-bad-content|/usr/share|root/opt/csw/lib/rpm/brp-compress
CHECKPKG_OVERRIDES_CSWrpm += file-with-bad-content|/usr/local|root/opt/csw/lib/rpm/check-rpaths-worker

include gar/category.mk
