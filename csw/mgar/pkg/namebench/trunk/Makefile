NAME = namebench
VERSION = 1.3.1
CATEGORIES = python

DESCRIPTION = DNS benchmark utility
define BLURB
  DNS benchmark utility
endef

MASTER_SITES = http://namebench.googlecode.com/files/
DISTFILES  = $(NAME)-$(VERSION)-source.tgz

LICENSE = COPYING

PACKAGES = CSWnamebench
CATALOGNAME = namebench
SPKG_SOURCEURL = http://code.google.com/p/namebench

RUNTIME_DEP_PKGS = CSWpython-tk

ARCHALL = 1

TEST_SCRIPTS =

CHECKPKG_OVERRIDES_CSWnamebench += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWnamebench += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWnamebench += surplus-dependency|CSWpython-tk
CHECKPKG_OVERRIDES_CSWnamebench += file-with-bad-content|/usr/local|root/opt/csw/namebench/config/data_sources.cfg
CHECKPKG_OVERRIDES_CSWnamebench += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/libnamebench/util.py
CHECKPKG_OVERRIDES_CSWnamebench += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/libnamebench/util.py

include gar/category.mk
