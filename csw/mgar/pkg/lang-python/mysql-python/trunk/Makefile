# $Id$

NAME = MySQL-python
VERSION = 1.2.4b4
CATEGORIES = python
GARTYPE = v2

define BLURB
  MySQL support for Python
endef

SF_PROJECT = $(call TOLOWER,$(NAME))
DISTFILES    = $(DISTNAME).zip

PATCHFILES += 0001-Disable-the-stupid-download.-We-have-setuptools.patch
PATCHFILES += 0002-Remove-GCC-incompatible-compilation-flags.patch
# PATCHFILES_2_7 += 0002-Remove-GCC-incompatible-compilation-flags.patch
# PATCHFILES += $(PATCHFILES_$(PYTHON_VERSION))

BUILD_DEP_PKGS = CSWpy-setuptools
PACKAGES = CSWpy-mysql
RUNTIME_DEP_PKGS_CSWpy-mysql += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-mysql += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWpy-mysql += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-mysql += CSWlibpython2-7-1-0
SPKG_DESC_CSWpy-mysql = MySQL Support for Python

OBSOLETED_BY_CSWpy-mysql = CSWpymysql

SKIPTEST = 1

CHECKPKG_OVERRIDES_CSWpy-mysql += binary-architecture-does-not-match-placement|file=opt/csw/lib/python2.6/site-packages/_mysql.so|arch_id=18|arch_name=sparcv8+

include gar/category.mk
