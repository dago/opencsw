# $Id: Makefile 19383 2012-10-05 10:07:53Z bilko50000 $
#

NAME = bzr
VERSION = 2.5.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Next generation distributed version control
define BLURB
	Bazaar is a distributed revision control system. It allows team members
	to branch and merge upstream code very easily.
endef

MASTER_SITES = http://launchpad.net/bzr/2.5/$(VERSION)/\+download/
DISTFILES    = $(DISTNAME).tar.gz
PACKAGES     = CSWbzr
LICENSE = COPYING.txt
TEST_SCRIPTS = 

RUNTIME_DEP_PKGS = CSWpy-crypto
RUNTIME_DEP_PKGS += CSWpy-paramiko
RUNTIME_DEP_PKGS += CSWlibpython2-6-1-0

CHECKPKG_OVERRIDES_CSWbzr += surplus-dependency|CSWpy-crypto
CHECKPKG_OVERRIDES_CSWbzr += surplus-dependency|CSWpy-paramiko
CHECKPKG_OVERRIDES_CSWbzr += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWbzr += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWbzr += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/bzrlib/transport/http/_urllib2_wrappers.py

include gar/category.mk

post-install-modulated:
	@mv $(DESTDIR)/opt/csw/man $(DESTDIR)/opt/csw/share

