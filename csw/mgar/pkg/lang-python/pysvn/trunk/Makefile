# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pysvn
VERSION = 1.7.6
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = Python SVN Extension and WorkBench GUI
define BLURB

  The pysvn project's goal is to enable Tools to be written in Python that use
  Subversion.

  Windows, Mac OS X, Linux and other unix platforms are supported.

  pysvn Extension Features

  * Supports all svn client features
  * Supports svn transaction features required to write svn pre-commit hooks
  * Easy to learn and use
  * Python like interface
  * Good Documentation and examples
  * No need to understand the Subversion C API

endef

MASTER_SITES = http://pysvn.barrys-emacs.org/source_kits/
DISTFILES += $(DISTNAME).tar.gz
PATCHFILES  = 0002-pysvn.hpp-string-includes-first.patch
#PATCHFILES += 0005-Use-dash-capital-R-for-runtime-path.patch
#ÃPATCHFILES += 0006-Use-opt-csw-lib.patch
PATCHFILES += 0003-bin-bash-instead-of-bin-sh.patch
PATCHFILES += 0001-fixes-for-tests.patch
PATCHFILES += 0008-gid-in-two-more-places.patch

# svn_lib_dir is incorrectly used instead of SVN_LIB
# in configure
PATCHFILES += 0004-fixes-SVN_LIB-macro.patch

# rpath option is a gnu ld one but not a SUN ld one
PATCHFILES += 0005-no-rpath-with-SUN-ld.patch

# pysvn tries to use en_GB.utf8 not available during a test
# let's rather use the default one
PATCHFILES += 0006-fix-test-locale-problem.patch

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://pysvn.tigris.org/

LICENSE = LICENSE.txt

BUILD_DEP_PKGS += CSWsvn-devel
BUILD_DEP_PKGS += CSWapache2-dev
BUILD_DEP_PKGS += CSWlibexpat-dev
BUILD_DEP_PKGS += CSWbash

RUNTIME_DEP_PKGS += CSWlibneon27
RUNTIME_DEP_PKGS += CSWlibgcc-s1
RUNTIME_DEP_PKGS += CSWlibstdc++6
RUNTIME_DEP_PKGS += CSWpython
RUNTIME_DEP_PKGS += CSWsvn
RUNTIME_DEP_PKGS += CSWlibexpat1


INCOMPATIBELE_PKGS = CSWpyxml

CONFIGURE_SCRIPTS = pysvn
BUILD_SCRIPTS = pysvn
INSTALL_SCRIPTS = pysvn
TEST_SCRIPTS_5.8 =
TEST_SCRIPTS_5.9 = pysvn
TEST_SCRIPTS_5.10 = pysvn
TEST_SCRIPTS = $(TEST_SCRIPTS_$(GAROSREL))
CONFIGURE_ARGS = $(DIRPATHS)
#GARCOMPILER = GNU


include gar/category.mk

configure-pysvn:
	(cd $(WORKSRC)/Source \
		&& $(CONFIGURE_ENV) python setup.py configure \
			--apr-inc-dir=$(includedir) \
			--apr-lib-dir=$(libdir) \
			--apu-inc-dir=$(includedir) \
			--svn-bin-dir=$(bindir) \
			--svn-inc-dir=/opt/csw/include/subversion-1 \
			--svn-lib-dir=/opt/csw/lib/svn \
	)
	@$(MAKECOOKIE)

build-pysvn:
	(cd $(WORKSRC)/Source \
		&& $(BUILD_ENV) gmake \
	)
	@$(MAKECOOKIE)

test-pysvn:
	(cd $(WORKSRC)/Tests && gmake)
	@$(MAKECOOKIE)

install-pysvn:
	ginstall -m 755 -d $(DESTDIR)$(libdir)/python/site-packages/pysvn
	ginstall -m 644 $(WORKSRC)/Source/pysvn/__init__.py $(DESTDIR)$(libdir)/python/site-packages/pysvn
	$(foreach F,$(wildcard $(WORKSRC)/Source/pysvn/_pysvn*.so),ginstall -m 755 $(F) $(DESTDIR)$(libdir)/python/site-packages/pysvn)
	@$(MAKECOOKIE)
