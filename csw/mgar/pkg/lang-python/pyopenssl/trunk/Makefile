# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pyOpenSSL
VERSION = 0.11
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = OpenSSL bindings for Python
define BLURB
  Long description
endef

MASTER_SITES = http://launchpad.net/pyopenssl/main/$(VERSION)/+download/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES = CSWpy-openssl
RUNTIME_DEP_PKGS_CSWpy-openssl += CSWosslrt
RUNTIME_DEP_PKGS_CSWpy-openssl += CSWlibpython2-6-1-0

TEST_SCRIPTS =

include gar/category.mk

