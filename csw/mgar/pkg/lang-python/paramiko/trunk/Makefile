# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = paramiko
VERSION = 1.15.2
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Python module that implements the SSH2 protocol
define BLURB
  Paramiko is a module for Python 2.2 (or higher) that implements the SSH2
  protocol for secure (encrypted and authenticated) connections to remote
  machines. It is written entirely in python and contains no C or
  platform-dependent code.
endef

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

PACKAGES += CSWpy-paramiko
# We stick with upstream naming
CHECKPKG_OVERRIDES_CSWpy-paramiko += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpy-paramiko += catalogname-does-not-start-with-py_
SPKG_DESC_CSWpy-paramiko = Python module that implements the SSH2 protocol
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpy-paramiko += CSWpy-crypto
# checkpkg cannot track this
CHECKPKG_OVERRIDES_CSWpy-paramiko += surplus-dependency|CSWpy-crypto
ARCHALL_CSWpy-paramiko = 1
OBSOLETED_BY_CSWpy-paramiko = CSWparamiko

REINPLACEMENTS += moduli
REINPLACE_MATCH_moduli += /usr/local/etc/moduli
REINPLACE_WITH_moduli += /etc/opt/csw/ssh/moduli
REINPLACE_FILES_moduli += paramiko/transport.py

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
