# $Id$
NAME = django-auth-ldap
VERSION = 1.1.2
CATEGORIES = python
GARTYPE = v2
PACKAGES = CSWpy-django-auth-ldap
CATALOGNAME = py_django_auth_ldap
ARCHALL_CSWpy-django-auth-ldap = 1
LICENSE = PKG-INFO
RUNTIME_DEP_PKGS += CSWpy-django 
RUNTIME_DEP_PKGS += CSWpy-ldap

# checkpkg can't detect python run time dependencies
CHECKPKG_OVERRIDES_CSWpy-django-auth-ldap += surplus-dependency|CSWpy-ldap
CHECKPKG_OVERRIDES_CSWpy-django-auth-ldap += surplus-dependency|CSWpy-django

DESCRIPTION = Django LDAP authentication backend
define BLURB
  This is a Django authentication backend that authenticates against
  an LDAP service. Configuration can be as simple as a single
  distinguished name template, but there are many rich configuration
  options for working with users, groups, and permissions.
endef

# 1st char of NAME is the directory name
MASTER_SITE_DIR = $(shell echo $(NAME) | cut -c 1)
MASTER_SITES = http://pypi.python.org/packages/source/$(MASTER_SITE_DIR)/$(NAME)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
