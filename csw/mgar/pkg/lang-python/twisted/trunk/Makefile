# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = Twisted
VERSION = 13.1.0
CATEGORIES = python
GARTYPE = v2

define BLURB
  Twisted is a networking engine written in Python, supporting numerous
  protocols. It contains a web server, numerous chat clients, chat servers,
  mail servers, and more.
endef

MASTER_SITES += $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.bz2

# For /usr/include/sys/socket.h to make msghdr.msg_control available.
# Add definition until this is fixed:
#   https://twistedmatrix.com/trac/ticket/6787
EXTRA_CPPFLAGS += -D_XPG4_2

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpy-zope-interface
BUILD_DEP_PKGS += CSWpy-openssl

PACKAGES += CSWpy-twisted
SPKG_DESC_CSWpy-twisted = An event-driven networking engine
RUNTIME_DEP_PKGS_CSWpy-twisted += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-twisted += CSWpy-zope-interface
RUNTIME_DEP_PKGS_CSWpy-twisted += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-twisted += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-twisted += CSWpy-crypto
RUNTIME_DEP_PKGS_CSWpy-twisted += CSWpy-asn1
OBSOLETED_BY_CSWpy-twisted = CSWtwisted

CHECKPKG_OVERRIDES_CSWpy-twisted += surplus-dependency|CSWpy-zope-interface
CHECKPKG_OVERRIDES_CSWpy-twisted += surplus-dependency|CSWpy-crypto
CHECKPKG_OVERRIDES_CSWpy-twisted += surplus-dependency|CSWpy-asn1

CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/twisted/conch/unix.py
CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/twisted/conch/unix.py
CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/twisted/conch/openssh_compat/factory.py
CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/twisted/conch/openssh_compat/factory.py
CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/twisted/tap/ftp.py
CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/twisted/tap/ftp.py
CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/twisted/scripts/tap2deb.py
CHECKPKG_OVERRIDES_CSWpy-twisted += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/twisted/scripts/tap2deb.py

include gar/category.mk
