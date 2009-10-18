# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = pysvn
GARVERSION = 1.7.1
CATEGORIES = lib
DESCRIPTION = python
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
SPKG_SOURCEURL = http://pysvn.tigris.org/
MASTER_SITES = http://pysvn.barrys-emacs.org/source_kits/
PATCHFILES  = 0002-pysvn.hpp-string-includes-first.patch
PATCHFILES += 0005-Use-dash-capital-R-for-runtime-path.patch
PATCHFILES += 0006-Use-opt-csw-lib.patch
PATCHFILES += 0003-bin-bash-instead-of-bin-sh.patch
PATCHFILES += 0001-fixes-for-tests.patch
PATCHFILES += 0008-gid-in-two-more-places.patch
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
REQUIRED_PKGS  = CSWexpat
REQUIRED_PKGS += CSWgcc3core
REQUIRED_PKGS += CSWgcc3corert
REQUIRED_PKGS += CSWgcc3g++
REQUIRED_PKGS += CSWgcc3g++rt
REQUIRED_PKGS += CSWgcc4corert
REQUIRED_PKGS += CSWgcc4g++rt
REQUIRED_PKGS += CSWneon
REQUIRED_PKGS += CSWsvn

PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWsvn-devel CSWapache2-devel CSWbash
INCOMPATIBELE_PKGS = CSWpyxml
CONFIGURE_SCRIPTS = pysvn
BUILD_SCRIPTS = pysvn
INSTALL_SCRIPTS = pysvn
TEST_SCRIPTS_5.8 =
TEST_SCRIPTS_5.9 = pysvn
TEST_SCRIPTS_5.10 = pysvn
TEST_SCRIPTS = $(TEST_SCRIPTS_$(GAROSREL))
CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER = GNU

include gar/category.mk

configure-pysvn:
	(cd $(WORKSRC)/Source \
		&& $(CONFIGURE_ENV) python setup.py configure \
			--apr-inc-dir=/opt/csw/apache2/include \
			--apr-lib-dir=/opt/csw/apache2/lib \
			--svn-bin-dir=/opt/csw/bin \
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
