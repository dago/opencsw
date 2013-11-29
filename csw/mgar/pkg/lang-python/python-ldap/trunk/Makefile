# $Id$
NAME = python-ldap
VERSION = 2.4.13
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = LDAP bindings for Python
define BLURB
  python-ldap provides an object-oriented API to access LDAP directory
  servers from Python programs. Mainly it wraps the OpenLDAP 2.x libs
  for that purpose.
endef

MASTER_SITES += $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz
PATCHFILES += 0000-openldap-path.patch

VENDOR_URL = http://www.python-ldap.org/
LICENSE = LICENCE

BUILD_DEP_PKGS += CSWpython-dev
BUILD_DEP_PKGS += CSWopenldap-dev
BUILD_DEP_PKGS += CSWsasl-dev

PACKAGES = CSWpy-ldap
SPKG_DESC_CSWpy-ldap = LDAP bindings for Python
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpy-ldap += CSWlibldap-r2-4-2
RUNTIME_DEP_PKGS_CSWpy-ldap += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-ldap += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-ldap += CSWlibgcc-s1

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
