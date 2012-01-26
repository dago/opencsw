# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = twisted
MAJ_VERSION = 10.2
PATCHLEVEL = 0
VERSION = $(MAJ_VERSION).$(PATCHLEVEL)
CATEGORIES = python
GARTYPE = v2

define BLURB
  Twisted is a networking engine written in Python, supporting numerous
  protocols. It contains a web server, numerous chat clients, chat servers,
  mail servers, and more.
endef

UPSTREAM_NAME = Twisted
DISTNAME      = $(UPSTREAM_NAME)-$(VERSION)
MASTER_SITES  = http://tmrc.mit.edu/mirror/$(NAME)/$(UPSTREAM_NAME)/$(MAJ_VERSION)/
DISTFILES     = $(DISTNAME).tar.bz2
TEST_SCRIPTS  = 
LICENSE       = LICENSE

PACKAGES       = CSWpy-twisted
RUNTIME_DEP_PKGS_CSWpy-twisted += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-twisted += CSWpy-zope-interface
SPKG_DESC_CSWpy-twisted = An event-driven networking engine
CATALOGNAME_CSWpy-twisted = py_twisted

OBSOLETED_BY_CSWpy-twisted = CSWtwisted

ARCHALL_CSWtwisted = 1

# CSWtwisted is now empty, so we need to tell checkpkg that it really needs to
# depend on these two packages.
CHECKPKG_OVERRIDES_CSWtwisted += surplus-dependency|CSWpy-twisted
CHECKPKG_OVERRIDES_CSWtwisted += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpy-twisted += surplus-dependency|CSWpy-zope-interface
CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/twisted/python/_twisted_zsh_stub
CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/twisted/tap/ftp.py
CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/twisted/conch/unix.py
CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/twisted/conch/openssh_compat/factory.py
CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/twisted/scripts/tap2deb.py

include gar/category.mk
