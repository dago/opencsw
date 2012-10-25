# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = paramiko
VERSION = 1.7.7.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Python module that implements the SSH2 protocol
define BLURB
  Paramiko is a module for Python 2.2 (or higher) that implements the SSH2
  protocol for secure (encrypted and authenticated) connections to remote
  machines. It is written entirely in python and contains no C or
  platform-dependent code.
endef

MASTER_SITES = http://www.lag.net/paramiko/download/
DISTFILES    = $(DISTNAME).tar.gz
ARCHALL      = 1

RUNTIME_DEP_PKGS   = CSWpy-crypto
CHECKPKG_OVERRIDES = surplus-dependency|CSWpy-crypto

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-merge-modulated:
	gsed -i 's,/usr/local/etc/moduli,/opt/csw/etc/ssh/moduli,' \
		$(PKGROOT)$(SITE_PACKAGES)/paramiko/transport.py
	@$(MAKECOOKIE)
