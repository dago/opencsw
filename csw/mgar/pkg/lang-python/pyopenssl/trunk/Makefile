# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pyOpenSSL
VERSION = 0.13.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = OpenSSL bindings for Python
define BLURB
  OpenSSL bindings for Python
endef

MASTER_SITE_DIR = $(shell echo $(NAME) | cut -c 1)
MASTER_SITES = http://pypi.python.org/packages/source/$(MASTER_SITE_DIR)/$(NAME)/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES = CSWpy-openssl
RUNTIME_DEP_PKGS_CSWpy-openssl += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWpy-openssl += CSWlibpython2-6-1-0

TEST_SCRIPTS =

include gar/category.mk

