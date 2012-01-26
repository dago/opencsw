# $Id$
NAME = python-ldap
VERSION = 2.3.12
CATEGORIES = python
GARTYPE = v2
PACKAGES = CSWpy-ldap
CATALOGNAME = py_ldap
LICENSE = LICENCE

DESCRIPTION = LDAP bindings for Python
define BLURB
  python-ldap provides an object-oriented API to access LDAP directory
  servers from Python programs. Mainly it wraps the OpenLDAP 2.x libs
  for that purpose.
endef

BUILD_DEP_PKGS = CSWpython-devel CSWoldapdevel CSWossldevel
RUNTIME_DEP_PKGS_CSWpy-ldap += CSWsasl
RUNTIME_DEP_PKGS_CSWpy-ldap += CSWosslrt
RUNTIME_DEP_PKGS_CSWpy-ldap += CSWoldaprt
RUNTIME_DEP_PKGS_CSWpy-ldap += CSWlibpython2-6-1-0

MASTER_SITE_DIR = $(shell echo $(NAME) | cut -c 1)
MASTER_SITES = http://pypi.python.org/packages/source/$(MASTER_SITE_DIR)/$(NAME)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
VENDOR_URL = http://www.python-ldap.org/
PATCHFILES += 0000-openldap-path.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
