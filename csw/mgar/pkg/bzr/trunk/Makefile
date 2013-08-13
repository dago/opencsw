# $Id$
#

NAME = bzr
VERSION = 2.6.0
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Next generation distributed version control
define BLURB
	Bazaar is a distributed revision control system. It allows team members
	to branch and merge upstream code very easily.
endef

MASTER_SITES = http://launchpad.net/bzr/2.6/$(VERSION)/\+download/
DISTFILES    = $(DISTNAME).tar.gz
PACKAGES     = CSWbzr
LICENSE = COPYING.txt
TEST_SCRIPTS =

RUNTIME_DEP_PKGS = CSWpy-crypto
RUNTIME_DEP_PKGS += CSWpy-paramiko
RUNTIME_DEP_PKGS += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWbzr += CSWlibgcc-s1

CHECKPKG_OVERRIDES_CSWbzr += surplus-dependency|CSWpy-crypto
CHECKPKG_OVERRIDES_CSWbzr += surplus-dependency|CSWpy-paramiko
CHECKPKG_OVERRIDES_CSWbzr += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWbzr += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWbzr += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/bzrlib/transport/http/_urllib2_wrappers.py
CHECKPKG_OVERRIDES_CSWbzr += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/bzrlib/transport/http/_urllib2_wrappers.py

include gar/category.mk

post-install-modulated:
	@mv $(DESTDIR)/opt/csw/man $(DESTDIR)/opt/csw/share

